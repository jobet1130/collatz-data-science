"""Unit tests for Collatz sequence calculations."""

import pytest


def collatz_sequence_length(n):
    """Calculate the length of the Collatz sequence for a given number."""
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    length = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def collatz_sequence_max(n):
    """Calculate the maximum value in the Collatz sequence for a given number."""
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    max_value = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        max_value = max(max_value, n)
    return max_value


def generate_collatz_sequence(n):
    """Generate the complete Collatz sequence for a given number."""
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


class TestCollatzSequenceLength:
    """Test cases for Collatz sequence length calculation."""

    @pytest.mark.unit
    def test_length_of_one(self):
        """Test that the length of sequence starting with 1 is 0."""
        assert collatz_sequence_length(1) == 0

    @pytest.mark.unit
    def test_length_of_two(self):
        """Test that the length of sequence starting with 2 is 1."""
        assert collatz_sequence_length(2) == 1

    @pytest.mark.unit
    def test_length_of_three(self):
        """Test that the length of sequence starting with 3 is 7."""
        assert collatz_sequence_length(3) == 7

    @pytest.mark.unit
    def test_length_of_four(self):
        """Test that the length of sequence starting with 4 is 2."""
        assert collatz_sequence_length(4) == 2

    @pytest.mark.unit
    def test_length_of_twenty_seven(self):
        """Test that the length of sequence starting with 27 is 111."""
        assert collatz_sequence_length(27) == 111

    @pytest.mark.unit
    def test_invalid_input_zero(self):
        """Test that zero raises ValueError."""
        with pytest.raises(ValueError, match="Input must be a positive integer"):
            collatz_sequence_length(0)

    @pytest.mark.unit
    def test_invalid_input_negative(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match="Input must be a positive integer"):
            collatz_sequence_length(-5)


class TestCollatzSequenceMax:
    """Test cases for Collatz sequence maximum value calculation."""

    @pytest.mark.unit
    def test_max_of_one(self):
        """Test that the max value of sequence starting with 1 is 1."""
        assert collatz_sequence_max(1) == 1

    @pytest.mark.unit
    def test_max_of_two(self):
        """Test that the max value of sequence starting with 2 is 2."""
        assert collatz_sequence_max(2) == 2

    @pytest.mark.unit
    def test_max_of_three(self):
        """Test that the max value of sequence starting with 3 is 16."""
        assert collatz_sequence_max(3) == 16

    @pytest.mark.unit
    def test_max_of_twenty_seven(self):
        """Test that the max value of sequence starting with 27 is 9232."""
        assert collatz_sequence_max(27) == 9232

    @pytest.mark.unit
    def test_invalid_input_zero(self):
        """Test that zero raises ValueError."""
        with pytest.raises(ValueError, match="Input must be a positive integer"):
            collatz_sequence_max(0)

    @pytest.mark.unit
    def test_invalid_input_negative(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match="Input must be a positive integer"):
            collatz_sequence_max(-5)


class TestCollatzSequenceGeneration:
    """Test cases for Collatz sequence generation."""

    @pytest.mark.unit
    def test_sequence_of_one(self):
        """Test that the sequence starting with 1 is [1]."""
        assert generate_collatz_sequence(1) == [1]

    @pytest.mark.unit
    def test_sequence_of_two(self):
        """Test that the sequence starting with 2 is [2, 1]."""
        assert generate_collatz_sequence(2) == [2, 1]

    @pytest.mark.unit
    def test_sequence_of_three(self):
        """Test that the sequence starting with 3 follows the expected pattern."""
        expected = [3, 10, 5, 16, 8, 4, 2, 1]
        assert generate_collatz_sequence(3) == expected

    @pytest.mark.unit
    def test_sequence_of_four(self):
        """Test that the sequence starting with 4 is [4, 2, 1]."""
        assert generate_collatz_sequence(4) == [4, 2, 1]

    @pytest.mark.unit
    def test_sequence_ends_with_one(self):
        """Test that all sequences end with 1."""
        for n in range(1, 20):
            sequence = generate_collatz_sequence(n)
            assert sequence[-1] == 1, f"Sequence for {n} does not end with 1"

    @pytest.mark.unit
    def test_sequence_starts_with_input(self):
        """Test that all sequences start with the input number."""
        for n in range(1, 20):
            sequence = generate_collatz_sequence(n)
            assert sequence[0] == n, f"Sequence for {n} does not start with {n}"

    @pytest.mark.unit
    def test_invalid_input_zero(self):
        """Test that zero raises ValueError."""
        with pytest.raises(ValueError, match="Input must be a positive integer"):
            generate_collatz_sequence(0)

    @pytest.mark.unit
    def test_invalid_input_negative(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match="Input must be a positive integer"):
            generate_collatz_sequence(-5)


@pytest.mark.slow
@pytest.mark.unit
def test_large_number_performance():
    """Test that large numbers can be processed (marked as slow test)."""
    # This test is marked as slow and can be skipped with -m "not slow"
    result = collatz_sequence_length(1000)
    assert isinstance(result, int)
    assert result > 0


@pytest.mark.parametrize(
    "n,expected_length",
    [(1, 0), (2, 1), (3, 7), (4, 2), (5, 5), (6, 8), (7, 16), (8, 3), (9, 19), (10, 6)],
)
@pytest.mark.unit
def test_known_sequence_lengths(n, expected_length):
    """Test known sequence lengths using parametrized tests."""
    assert collatz_sequence_length(n) == expected_length


@pytest.mark.parametrize(
    "n,expected_max",
    [
        (1, 1),
        (2, 2),
        (3, 16),
        (4, 4),
        (5, 16),
        (6, 16),
        (7, 52),
        (8, 8),
        (9, 52),
        (10, 16),
    ],
)
@pytest.mark.unit
def test_known_sequence_maxes(n, expected_max):
    """Test known sequence maximum values using parametrized tests."""
    assert collatz_sequence_max(n) == expected_max
