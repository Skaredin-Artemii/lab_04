"""Алгоритмы сортировки."""

from .errors import InvalidTypeError


def bubble_sort(arr: list) -> list:
    """Пузырьковая сортировка (квадратичная). Возвращает новый список."""
    if not isinstance(arr, list):
        raise InvalidTypeError("На вход должен подаваться список")
    result = arr.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def merge_sort(arr: list) -> list:
    """Сортировка слиянием (эффективная). Возвращает новый список."""
    if not isinstance(arr, list):
        raise InvalidTypeError("На вход должен подаваться список")
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    """Слияние двух отсортированных списков."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



            
            
