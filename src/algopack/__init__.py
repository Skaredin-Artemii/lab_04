"""Пакет algopack - алгоритмический мини-пакет."""

from .benchmark import run_benchmark
from .datastructs import Stack
from .errors import (
    AlgoPackError,
    EmptyStructureError,
    InvalidInputError,
    InvalidTypeError,
)
from .generators import (
    generate_duplicates,
    generate_nearly_sorted,
    generate_random,
    generate_reversed,
    generate_sorted,
)
from .recurrence import fast_pow_iterative, fast_pow_recursive
from .sorting import bubble_sort, merge_sort

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