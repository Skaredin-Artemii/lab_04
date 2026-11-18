"""Генераторы тестовых наборов данных."""

import random

from .errors import InvalidInputError, InvalidTypeError


def generate_random(size: int, seed: int | None = None) -> list:
    """Генератор рандомного набора."""
    if not isinstance(size, int):
        raise InvalidTypeError("Размер должен быть целым числом")
    if size < 0:
        raise InvalidInputError("Размер не может быть отрицательным")
    rng = random.Random(seed)
    return [rng.randint (-1000, 1000) for _ in range(size)]


def generate_sorted(size: int, seed: int | None = None) -> list:
    """Генератор отсортированного набора."""
    if not isinstance(size, int):
        raise InvalidTypeError("Размер должен быть целым числом")
    if size < 0:
        raise InvalidInputError("Размер не может быть отрицательным")
    rng = random.Random(seed)
    arr = [rng.randint (-1000, 1000) for _ in range(size)]
    return sorted(arr)


def generate_reversed(size: int, seed: int | None = None) -> list:
    """Генератор отсортированного по убыванию набора."""
    if not isinstance(size, int):
        raise InvalidTypeError("Размер должен быть целым числом")
    if size < 0:
        raise InvalidInputError("Размер не может быть отрицательным")
    rng = random.Random(seed)
    arr = [rng.randint(-1000, 1000) for _ in range(size)]
    return sorted(arr, reverse=True)


def generate_nearly_sorted(size: int, seed: int | None = None) -> list:
    """Генератор почти отсортированного набора."""
    if not isinstance(size, int):
        raise InvalidTypeError("Размер должен быть целым числом")
    if size < 0:
        raise InvalidInputError("Размер не может быть отрицательным")
    rng = random.Random(seed)
    arr = sorted([rng.randint (-1000, 1000) for _ in range(size)])
    swaps = max(1, size // 10)
    for _ in range(swaps):
        i = rng.randint(0, size - 1)
        j = rng.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def generate_duplicates(size: int, seed: int | None = None) -> list:
    """Генератор набора с дубликатами."""
    if not isinstance(size, int):
        raise InvalidTypeError("Размер должен быть целым числом")
    if size < 0:
        raise InvalidInputError("Размер не может быть отрицательным")
    rng = random.Random(seed)
    if size < 5:
        return [22] * size
    return [rng.choice([0, 11, 55, 100]) for _ in range(size)]
