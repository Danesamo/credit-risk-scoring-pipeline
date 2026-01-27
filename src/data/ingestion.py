"""
Data Ingestion module for Credit Risk Scoring Project.

This module handles loading CSV data into PostgreSQL database.
Uses chunked loading for large files to manage memory.

Author: Daniela Samo
Date: January 2026
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, List
import yaml
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()


class DataIngestion:
    """
    Handles data ingestion from CSV files to PostgreSQL.

    Supports chunked loading for large files and progress tracking.
    """

    def __init__(self, config_path: str = "configs/config.yaml"):
        """
        Initialize the ingestion handler.

        Args:
            config_path: Path to configuration file
        """
        self.config = self._load_config(config_path)
        self.raw_path = Path(self.config['paths']['data']['raw'])
        self.engine = self._create_engine()

    def _load_config(self, config_path: str) -> dict:
        """Load configuration from YAML file."""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def _create_engine(self) -> Engine:
        """Create SQLAlchemy engine for PostgreSQL connection."""
        host = os.getenv('POSTGRES_HOST', 'localhost')
        port = os.getenv('POSTGRES_PORT', '5432')
        database = os.getenv('POSTGRES_DB', 'credit_risk')
        user = os.getenv('POSTGRES_USER', 'credit_user')
        password = os.getenv('POSTGRES_PASSWORD', '')

        connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"

        return create_engine(connection_string)

    def test_connection(self) -> bool:
        """
        Test the database connection.

        Returns:
            True if connection successful, False otherwise
        """
        try:
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Database connection successful!")
            return True
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False

    def load_csv_to_postgres(
        self,
        table_name: str,
        csv_filename: Optional[str] = None,
        schema: str = "credit_risk",
        chunk_size: int = 10000,
        if_exists: str = "replace"
    ) -> int:
        """
        Load a CSV file into PostgreSQL table.

        Args:
            table_name: Name of the target table
            csv_filename: CSV filename (defaults to table_name.csv)
            schema: Database schema
            chunk_size: Number of rows per chunk for large files
            if_exists: What to do if table exists ('replace', 'append', 'fail')

        Returns:
            Number of rows loaded
        """
        if csv_filename is None:
            csv_filename = f"{table_name}.csv"

        file_path = self.raw_path / csv_filename

        if not file_path.exists():
            raise FileNotFoundError(f"CSV file not found: {file_path}")

        print(f"\nLoading {csv_filename} into {schema}.{table_name}...")

        # Get file size for progress estimation
        file_size_mb = file_path.stat().st_size / (1024 * 1024)
        print(f"  File size: {file_size_mb:.1f} MB")

        start_time = time.time()
        total_rows = 0

        # Read and load in chunks
        chunks = pd.read_csv(file_path, chunksize=chunk_size)

        for i, chunk in enumerate(chunks):
            # Clean column names (lowercase, no spaces)
            chunk.columns = chunk.columns.str.lower().str.replace(' ', '_')

            # Determine if_exists for first chunk vs subsequent
            mode = if_exists if i == 0 else 'append'

            chunk.to_sql(
                name=table_name,
                con=self.engine,
                schema=schema,
                if_exists=mode,
                index=False,
                method='multi'
            )

            total_rows += len(chunk)
            print(f"  Loaded chunk {i+1}: {total_rows:,} rows...", end='\r')

        elapsed_time = time.time() - start_time
        print(f"\n  Completed: {total_rows:,} rows in {elapsed_time:.1f}s")

        return total_rows

    def load_main_tables(self) -> dict:
        """
        Load the main tables into PostgreSQL.

        Tables loaded:
        - application_train (main table with TARGET)
        - bureau (credit history from other institutions)
        - previous_application (previous applications at Home Credit)

        Returns:
            Dictionary with table names and row counts
        """
        tables_to_load = [
            ("application_train", "application_train.csv"),
            ("bureau", "bureau.csv"),
            ("previous_application", "previous_application.csv"),
        ]

        results = {}

        for table_name, csv_file in tables_to_load:
            try:
                rows = self.load_csv_to_postgres(
                    table_name=table_name,
                    csv_filename=csv_file,
                    chunk_size=10000
                )
                results[table_name] = rows
            except Exception as e:
                print(f"  Error loading {table_name}: {e}")
                results[table_name] = -1

        return results

    def verify_load(self, schema: str = "credit_risk") -> pd.DataFrame:
        """
        Verify data was loaded correctly by checking row counts.

        Args:
            schema: Database schema

        Returns:
            DataFrame with table names and row counts
        """
        query = f"""
        SELECT
            table_name,
            (SELECT COUNT(*) FROM {schema}."" || table_name || "") as row_count
        FROM information_schema.tables
        WHERE table_schema = '{schema}'
        AND table_type = 'BASE TABLE'
        """

        # Simpler approach - check each table individually
        tables = ['application_train', 'bureau', 'previous_application']
        results = []

        for table in tables:
            try:
                with self.engine.connect() as conn:
                    result = conn.execute(
                        text(f"SELECT COUNT(*) FROM {schema}.{table}")
                    )
                    count = result.scalar()
                    results.append({'table': table, 'rows': count})
            except Exception as e:
                results.append({'table': table, 'rows': f'Error: {e}'})

        return pd.DataFrame(results)

    def get_table_info(self, table_name: str, schema: str = "credit_risk") -> pd.DataFrame:
        """
        Get information about a table's columns.

        Args:
            table_name: Name of the table
            schema: Database schema

        Returns:
            DataFrame with column information
        """
        query = f"""
        SELECT
            column_name,
            data_type,
            is_nullable
        FROM information_schema.columns
        WHERE table_schema = '{schema}'
        AND table_name = '{table_name}'
        ORDER BY ordinal_position
        """

        with self.engine.connect() as conn:
            return pd.read_sql(query, conn)


def run_ingestion():
    """Main function to run the data ingestion process."""
    print("=" * 60)
    print("Credit Risk Scoring - Data Ingestion")
    print("=" * 60)

    # Initialize ingestion handler
    ingestion = DataIngestion()

    # Test connection
    if not ingestion.test_connection():
        print("Aborting: Cannot connect to database")
        return

    # Load main tables
    print("\nLoading main tables...")
    results = ingestion.load_main_tables()

    # Summary
    print("\n" + "=" * 60)
    print("INGESTION SUMMARY")
    print("=" * 60)
    for table, rows in results.items():
        status = "OK" if rows > 0 else "FAILED"
        print(f"  {table}: {rows:,} rows [{status}]")

    # Verify
    print("\nVerifying loaded data...")
    verification = ingestion.verify_load()
    print(verification.to_string(index=False))

    print("\nIngestion complete!")


if __name__ == "__main__":
    import os
    os.chdir(Path(__file__).parent.parent.parent)  # Change to project root
    run_ingestion()
