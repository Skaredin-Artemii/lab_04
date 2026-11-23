"""Тесты для генераторов наборов данных."""

import pytest

from algorithmic_package.errors import InvalidInputError, InvalidTypeError
from algorithmic_package.generators import (
    generate_duplicates,
    generate_nearly_sorted,
    generate_random,
    generate_reversed,
    generate_sorted,
)

ALL_GENS = [
    generate_random,
    generate_sorted,
    generate_reversed,
    generate_nearly_sorted,
    generate_duplicates,
]


def test_generators_size():
    """Тест на создание генераторами набора нужного размера."""
    for gen in ALL_GENS:
        arr = gen(50, seed=1)
        assert len(arr) == 50


def test_generators_seed_reproducibility():
    """Тест на создание одинаковых наборов с одинаковым seed."""
    for gen in ALL_GENS:
        arr1 = gen(20, seed=42)
        arr2 = gen(20, seed=42)
        assert arr1 == arr2


def test_generators_different_seeds():
    """Тест на создание разных наборов с разными seed."""
    for gen in ALL_GENS:
        arr1 = gen(100, seed=1)
        arr2 = gen(100, seed=2)
        assert arr1 != arr2


def test_generate_sorted_is_sorted():
    """Тест на генерирование сортированного списка."""
    arr = generate_sorted(100, seed=1)
    assert arr == sorted(arr)


def test_generate_reversed_is_reversed():
    """Тест на генерирование набора, отсортированного в обратном порядке."""
    arr = generate_reversed(100, seed=1)
    assert arr == sorted(arr, reverse=True)


def test_generate_duplicates_has_duplicates():
    """Тест на генерацию дубликатов в наборе."""
    arr = generate_duplicates(100, seed=1)
    assert len(set(arr)) < len(arr)


def test_generate_duplicates_small_size():
    """Тест на генерацию дубликатов в наборе при маленьких размерах."""
    arr = generate_duplicates(3, seed=1)
    assert len(arr) == 3
    assert len(set(arr)) == 1


def test_generators_negative_size_raises():
    """Тест на отрицательный размер."""
    for gen in ALL_GENS:
        with pytest.raises(InvalidInputError):
            gen(-1, seed=1)


def test_generators_invalid_type_raises():
    """Тест на несоотствие типа размера генерируемого набора."""
    for gen in ALL_GENS:
        with pytest.raises(InvalidTypeError):
            gen("строка", seed=1)