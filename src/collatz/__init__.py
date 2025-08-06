"""Collatz Data Science Package.

A comprehensive package for analyzing Collatz sequences and related mathematical patterns.
"""

__version__ = "0.1.0"
__author__ = "Collatz Data Science Team"

from .core import CollatzSequence, analyze_sequence, generate_sequence

__all__ = [
    "CollatzSequence",
    "analyze_sequence", 
    "generate_sequence",
]