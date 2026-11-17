"""Модуль для бенчмарка сортировок."""

import time
from typing import Callable
from . import sorting, generators


def _measure_time(func: Callable, arr: list, repeats: int) -> float:
    """Замер среднего времени выполнения функции на копиях массива."""
    times = []
    for _ in range(repeats):
        arr_copy = arr.copy()
        start = time.perf_counter()
        func(arr_copy)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / repeats


def run_benchmark(repeats: int = 5) -> None:
    """Запускает бенчмарк и выводит Markdown-таблицу."""
    print("=== Результаты бенчмарка сортировок ===")
    print("|   Алгоритм   | Размер | Тип массива | Время (сек) |")
    print("|--------------|--------|-------------|-------------|")

    gens = [("random", generators.generate_random), 
            ("sorted", generators.generate_sorted),
            ("reversed", generators.generate_reversed), 
            ("nearly_sorted", generators.generate_nearly_sorted), 
            ("duplicates", generators.generate_duplicates)]
    for gen_name, gen_func in gens:
        for size in [100, 1000, 10000]:
            arr = gen_func(size, seed=42)
            b_time = _measure_time(sorting.bubble_sort, arr, repeats)
            print(f"| Bubble Sort | {size} | {gen_name} | {b_time:.5f} |")
            m_time = _measure_time(sorting.merge_sort, arr, repeats)
            print(f"| Merge  Sort | {size} | {gen_name} | {m_time:.5f} |")
    print("\n=== Большие размеры (только Merge Sort) ===")
    print("|   Алгоритм   | Размер | Тип массива | Время (сек) |")
    print("|--------------|--------|-------------|-------------|")
    for gen_name, gen_func in gens:
        for size in [100000, 1000000, 10000000]:
            arr = gen_func(size, seed=42)
            m_time = _measure_time(sorting.merge_sort, arr, repeats)
            print(f"| Merge  Sort | {size} | {gen_name} | {m_time:.5f} |")



