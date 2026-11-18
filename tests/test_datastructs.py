"""Тестирование реализованной структуры данных (Stack)."""

import pytest

from algopack.datastructs import Stack
from algopack.errors import EmptyStructureError


def test_stack_new_is_empty():
    """Тест на создание и пустоту."""
    st = Stack()
    assert len(st) == 0
    assert not st


def test_stack_push_increases_length():
    """Тест на добавление и размер."""
    st = Stack()
    st.push(10)
    assert len(st) == 1
    assert st
    st.push(20)
    assert len(st) == 2


def test_stack_pop():
    "Тест на извлечение (pop)."
    st = Stack()
    st.push("Первый")
    st.push("Второй")
    val = st.pop()
    assert val == "Второй"
    assert len(st) == 1
    val = st.pop()
    assert val == "Первый"
    assert not st


def test_stack_peek_returns_top_without_removing():
    """Тест на просмотр (peek)."""
    st = Stack()
    st.push("A")
    st.push("B")
    val = st.peek()
    assert val == "B"
    assert len(st) == 2


def test_stack_pop_empty_raises():
    """Тест на ошибку при pop из пустого стека."""
    st = Stack()
    with pytest.raises(EmptyStructureError):
        st.pop()


def test_stack_peek_empty_raises():
    """Тест на ошибку при peek из пустого стека."""
    st = Stack()
    with pytest.raises(EmptyStructureError):
        st.peek()