"""Пакет algopack - алгоритмический мини-пакет."""

from .errors import (
    AlgoPackError, 
    EmptyStructureError, 
    InvalidTypeError, 
    InvalidInputError,
)
from .recurrence import fast_pow_recursive, fast_pow_iterative
from .sorting import bubble_sort, merge_sort
from .datastructs import Stack
from .generators import (
    generate_duplicates,
    generate_nearly_sorted, 
    generate_reversed, 
    generate_random, 
    generate_sorted,
)
from .benchmark import run_benchmark


__all__ = [
    "AlgoPackError",
    "EmptyStructureError",
    "InvalidTypeError",
    "InvalidInputError",
    "fast_pow_recursive",
    "fast_pow_iterative",
    "bubble_sort", 
    "merge_sort",
    "Stack",
    "generate_duplicates",
    "generate_nearly_sorted", 
    "generate_reversed", 
    "generate_random", 
    "generate_sorted",  
    "run_benchmark", 
]

__version__ = "0.1.0"