"""Core Collatz sequence analysis functions.

This module provides the fundamental functionality for generating and analyzing
Collatz sequences (also known as the 3n+1 problem).
"""

import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class CollatzSequence:
    """A class to represent and analyze a Collatz sequence."""

    def __init__(self, starting_number: int):
        """Initialize a Collatz sequence with a starting number.

        Args:
            starting_number: The positive integer to start the sequence with.

        Raises:
            ValueError: If starting_number is not a positive integer.
        """
        if not isinstance(starting_number, int) or starting_number <= 0:
            raise ValueError("Starting number must be a positive integer")

        self.starting_number = starting_number
        self.sequence = self._generate_sequence()

    def _generate_sequence(self) -> List[int]:
        """Generate the complete Collatz sequence.

        Returns:
            List of integers representing the Collatz sequence.
        """
        sequence = []
        n = self.starting_number

        while n != 1:
            sequence.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1

        sequence.append(1)  # Add the final 1
        return sequence

    def get_length(self) -> int:
        """Get the length of the sequence.

        Returns:
            The number of steps to reach 1.
        """
        return len(self.sequence)

    def get_max_value(self) -> int:
        """Get the maximum value in the sequence.

        Returns:
            The highest number reached in the sequence.
        """
        return max(self.sequence)

    def get_sequence(self) -> List[int]:
        """Get the complete sequence.

        Returns:
            List of all numbers in the sequence.
        """
        return self.sequence.copy()

    def analyze(self) -> Dict[str, Any]:
        """Perform comprehensive analysis of the sequence.

        Returns:
            Dictionary containing various statistics about the sequence.
        """
        return {
            "starting_number": self.starting_number,
            "length": self.get_length(),
            "max_value": self.get_max_value(),
            "sequence": self.get_sequence(),
            "even_count": sum(1 for x in self.sequence if x % 2 == 0),
            "odd_count": sum(1 for x in self.sequence if x % 2 == 1),
            "growth_factor": (
                self.get_max_value() / self.starting_number
                if self.starting_number > 0
                else 0
            ),
        }


def generate_sequence(starting_number: int) -> List[int]:
    """Generate a Collatz sequence for a given starting number.

    Args:
        starting_number: The positive integer to start with.

    Returns:
        List of integers representing the Collatz sequence.

    Raises:
        ValueError: If starting_number is not a positive integer.
    """
    collatz = CollatzSequence(starting_number)
    return collatz.get_sequence()


def analyze_sequence(starting_number: int) -> Dict[str, Any]:
    """Analyze a Collatz sequence for a given starting number.

    Args:
        starting_number: The positive integer to start with.

    Returns:
        Dictionary containing analysis results.

    Raises:
        ValueError: If starting_number is not a positive integer.
    """
    collatz = CollatzSequence(starting_number)
    return collatz.analyze()


def batch_analyze(start: int, end: int) -> List[Dict[str, Any]]:
    """Analyze multiple Collatz sequences in a range.

    Args:
        start: Starting number (inclusive).
        end: Ending number (inclusive).

    Returns:
        List of analysis dictionaries for each number in the range.
    """
    results = []

    for n in range(start, end + 1):
        try:
            analysis = analyze_sequence(n)
            results.append(analysis)
            logger.debug(f"Analyzed sequence for {n}: length={analysis['length']}")
        except Exception as e:
            logger.error(f"Error analyzing sequence for {n}: {e}")

    return results


def find_longest_sequence(start: int, end: int) -> Dict[str, Any]:
    """Find the number with the longest Collatz sequence in a range.

    Args:
        start: Starting number (inclusive).
        end: Ending number (inclusive).

    Returns:
        Dictionary containing the number and its analysis.
    """
    longest = None
    max_length = 0

    for n in range(start, end + 1):
        try:
            analysis = analyze_sequence(n)
            if analysis["length"] > max_length:
                max_length = analysis["length"]
                longest = analysis
        except Exception as e:
            logger.error(f"Error analyzing sequence for {n}: {e}")

    return longest or {}
