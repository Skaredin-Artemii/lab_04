"""Тесты рекуррентной задачи."""

import pytest

from algopack.errors import InvalidInputError
from algopack.recurrence import fast_pow_iterative, fast_pow_recursive

POW_FUNCS = [fast_pow_recursive, fast_pow_iterative]

def test_pow_correctness():
    """Тест на корректность вычислений."""
    for func in POW_FUNCS:
        assert func(2, 10) == 1024
        assert func(5, 0) == 1
        assert func(1, 100) == 1


def test_pow_zero_base():
    """Тест на возведение нуля в степень."""
    for func in POW_FUNCS:
        assert func(0, 1000) == 0
        assert func(0, 1) == 0


def test_pow_exponent_one():
    """Тест на возведение в первую степень."""
    for func in POW_FUNCS:
        assert func(42, 1) == 42
        assert func(-10, 1) == -10

def test_pow_negative_base():
    """Тест на возведение отрицательного числа в четную и нечетную степень."""
    for func in POW_FUNCS:
        assert func(-2, 3) == -8
        assert func(-2, 10) == 1024


def test_pow_float_base():
    """Тест на дробное основание."""
    for func in POW_FUNCS:
        assert func(2.5, 2) == pytest.approx(6.25)
        assert func(5.5, 4) == pytest.approx(915.0625)
        assert func(0.025, 2) == pytest.approx(0.000625)


def test_pow_large_exponent():
    """Тест на корректность возведения в большую степень."""
    for func in POW_FUNCS:
        assert func(2, 50) == 1125899906842624
        assert func(3, 31) == 617673396283947


def test_pow_zero_to_zero():
    """Проверка 0^0 (по соглашению Python 0^0 = 1)."""
    for func in POW_FUNCS:
        assert func(0, 0) == 1


def test_pow_negative_exponent():
    """Тест на отрицательную степень (должен вызывать InvalidInputError)."""
    for func in POW_FUNCS:
        with pytest.raises(InvalidInputError):
            func(2, -5)
        with pytest.raises(InvalidInputError):
            func(10, -1)
        