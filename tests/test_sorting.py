"""Тесты сортировок."""

import pytest
from algopack.sorting import bubble_sort, merge_sort
from algopack.errors import InvalidTypeError
from algopack.generators import generate_random

SORT_FUNCS = [bubble_sort, merge_sort]

def test_sorting_correctness():
    """Тест на корректную сортировку."""
    cases = [ ([], []), ([42], [42]), ([1, 2, 3], [1, 2, 3]),
    ([5, 1, 4, 2], [1, 2, 4, 5]), ([3, 1, 3, 2], [3, 1, 3, 2]), 
    ([-1, -5, 0, 2], [-5, -1, 0, 2]) ]
    for func in SORT_FUNCS:
        for arr, expected in cases:
            assert func(arr) == expected


def test_sorting_random():
    """Тест на случайных массивах."""
    arr = generate_random(100, seed=42)
    expected = sorted(arr)
    for func in SORT_FUNCS:
        assert func(arr) == expected


def test_sorting_does_not_mutate():
    """Тест на неизменность исходного массива."""
    for func in SORT_FUNCS:
        arr = [5, 2, 8, 1]
        original = arr.copy()
        func(arr)
        assert arr == original


def test_sorting_invalid_type():
    """Тест на неверный тип данных."""
    bad_inputs = ["строка", 123, None, (1, 2, 3), {"a": 1}]
    for func in SORT_FUNCS:
        for bad in bad_inputs:
            with pytest.raises(InvalidTypeError):
                func(bad)
        