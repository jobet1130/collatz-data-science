"""Database connection and basic functionality tests."""

import os
import pytest
import psycopg2
from psycopg2.extras import RealDictCursor


@pytest.fixture
def db_connection():
    """Create a database connection for testing."""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME", "collatz_db_test"),
        user=os.getenv("DB_USER", "postgresql"),
        password=os.getenv("DB_PASSWORD", "test_password"),
    )
    yield conn
    conn.close()


@pytest.mark.database
def test_database_connection(db_connection):
    """Test that we can connect to the database."""
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        assert result[0] == 1


@pytest.mark.database
def test_tables_exist(db_connection):
    """Test that all required tables exist."""
    expected_tables = {
        "collatz_sequences",
        "sequence_steps",
        "analysis_results",
        "experiments",
        "batch_jobs",
        "performance_metrics",
    }

    with db_connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
        """
        )
        tables = {row[0] for row in cursor.fetchall()}

    assert expected_tables.issubset(
        tables
    ), f"Missing tables: {expected_tables - tables}"


@pytest.mark.database
def test_views_exist(db_connection):
    """Test that all required views exist."""
    expected_views = {
        "sequence_statistics",
        "sequence_length_distribution",
        "top_longest_sequences",
        "top_peak_sequences",
        "recent_analysis_summary",
        "experiment_status_overview",
        "batch_job_progress",
        "performance_summary",
        "daily_processing_stats",
        "active_experiments",
    }

    with db_connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT table_name 
            FROM information_schema.views 
            WHERE table_schema = 'public'
        """
        )
        views = {row[0] for row in cursor.fetchall()}

    assert expected_views.issubset(views), f"Missing views: {expected_views - views}"


@pytest.mark.database
def test_functions_exist(db_connection):
    """Test that custom functions exist."""
    expected_functions = {
        "calculate_collatz_length",
        "calculate_collatz_max",
        "get_range_statistics",
        "upsert_collatz_sequence",
        "cleanup_old_metrics",
        "update_updated_at_column",
    }

    with db_connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT routine_name 
            FROM information_schema.routines 
            WHERE routine_schema = 'public' AND routine_type = 'FUNCTION'
        """
        )
        functions = {row[0] for row in cursor.fetchall()}

    assert expected_functions.issubset(
        functions
    ), f"Missing functions: {expected_functions - functions}"


@pytest.mark.database
def test_collatz_function(db_connection):
    """Test the calculate_collatz_length function."""
    with db_connection.cursor() as cursor:
        # Test known Collatz sequence: 27 -> 111 steps
        cursor.execute("SELECT calculate_collatz_length(27)")
        result = cursor.fetchone()[0]
        assert result == 111

        # Test known Collatz sequence: 1 -> 0 steps
        cursor.execute("SELECT calculate_collatz_length(1)")
        result = cursor.fetchone()[0]
        assert result == 0


@pytest.mark.database
def test_collatz_max_function(db_connection):
    """Test the calculate_collatz_max function."""
    with db_connection.cursor() as cursor:
        # Test known Collatz sequence: 27 -> max value 9232
        cursor.execute("SELECT calculate_collatz_max(27)")
        result = cursor.fetchone()[0]
        assert result == 9232

        # Test known Collatz sequence: 1 -> max value 1
        cursor.execute("SELECT calculate_collatz_max(1)")
        result = cursor.fetchone()[0]
        assert result == 1


@pytest.mark.database
def test_sequence_statistics_view(db_connection):
    """Test that the sequence_statistics view returns data."""
    with db_connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM sequence_statistics LIMIT 1")
        result = cursor.fetchone()

        # Check that we get a result and it has expected columns
        assert result is not None
        expected_columns = {
            "total_sequences",
            "min_starting_number",
            "max_starting_number",
            "avg_sequence_length",
            "min_sequence_length",
            "max_sequence_length",
            "median_sequence_length",
            "avg_max_value",
            "min_max_value",
            "max_max_value",
            "avg_total_steps",
            "min_total_steps",
            "max_total_steps",
            "sequences_with_stopping_time",
        }
        assert set(result.keys()).issuperset(expected_columns)
