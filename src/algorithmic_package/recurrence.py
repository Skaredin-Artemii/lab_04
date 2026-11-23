"""Рекуррентная задача: быстрая степень."""

from .errors import InvalidInputError


def fast_pow_iterative(base: float, exponent: int) -> float:
    """Итеративное бинарное возведение в степень."""
    if exponent < 0:
        raise InvalidInputError("Отрицательная степень не поддерживается")
    result = 1.0
    current_base = base
    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_base
        current_base *= current_base
        exponent //= 2
    return result


def fast_pow_recursive(base: float, exponent: int) -> float:
    """Рекурсивное возведение в степень."""
    if exponent < 0:
        raise InvalidInputError("Отрицательная степень не поддерживается")
    if exponent == 0:
        return 1.0
    if exponent == 1:
        return base
    if exponent % 2 == 0:
        half = fast_pow_recursive(base, exponent // 2)
        return half * half
    else:
        return base * fast_pow_recursive(base, exponent - 1)
