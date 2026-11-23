"""Демонстрация и запуск бенчмарка пакета algorithmic_package."""

from .benchmark import run_benchmark
from .datastructs import Stack
from .errors import (
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


def main() -> None:
    print("=== 1. Быстрая степень ===")
    print(f"5^15 (итеративно) = {fast_pow_iterative(5, 15)}")
    print(f"5^15 (рекурсивно) = {fast_pow_recursive(5, 15)}")
    print(f"5^0 (итеративно) = {fast_pow_iterative(5, 0)}")
    print(f"5^0 (рекурсивно) = {fast_pow_recursive(5, 0)}")
    try:
        fast_pow_iterative(2, -5)
    except InvalidInputError as e:
        print(f" Поймана ошибка: {e}")
    print("\n")

    print("=== 2. Сортировки ===")
    arr = [5, 2, 8, 1, -3, 0, 5]
    print(f"Исходный массив: {arr}")
    print(f"Bubble Sort: {bubble_sort(arr)}")
    print(f"Merge Sort: {merge_sort(arr)}")
    print(f"Исходный массив не изменился: {arr}")
    try:
        bubble_sort("это строка, а не список")
    except InvalidTypeError as e:
        print(f" Поймана ошибка: {e}")
    print("\n")

    print("=== 3. Структура данных (Stack) ===")
    st = Stack()
    print(f"Стек пуст? {not bool(st)}")
    st.push("Первый")
    st.push("Второй")
    st.push("Третий")
    print(f"Размер стека: {len(st)}")
    print(f"Верхний элемент: {st.peek()}")
    print(f"Извлекли: {st.pop()}")
    print(f"Размер после извлечения: {len(st)}")
    try:
        empty_st = Stack()
        empty_st.pop()
    except EmptyStructureError as e:
        print(f" Поймана ошибка: {e}")
    print("\n")

    print("=== 4. Генераторы наборов ===")
    print(f"Случайный: {generate_random(10, seed=42)}")
    print(f"Отсортированный: {generate_sorted(10, seed=42)}")
    print(f"Обратный: {generate_reversed(10, seed=42)}")
    print(f"Почти отсортированный: {generate_nearly_sorted(10, seed=42)}")
    print(f"С дубликатами: {generate_duplicates(10, seed=42)}")
    g1 = generate_random(10, seed=100)
    g2 = generate_random(10, seed=100)
    print(f"\nПроверка seed=100: {g1} == {g2} -> {g1 == g2}")
    print("\n")

    print("=== 5. Бенчмарк ===")
    run_benchmark(repeats=5)


if __name__ == "__main__":
    main()

