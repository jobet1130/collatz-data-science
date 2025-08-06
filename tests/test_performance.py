"""Performance benchmarks for Collatz sequence calculations."""

import pytest

from src.collatz.sequence import (
    collatz_length,
    collatz_max_value,
    collatz_sequence,
)


class TestCollatzPerformance:
    """Performance benchmark tests for Collatz sequence functions."""

    @pytest.mark.benchmark
    def test_sequence_length_performance_small(self, benchmark):
        """Benchmark sequence length calculation for small numbers."""
        result = benchmark(collatz_length, 100)
        assert result > 0

    @pytest.mark.benchmark
    def test_sequence_length_performance_medium(self, benchmark):
        """Benchmark sequence length calculation for medium numbers."""
        result = benchmark(collatz_length, 1000)
        assert result > 0

    @pytest.mark.benchmark
    def test_sequence_length_performance_large(self, benchmark):
        """Benchmark sequence length calculation for large numbers."""
        result = benchmark(collatz_length, 10000)
        assert result > 0

    @pytest.mark.benchmark
    def test_sequence_max_performance_small(self, benchmark):
        """Benchmark sequence max calculation for small numbers."""
        result = benchmark(collatz_max_value, 100)
        assert result >= 100

    @pytest.mark.benchmark
    def test_sequence_max_performance_medium(self, benchmark):
        """Benchmark sequence max calculation for medium numbers."""
        result = benchmark(collatz_max_value, 1000)
        assert result >= 1000

    @pytest.mark.benchmark
    def test_sequence_max_performance_large(self, benchmark):
        """Benchmark sequence max calculation for large numbers."""
        result = benchmark(collatz_max_value, 10000)
        assert result >= 10000

    @pytest.mark.benchmark
    def test_sequence_generation_performance_small(self, benchmark):
        """Benchmark sequence generation for small numbers."""
        result = benchmark(collatz_sequence, 100)
        assert len(result) > 0
        assert result[0] == 100
        assert result[-1] == 1

    @pytest.mark.benchmark
    def test_sequence_generation_performance_medium(self, benchmark):
        """Benchmark sequence generation for medium numbers."""
        result = benchmark(collatz_sequence, 1000)
        assert len(result) > 0
        assert result[0] == 1000
        assert result[-1] == 1

    @pytest.mark.benchmark
    def test_sequence_generation_performance_large(self, benchmark):
        """Benchmark sequence generation for large numbers."""
        result = benchmark(collatz_sequence, 10000)
        assert len(result) > 0
        assert result[0] == 10000
        assert result[-1] == 1


@pytest.mark.benchmark
@pytest.mark.parametrize("n", [10, 50, 100, 500, 1000])
def test_sequence_length_scaling(benchmark, n):
    """Test how sequence length calculation scales with input size."""
    result = benchmark(collatz_length, n)
    assert result > 0


@pytest.mark.benchmark
@pytest.mark.parametrize("n", [10, 50, 100, 500, 1000])
def test_sequence_max_scaling(benchmark, n):
    """Test how sequence max calculation scales with input size."""
    result = benchmark(collatz_max_value, n)
    assert result >= n


@pytest.mark.benchmark
@pytest.mark.parametrize("n", [10, 50, 100, 500, 1000])
def test_sequence_generation_scaling(benchmark, n):
    """Test how sequence generation scales with input size."""
    result = benchmark(collatz_sequence, n)
    assert len(result) > 0
    assert result[0] == n
    assert result[-1] == 1


@pytest.mark.benchmark
def test_batch_sequence_length_performance(benchmark):
    """Benchmark calculating sequence lengths for multiple numbers."""

    def batch_calculation():
        return [collatz_length(i) for i in range(1, 101)]

    result = benchmark(batch_calculation)
    assert len(result) == 100
    assert all(length >= 0 for length in result)


@pytest.mark.benchmark
def test_batch_sequence_max_performance(benchmark):
    """Benchmark calculating sequence maxes for multiple numbers."""

    def batch_calculation():
        return [collatz_max_value(i) for i in range(1, 101)]

    result = benchmark(batch_calculation)
    assert len(result) == 100
    assert all(max_val >= i for i, max_val in enumerate(result, 1))
