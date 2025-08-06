"""Database utilities for Collatz sequence data storage."""

import os
import logging
from typing import Optional, List, Dict, Any
import psycopg2
from psycopg2.extras import RealDictCursor, execute_batch
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


class CollatzDatabase:
    """Database connection and operations for Collatz sequence data."""

    def __init__(self, connection_params: Optional[Dict[str, str]] = None):
        """Initialize database connection.

        Args:
            connection_params: Database connection parameters.
                             If None, uses environment variables.
        """
        if connection_params is None:
            connection_params = {
                "host": os.getenv("DB_HOST", "localhost"),
                "port": os.getenv("DB_PORT", "5432"),
                "database": os.getenv("DB_NAME"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD"),
            }

        self.connection_params = connection_params
        self.connection = None
        self.engine = None

    def connect(self):
        """Establish database connection."""
        try:
            self.connection = psycopg2.connect(**self.connection_params)

            # Create SQLAlchemy engine for pandas compatibility
            db_url = f"postgresql://{self.connection_params['user']}:{self.connection_params['password']}@{self.connection_params['host']}:{self.connection_params['port']}/{self.connection_params['database']}"
            self.engine = create_engine(db_url)

            logging.info("Database connection established")
        except Exception as e:
            logging.error(f"Failed to connect to database: {e}")
            raise

    def disconnect(self):
        """Close database connection."""
        if self.engine:
            self.engine.dispose()
            self.engine = None
        if self.connection:
            self.connection.close()
            self.connection = None
            logging.info("Database connection closed")

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()

    def insert_collatz_sequences(self, data: List[Dict[str, Any]]) -> int:
        """Insert Collatz sequence data into the database.

        Args:
            data: List of dictionaries containing sequence data

        Returns:
            Number of records inserted
        """
        if not self.connection:
            raise RuntimeError("Database connection not established")

        insert_query = """
            INSERT INTO collatz_sequences 
            (starting_number, sequence_length, max_value, total_steps, stopping_time)
            VALUES (%(starting_number)s, %(sequence_length)s, %(max_value)s, 
                   %(total_steps)s, %(stopping_time)s)
            ON CONFLICT (starting_number) DO UPDATE SET
                sequence_length = EXCLUDED.sequence_length,
                max_value = EXCLUDED.max_value,
                total_steps = EXCLUDED.total_steps,
                stopping_time = EXCLUDED.stopping_time,
                updated_at = CURRENT_TIMESTAMP
        """

        try:
            with self.connection.cursor() as cursor:
                execute_batch(cursor, insert_query, data, page_size=1000)
                self.connection.commit()
                return len(data)
        except Exception as e:
            self.connection.rollback()
            logging.error(f"Failed to insert data: {e}")
            raise

    def get_sequences_dataframe(self, limit: Optional[int] = None) -> pd.DataFrame:
        """Retrieve Collatz sequences as a pandas DataFrame.

        Args:
            limit: Maximum number of records to retrieve

        Returns:
            DataFrame containing sequence data
        """
        if not self.connection:
            raise RuntimeError("Database connection not established")

        query = "SELECT * FROM collatz_sequences ORDER BY starting_number"
        if limit:
            query += f" LIMIT {limit}"

        try:
            return pd.read_sql_query(query, self.engine)
        except Exception as e:
            logging.error(f"Failed to retrieve data: {e}")
            raise

    def insert_analysis_result(
        self,
        analysis_type: str,
        range_start: int,
        range_end: int,
        total_sequences: int,
        avg_sequence_length: float,
        max_sequence_length: int,
        min_sequence_length: int,
        avg_max_value: float,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> int:
        """Insert analysis results into the database.

        Args:
            analysis_type: Type of analysis performed
            range_start: Starting number of the range
            range_end: Ending number of the range
            total_sequences: Total number of sequences analyzed
            avg_sequence_length: Average sequence length
            max_sequence_length: Maximum sequence length
            min_sequence_length: Minimum sequence length
            avg_max_value: Average maximum value in sequences
            metadata: Additional metadata as JSON

        Returns:
            ID of the inserted analysis result
        """
        if not self.connection:
            raise RuntimeError("Database connection not established")

        insert_query = """
            INSERT INTO analysis_results 
            (analysis_type, range_start, range_end, total_sequences,
             avg_sequence_length, max_sequence_length, min_sequence_length,
             avg_max_value, metadata)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    insert_query,
                    (
                        analysis_type,
                        range_start,
                        range_end,
                        total_sequences,
                        avg_sequence_length,
                        max_sequence_length,
                        min_sequence_length,
                        avg_max_value,
                        metadata,
                    ),
                )
                result_id = cursor.fetchone()[0]
                self.connection.commit()
                return result_id
        except Exception as e:
            self.connection.rollback()
            logging.error(f"Failed to insert analysis result: {e}")
            raise

    def check_connection(self) -> bool:
        """Check if database connection is working.

        Returns:
            True if connection is working, False otherwise
        """
        try:
            if not self.connection:
                return False
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                return cursor.fetchone()[0] == 1
        except Exception:
            return False


def get_database_connection() -> CollatzDatabase:
    """Get a database connection using environment variables.

    Returns:
        CollatzDatabase instance
    """
    return CollatzDatabase()
