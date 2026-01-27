"""
Preprocessing module for Credit Risk Scoring Project.

This module handles:
- Data loading from CSV files
- Missing values imputation
- Outlier treatment
- Anomaly correction
- Data type optimization

Author: Daniela Samo
Date: January 2026
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, Dict, List, Tuple, Union
import yaml
import warnings

warnings.filterwarnings('ignore')


class DataPreprocessor:
    """
    Preprocessor class for credit risk data.

    Handles loading, cleaning, and preparing data for feature engineering.
    """

    def __init__(self, config_path: str = "configs/config.yaml"):
        """
        Initialize the preprocessor with configuration.

        Args:
            config_path: Path to the configuration file
        """
        self.config = self._load_config(config_path)
        self.raw_path = Path(self.config['paths']['data']['raw'])
        self.processed_path = Path(self.config['paths']['data']['processed'])

        # Ensure processed directory exists
        self.processed_path.mkdir(parents=True, exist_ok=True)

        # Store preprocessing statistics
        self.stats = {}

    def _load_config(self, config_path: str) -> dict:
        """Load configuration from YAML file."""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def load_data(self, table_name: str) -> pd.DataFrame:
        """
        Load a specific table from raw data.

        Args:
            table_name: Name of the table to load

        Returns:
            DataFrame with the loaded data
        """
        file_path = self.raw_path / f"{table_name}.csv"

        if not file_path.exists():
            raise FileNotFoundError(f"Data file not found: {file_path}")

        print(f"Loading {table_name}...")
        df = pd.read_csv(file_path)
        print(f"  Loaded {len(df):,} rows, {len(df.columns)} columns")

        return df

    def get_missing_stats(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate missing value statistics for a DataFrame.

        Args:
            df: Input DataFrame

        Returns:
            DataFrame with missing value statistics
        """
        missing = df.isnull().sum()
        missing_pct = (missing / len(df)) * 100

        stats = pd.DataFrame({
            'missing_count': missing,
            'missing_pct': missing_pct
        }).sort_values('missing_pct', ascending=False)

        return stats[stats['missing_count'] > 0]

    def fix_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fix known anomalies in the application data.

        Known anomalies:
        - DAYS_EMPLOYED = 365243 (placeholder for unemployed/retired)
        - Negative DAYS values (days before application)

        Args:
            df: Input DataFrame (application_train or application_test)

        Returns:
            DataFrame with fixed anomalies
        """
        df = df.copy()

        # Fix DAYS_EMPLOYED anomaly (365243 = ~1000 years, obviously a placeholder)
        if 'DAYS_EMPLOYED' in df.columns:
            anomaly_mask = df['DAYS_EMPLOYED'] == 365243
            anomaly_count = anomaly_mask.sum()

            if anomaly_count > 0:
                # Create indicator variable for this anomaly
                df['DAYS_EMPLOYED_ANOMALY'] = anomaly_mask.astype(int)
                # Replace with NaN (will be imputed later)
                df.loc[anomaly_mask, 'DAYS_EMPLOYED'] = np.nan
                print(f"  Fixed DAYS_EMPLOYED anomaly: {anomaly_count:,} rows")

        return df

    def impute_missing_values(
        self,
        df: pd.DataFrame,
        numeric_strategy: str = 'median',
        categorical_strategy: str = 'mode',
        special_value: Optional[float] = None
    ) -> pd.DataFrame:
        """
        Impute missing values in the DataFrame.

        Args:
            df: Input DataFrame
            numeric_strategy: Strategy for numeric columns ('median', 'mean', 'zero', 'special')
            categorical_strategy: Strategy for categorical columns ('mode', 'unknown')
            special_value: Value to use when strategy is 'special'

        Returns:
            DataFrame with imputed values
        """
        df = df.copy()

        # Identify column types
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

        # Impute numeric columns
        for col in numeric_cols:
            if df[col].isnull().sum() > 0:
                if numeric_strategy == 'median':
                    fill_value = df[col].median()
                elif numeric_strategy == 'mean':
                    fill_value = df[col].mean()
                elif numeric_strategy == 'zero':
                    fill_value = 0
                elif numeric_strategy == 'special':
                    fill_value = special_value if special_value is not None else -999
                else:
                    fill_value = df[col].median()

                df[col] = df[col].fillna(fill_value)

        # Impute categorical columns
        for col in categorical_cols:
            if df[col].isnull().sum() > 0:
                if categorical_strategy == 'mode':
                    fill_value = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
                else:
                    fill_value = 'Unknown'

                df[col] = df[col].fillna(fill_value)

        return df

    def drop_high_missing_columns(
        self,
        df: pd.DataFrame,
        threshold: float = 0.8
    ) -> Tuple[pd.DataFrame, List[str]]:
        """
        Drop columns with missing values above threshold.

        Args:
            df: Input DataFrame
            threshold: Maximum allowed missing ratio (default 0.8 = 80%)

        Returns:
            Tuple of (cleaned DataFrame, list of dropped columns)
        """
        missing_pct = df.isnull().sum() / len(df)
        cols_to_drop = missing_pct[missing_pct > threshold].index.tolist()

        if cols_to_drop:
            print(f"  Dropping {len(cols_to_drop)} columns with >{threshold*100:.0f}% missing values")
            df = df.drop(columns=cols_to_drop)

        return df, cols_to_drop

    def cap_outliers(
        self,
        df: pd.DataFrame,
        columns: Optional[List[str]] = None,
        lower_percentile: float = 0.01,
        upper_percentile: float = 0.99
    ) -> pd.DataFrame:
        """
        Cap outliers using percentile-based clipping.

        Args:
            df: Input DataFrame
            columns: List of columns to cap (if None, all numeric columns)
            lower_percentile: Lower percentile for capping
            upper_percentile: Upper percentile for capping

        Returns:
            DataFrame with capped outliers
        """
        df = df.copy()

        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns.tolist()

        for col in columns:
            if col in df.columns:
                lower = df[col].quantile(lower_percentile)
                upper = df[col].quantile(upper_percentile)
                df[col] = df[col].clip(lower=lower, upper=upper)

        return df

    def optimize_dtypes(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Optimize DataFrame memory usage by downcasting dtypes.

        Args:
            df: Input DataFrame

        Returns:
            DataFrame with optimized dtypes
        """
        df = df.copy()

        initial_mem = df.memory_usage(deep=True).sum() / 1024**2

        # Downcast integers
        int_cols = df.select_dtypes(include=['int64']).columns
        for col in int_cols:
            df[col] = pd.to_numeric(df[col], downcast='integer')

        # Downcast floats
        float_cols = df.select_dtypes(include=['float64']).columns
        for col in float_cols:
            df[col] = pd.to_numeric(df[col], downcast='float')

        # Convert object columns with low cardinality to category
        obj_cols = df.select_dtypes(include=['object']).columns
        for col in obj_cols:
            if df[col].nunique() / len(df) < 0.5:  # Less than 50% unique values
                df[col] = df[col].astype('category')

        final_mem = df.memory_usage(deep=True).sum() / 1024**2
        print(f"  Memory optimization: {initial_mem:.1f} MB -> {final_mem:.1f} MB ({(1-final_mem/initial_mem)*100:.1f}% reduction)")

        return df

    def preprocess_application(
        self,
        df: pd.DataFrame,
        drop_high_missing: bool = True,
        missing_threshold: float = 0.7,
        cap_outliers: bool = False
    ) -> pd.DataFrame:
        """
        Full preprocessing pipeline for application data.

        Args:
            df: Application DataFrame (train or test)
            drop_high_missing: Whether to drop columns with high missing values
            missing_threshold: Threshold for dropping columns
            cap_outliers: Whether to cap outliers

        Returns:
            Preprocessed DataFrame
        """
        print("Preprocessing application data...")

        # Step 1: Fix anomalies
        df = self.fix_anomalies(df)

        # Step 2: Drop high missing columns (optional)
        dropped_cols = []
        if drop_high_missing:
            df, dropped_cols = self.drop_high_missing_columns(df, threshold=missing_threshold)

        # Step 3: Cap outliers (optional)
        if cap_outliers:
            # Don't cap ID columns or binary columns
            exclude_cols = ['SK_ID_CURR', 'TARGET'] + [c for c in df.columns if df[c].nunique() <= 2]
            numeric_cols = [c for c in df.select_dtypes(include=[np.number]).columns if c not in exclude_cols]
            df = self.cap_outliers(df, columns=numeric_cols)

        # Step 4: Impute missing values
        df = self.impute_missing_values(df)

        # Step 5: Optimize dtypes
        df = self.optimize_dtypes(df)

        # Store statistics
        self.stats['dropped_columns'] = dropped_cols
        self.stats['final_shape'] = df.shape

        print(f"  Final shape: {df.shape[0]:,} rows, {df.shape[1]} columns")

        return df

    def save_processed_data(self, df: pd.DataFrame, filename: str) -> Path:
        """
        Save processed data to the processed directory.

        Args:
            df: DataFrame to save
            filename: Output filename

        Returns:
            Path to saved file
        """
        output_path = self.processed_path / filename
        df.to_csv(output_path, index=False)
        print(f"  Saved to {output_path}")
        return output_path


def preprocess_main_table(
    raw_path: str = "data/raw",
    processed_path: str = "data/processed",
    config_path: str = "configs/config.yaml"
) -> pd.DataFrame:
    """
    Main function to preprocess the application_train table.

    Args:
        raw_path: Path to raw data
        processed_path: Path to save processed data
        config_path: Path to config file

    Returns:
        Preprocessed DataFrame
    """
    # Initialize preprocessor
    preprocessor = DataPreprocessor(config_path)

    # Load data
    df = preprocessor.load_data("application_train")

    # Preprocess
    df_processed = preprocessor.preprocess_application(
        df,
        drop_high_missing=True,
        missing_threshold=0.7,
        cap_outliers=False  # We'll do this more carefully in feature engineering
    )

    # Save
    preprocessor.save_processed_data(df_processed, "application_train_processed.csv")

    return df_processed


if __name__ == "__main__":
    # Run preprocessing when script is executed directly
    import os
    os.chdir(Path(__file__).parent.parent.parent)  # Change to project root

    df = preprocess_main_table()
    print("\nPreprocessing complete!")
    print(f"Shape: {df.shape}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
