"""
Feature Engineering module for Credit Risk Scoring Project.

This module handles:
- Aggregation of bureau data (from PostgreSQL)
- Aggregation of previous_application data (from PostgreSQL)
- Aggregation of large CSV files (installments, POS_CASH, credit_card)
- Creation of new features (ratios, indicators)
- Final dataset assembly

Author: Daniela Samo
Date: January 2026
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, Dict, List, Tuple
from sqlalchemy import create_engine, text
import yaml
import os
from dotenv import load_dotenv
import warnings
import gc

warnings.filterwarnings('ignore')
load_dotenv()


class FeatureEngineer:
    """
    Feature engineering class for credit risk scoring.
    """

    def __init__(self, config_path: str = "configs/config.yaml"):
        self.config = self._load_config(config_path)
        self.raw_path = Path(self.config['paths']['data']['raw'])
        self.features_path = Path(self.config['paths']['data']['features'])
        self.engine = self._create_engine()
        self.features_path.mkdir(parents=True, exist_ok=True)
        self.feature_groups = {}

    def _load_config(self, config_path: str) -> dict:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def _create_engine(self):
        host = os.getenv('POSTGRES_HOST', 'localhost')
        port = os.getenv('POSTGRES_PORT', '5432')
        database = os.getenv('POSTGRES_DB', 'credit_risk')
        user = os.getenv('POSTGRES_USER', 'credit_user')
        password = os.getenv('POSTGRES_PASSWORD', '')
        connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        return create_engine(connection_string)

    # =========================================================================
    # APPLICATION FEATURES
    # =========================================================================

    def create_application_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create new features from application_train table."""
        print("Creating application features...")
        df = df.copy()

        # Financial Ratios
        df['credit_income_ratio'] = df['amt_credit'] / (df['amt_income_total'] + 1)
        df['annuity_income_ratio'] = df['amt_annuity'] / (df['amt_income_total'] + 1)
        df['credit_annuity_ratio'] = df['amt_credit'] / (df['amt_annuity'] + 1)
        df['goods_credit_ratio'] = df['amt_goods_price'] / (df['amt_credit'] + 1)
        df['income_per_person'] = df['amt_income_total'] / (df['cnt_fam_members'] + 1)

        # Age Features
        df['age_years'] = -df['days_birth'] / 365
        df['employed_years'] = -df['days_employed'] / 365
        df['employed_years'] = df['employed_years'].clip(lower=0, upper=50)
        df['employed_to_age_ratio'] = df['employed_years'] / (df['age_years'] + 1)
        df['registration_to_age'] = (-df['days_registration'] / 365) / (df['age_years'] + 1)
        df['id_publish_to_age'] = (-df['days_id_publish'] / 365) / (df['age_years'] + 1)

        # Document Indicators
        doc_cols = [c for c in df.columns if c.startswith('flag_document_')]
        df['documents_provided_count'] = df[doc_cols].sum(axis=1)

        # Contact Information
        contact_cols = ['flag_mobil', 'flag_emp_phone', 'flag_work_phone',
                       'flag_cont_mobile', 'flag_phone', 'flag_email']
        existing_contact = [c for c in contact_cols if c in df.columns]
        df['contact_info_count'] = df[existing_contact].sum(axis=1)

        # External Sources
        ext_cols = ['ext_source_1', 'ext_source_2', 'ext_source_3']
        existing_ext = [c for c in ext_cols if c in df.columns]
        df['ext_source_mean'] = df[existing_ext].mean(axis=1)
        df['ext_source_std'] = df[existing_ext].std(axis=1)
        df['ext_source_min'] = df[existing_ext].min(axis=1)
        df['ext_source_max'] = df[existing_ext].max(axis=1)

        self.feature_groups['application'] = [
            'credit_income_ratio', 'annuity_income_ratio', 'credit_annuity_ratio',
            'goods_credit_ratio', 'income_per_person', 'age_years', 'employed_years',
            'employed_to_age_ratio', 'registration_to_age', 'id_publish_to_age',
            'documents_provided_count', 'contact_info_count',
            'ext_source_mean', 'ext_source_std', 'ext_source_min', 'ext_source_max'
        ]

        print(f"  Created {len(self.feature_groups['application'])} application features")
        return df

    # =========================================================================
    # BUREAU FEATURES
    # =========================================================================

    def create_bureau_features(self) -> pd.DataFrame:
        """Create aggregated features from bureau table."""
        print("Creating bureau features from PostgreSQL...")

        query = """
        SELECT
            sk_id_curr,
            COUNT(*) as bureau_credit_count,
            SUM(CASE WHEN credit_active = 'Active' THEN 1 ELSE 0 END) as bureau_active_count,
            SUM(CASE WHEN credit_active = 'Closed' THEN 1 ELSE 0 END) as bureau_closed_count,
            SUM(amt_credit_sum) as bureau_amt_credit_sum_total,
            AVG(amt_credit_sum) as bureau_amt_credit_sum_mean,
            MAX(amt_credit_sum) as bureau_amt_credit_sum_max,
            SUM(amt_credit_sum_debt) as bureau_debt_sum,
            AVG(amt_credit_sum_debt) as bureau_debt_mean,
            SUM(amt_credit_sum_overdue) as bureau_overdue_sum,
            MAX(amt_credit_sum_overdue) as bureau_overdue_max,
            SUM(CASE WHEN amt_credit_sum_overdue > 0 THEN 1 ELSE 0 END) as bureau_overdue_count,
            SUM(cnt_credit_prolong) as bureau_prolong_count,
            AVG(days_credit) as bureau_days_credit_mean,
            MIN(days_credit) as bureau_days_credit_min,
            AVG(days_credit_enddate) as bureau_days_enddate_mean,
            COUNT(DISTINCT credit_type) as bureau_credit_type_count
        FROM credit_risk.bureau
        GROUP BY sk_id_curr
        """

        bureau_agg = pd.read_sql(query, self.engine)

        # Derived features
        bureau_agg['bureau_active_ratio'] = (
            bureau_agg['bureau_active_count'] /
            (bureau_agg['bureau_credit_count'] + 1)
        )
        bureau_agg['bureau_debt_credit_ratio'] = (
            bureau_agg['bureau_debt_sum'] /
            (bureau_agg['bureau_amt_credit_sum_total'] + 1)
        )

        self.feature_groups['bureau'] = [c for c in bureau_agg.columns if c != 'sk_id_curr']

        print(f"  Created {len(self.feature_groups['bureau'])} bureau features")
        print(f"  Clients with bureau history: {len(bureau_agg):,}")

        return bureau_agg

    # =========================================================================
    # PREVIOUS APPLICATION FEATURES
    # =========================================================================

    def create_previous_application_features(self) -> pd.DataFrame:
        """Create aggregated features from previous_application table."""
        print("Creating previous application features from PostgreSQL...")

        query = """
        SELECT
            sk_id_curr,
            COUNT(*) as prev_app_count,
            SUM(CASE WHEN name_contract_status = 'Approved' THEN 1 ELSE 0 END) as prev_approved_count,
            SUM(CASE WHEN name_contract_status = 'Refused' THEN 1 ELSE 0 END) as prev_refused_count,
            SUM(CASE WHEN name_contract_status = 'Canceled' THEN 1 ELSE 0 END) as prev_canceled_count,
            AVG(amt_application) as prev_amt_application_mean,
            MAX(amt_application) as prev_amt_application_max,
            AVG(amt_credit) as prev_amt_credit_mean,
            SUM(amt_credit) as prev_amt_credit_sum,
            AVG(amt_credit - amt_application) as prev_credit_app_diff_mean,
            AVG(amt_annuity) as prev_amt_annuity_mean,
            MAX(amt_annuity) as prev_amt_annuity_max,
            AVG(amt_down_payment) as prev_down_payment_mean,
            AVG(days_decision) as prev_days_decision_mean,
            MIN(days_decision) as prev_days_decision_min,
            COUNT(DISTINCT name_contract_type) as prev_contract_type_count,
            COUNT(DISTINCT name_goods_category) as prev_goods_category_count
        FROM credit_risk.previous_application
        GROUP BY sk_id_curr
        """

        prev_agg = pd.read_sql(query, self.engine)

        # Derived features
        prev_agg['prev_approval_rate'] = (
            prev_agg['prev_approved_count'] /
            (prev_agg['prev_app_count'] + 1)
        )
        prev_agg['prev_refused_rate'] = (
            prev_agg['prev_refused_count'] /
            (prev_agg['prev_app_count'] + 1)
        )

        self.feature_groups['previous_application'] = [c for c in prev_agg.columns if c != 'sk_id_curr']

        print(f"  Created {len(self.feature_groups['previous_application'])} previous application features")
        print(f"  Clients with previous applications: {len(prev_agg):,}")

        return prev_agg

    # =========================================================================
    # INSTALLMENTS FEATURES (from CSV)
    # =========================================================================

    def create_installments_features(self, chunk_size: int = 100000) -> pd.DataFrame:
        """Create aggregated features from installments_payments.csv."""
        print("Creating installments features from CSV (chunked)...")

        file_path = self.raw_path / "installments_payments.csv"
        agg_dict = {}

        for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
            print(f"  Processing chunk {i+1}...", end='\r')

            chunk['payment_delay'] = chunk['DAYS_ENTRY_PAYMENT'] - chunk['DAYS_INSTALMENT']
            chunk['payment_diff'] = chunk['AMT_PAYMENT'] - chunk['AMT_INSTALMENT']
            chunk['is_late'] = (chunk['payment_delay'] > 0).astype(int)

            chunk_agg = chunk.groupby('SK_ID_CURR').agg({
                'SK_ID_PREV': 'count',
                'payment_delay': ['mean', 'max', 'sum'],
                'payment_diff': ['mean', 'sum'],
                'is_late': ['sum', 'mean'],
                'AMT_PAYMENT': ['sum', 'mean'],
                'AMT_INSTALMENT': ['sum', 'mean']
            })

            chunk_agg.columns = [
                'instal_count',
                'instal_delay_mean', 'instal_delay_max', 'instal_delay_sum',
                'instal_payment_diff_mean', 'instal_payment_diff_sum',
                'instal_late_count', 'instal_late_ratio',
                'instal_amt_payment_sum', 'instal_amt_payment_mean',
                'instal_amt_instalment_sum', 'instal_amt_instalment_mean'
            ]

            for idx, row in chunk_agg.iterrows():
                if idx in agg_dict:
                    for col in chunk_agg.columns:
                        if 'sum' in col or 'count' in col:
                            agg_dict[idx][col] = agg_dict[idx].get(col, 0) + row[col]
                        else:
                            agg_dict[idx][col] = row[col]
                else:
                    agg_dict[idx] = row.to_dict()

            del chunk, chunk_agg
            gc.collect()

        print(f"\n  Converting to DataFrame...")
        instal_agg = pd.DataFrame.from_dict(agg_dict, orient='index')
        instal_agg.index.name = 'sk_id_curr'
        instal_agg = instal_agg.reset_index()

        instal_agg['instal_late_ratio'] = (
            instal_agg['instal_late_count'] / (instal_agg['instal_count'] + 1)
        )
        instal_agg['instal_payment_ratio'] = (
            instal_agg['instal_amt_payment_sum'] / (instal_agg['instal_amt_instalment_sum'] + 1)
        )

        self.feature_groups['installments'] = [c for c in instal_agg.columns if c != 'sk_id_curr']

        print(f"  Created {len(self.feature_groups['installments'])} installments features")
        print(f"  Clients with installments: {len(instal_agg):,}")

        return instal_agg

    # =========================================================================
    # POS CASH BALANCE FEATURES (from CSV)
    # =========================================================================

    def create_pos_cash_features(self, chunk_size: int = 100000) -> pd.DataFrame:
        """Create aggregated features from POS_CASH_balance.csv."""
        print("Creating POS cash features from CSV (chunked)...")

        file_path = self.raw_path / "POS_CASH_balance.csv"
        agg_dict = {}

        for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
            print(f"  Processing chunk {i+1}...", end='\r')

            chunk['is_dpd'] = (chunk['SK_DPD'] > 0).astype(int)
            chunk['is_dpd_def'] = (chunk['SK_DPD_DEF'] > 0).astype(int)

            chunk_agg = chunk.groupby('SK_ID_CURR').agg({
                'SK_ID_PREV': 'nunique',
                'MONTHS_BALANCE': ['min', 'max', 'count'],
                'CNT_INSTALMENT': ['mean', 'max'],
                'CNT_INSTALMENT_FUTURE': ['mean', 'min'],
                'SK_DPD': ['sum', 'mean', 'max'],
                'SK_DPD_DEF': ['sum', 'mean', 'max'],
                'is_dpd': 'sum',
                'is_dpd_def': 'sum'
            })

            chunk_agg.columns = [
                'pos_contract_count',
                'pos_months_min', 'pos_months_max', 'pos_record_count',
                'pos_instalment_mean', 'pos_instalment_max',
                'pos_future_instalment_mean', 'pos_future_instalment_min',
                'pos_dpd_sum', 'pos_dpd_mean', 'pos_dpd_max',
                'pos_dpd_def_sum', 'pos_dpd_def_mean', 'pos_dpd_def_max',
                'pos_dpd_count', 'pos_dpd_def_count'
            ]

            for idx, row in chunk_agg.iterrows():
                if idx in agg_dict:
                    for col in chunk_agg.columns:
                        if 'sum' in col or 'count' in col:
                            agg_dict[idx][col] = agg_dict[idx].get(col, 0) + row[col]
                        else:
                            agg_dict[idx][col] = row[col]
                else:
                    agg_dict[idx] = row.to_dict()

            del chunk, chunk_agg
            gc.collect()

        print(f"\n  Converting to DataFrame...")
        pos_agg = pd.DataFrame.from_dict(agg_dict, orient='index')
        pos_agg.index.name = 'sk_id_curr'
        pos_agg = pos_agg.reset_index()

        pos_agg['pos_dpd_ratio'] = (
            pos_agg['pos_dpd_count'] / (pos_agg['pos_record_count'] + 1)
        )

        self.feature_groups['pos_cash'] = [c for c in pos_agg.columns if c != 'sk_id_curr']

        print(f"  Created {len(self.feature_groups['pos_cash'])} POS cash features")
        print(f"  Clients with POS/cash loans: {len(pos_agg):,}")

        return pos_agg

    # =========================================================================
    # CREDIT CARD BALANCE FEATURES (from CSV)
    # =========================================================================

    def create_credit_card_features(self, chunk_size: int = 100000) -> pd.DataFrame:
        """Create aggregated features from credit_card_balance.csv."""
        print("Creating credit card features from CSV (chunked)...")

        file_path = self.raw_path / "credit_card_balance.csv"
        agg_dict = {}

        for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
            print(f"  Processing chunk {i+1}...", end='\r')

            chunk['cc_utilization'] = chunk['AMT_BALANCE'] / (chunk['AMT_CREDIT_LIMIT_ACTUAL'] + 1)
            chunk['is_over_limit'] = (chunk['AMT_BALANCE'] > chunk['AMT_CREDIT_LIMIT_ACTUAL']).astype(int)
            chunk['is_dpd'] = (chunk['SK_DPD'] > 0).astype(int)

            chunk_agg = chunk.groupby('SK_ID_CURR').agg({
                'SK_ID_PREV': 'nunique',
                'MONTHS_BALANCE': ['min', 'max', 'count'],
                'AMT_BALANCE': ['mean', 'max', 'sum'],
                'AMT_CREDIT_LIMIT_ACTUAL': ['mean', 'max'],
                'AMT_DRAWINGS_CURRENT': ['mean', 'sum'],
                'AMT_PAYMENT_TOTAL_CURRENT': ['mean', 'sum'],
                'cc_utilization': ['mean', 'max'],
                'is_over_limit': 'sum',
                'SK_DPD': ['sum', 'mean', 'max'],
                'is_dpd': 'sum'
            })

            chunk_agg.columns = [
                'cc_card_count',
                'cc_months_min', 'cc_months_max', 'cc_record_count',
                'cc_balance_mean', 'cc_balance_max', 'cc_balance_sum',
                'cc_limit_mean', 'cc_limit_max',
                'cc_drawings_mean', 'cc_drawings_sum',
                'cc_payment_mean', 'cc_payment_sum',
                'cc_utilization_mean', 'cc_utilization_max',
                'cc_over_limit_count',
                'cc_dpd_sum', 'cc_dpd_mean', 'cc_dpd_max',
                'cc_dpd_count'
            ]

            for idx, row in chunk_agg.iterrows():
                if idx in agg_dict:
                    for col in chunk_agg.columns:
                        if 'sum' in col or 'count' in col:
                            agg_dict[idx][col] = agg_dict[idx].get(col, 0) + row[col]
                        else:
                            agg_dict[idx][col] = row[col]
                else:
                    agg_dict[idx] = row.to_dict()

            del chunk, chunk_agg
            gc.collect()

        print(f"\n  Converting to DataFrame...")
        cc_agg = pd.DataFrame.from_dict(agg_dict, orient='index')
        cc_agg.index.name = 'sk_id_curr'
        cc_agg = cc_agg.reset_index()

        cc_agg['cc_payment_to_balance_ratio'] = (
            cc_agg['cc_payment_sum'] / (cc_agg['cc_balance_sum'] + 1)
        )

        self.feature_groups['credit_card'] = [c for c in cc_agg.columns if c != 'sk_id_curr']

        print(f"  Created {len(self.feature_groups['credit_card'])} credit card features")
        print(f"  Clients with credit cards: {len(cc_agg):,}")

        return cc_agg

    # =========================================================================
    # MAIN ASSEMBLY
    # =========================================================================

    def build_feature_dataset(
        self,
        include_installments: bool = True,
        include_pos_cash: bool = True,
        include_credit_card: bool = True
    ) -> pd.DataFrame:
        """Build the complete feature dataset."""
        print("="*60)
        print("BUILDING FEATURE DATASET")
        print("="*60)

        # Load base application data
        print("\nLoading application_train from PostgreSQL...")
        app_df = pd.read_sql(
            "SELECT * FROM credit_risk.application_train",
            self.engine
        )
        print(f"  Loaded {len(app_df):,} rows")

        # Create application features
        app_df = self.create_application_features(app_df)

        # Create and merge bureau features
        bureau_df = self.create_bureau_features()
        app_df = app_df.merge(bureau_df, on='sk_id_curr', how='left')
        del bureau_df
        gc.collect()

        # Create and merge previous application features
        prev_df = self.create_previous_application_features()
        app_df = app_df.merge(prev_df, on='sk_id_curr', how='left')
        del prev_df
        gc.collect()

        # Create and merge installments features
        if include_installments:
            instal_df = self.create_installments_features()
            app_df = app_df.merge(instal_df, on='sk_id_curr', how='left')
            del instal_df
            gc.collect()

        # Create and merge POS cash features
        if include_pos_cash:
            pos_df = self.create_pos_cash_features()
            app_df = app_df.merge(pos_df, on='sk_id_curr', how='left')
            del pos_df
            gc.collect()

        # Create and merge credit card features
        if include_credit_card:
            cc_df = self.create_credit_card_features()
            app_df = app_df.merge(cc_df, on='sk_id_curr', how='left')
            del cc_df
            gc.collect()

        # Fill NaN for clients without history
        numeric_cols = app_df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if col not in ['sk_id_curr', 'target']:
                if any(x in col for x in ['count', 'sum']):
                    app_df[col] = app_df[col].fillna(0)
                else:
                    app_df[col] = app_df[col].fillna(app_df[col].median())

        # Summary
        print("\n" + "="*60)
        print("FEATURE DATASET SUMMARY")
        print("="*60)
        print(f"Total rows: {len(app_df):,}")
        print(f"Total columns: {len(app_df.columns)}")
        print(f"\nFeatures by group:")
        for group, features in self.feature_groups.items():
            print(f"  {group}: {len(features)} features")

        return app_df

    def save_features(self, df: pd.DataFrame, filename: str = "features_v1.csv") -> Path:
        """Save the feature dataset to disk."""
        output_path = self.features_path / filename
        df.to_csv(output_path, index=False)
        print(f"\nFeatures saved to: {output_path}")
        print(f"File size: {output_path.stat().st_size / 1024**2:.1f} MB")
        return output_path


def run_feature_engineering():
    """Main function to run feature engineering pipeline."""
    print("="*60)
    print("Credit Risk Scoring - Feature Engineering")
    print("="*60)

    fe = FeatureEngineer()

    features_df = fe.build_feature_dataset(
        include_installments=True,
        include_pos_cash=True,
        include_credit_card=True
    )

    fe.save_features(features_df, "features_v1.csv")

    print("\nFeature engineering complete!")
    return features_df


if __name__ == "__main__":
    import os
    os.chdir(Path(__file__).parent.parent.parent)
    df = run_feature_engineering()
