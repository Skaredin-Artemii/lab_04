"""Структуры данных."""

from .errors import EmptyStructureError


class Stack:
    """Стек."""
    def __init__(self) -> None:
        """Инициализация."""
        self._data: list = []

    def push(self, item) -> None:
        """Добавление."""
        self._data.append(item)
        
    def pop(self):
        """Извлечение."""
        if not self._data:
            raise EmptyStructureError("Нельзя извлечь элемент из пустого стека")
        return self._data.pop()

    def peek(self):
        """просмотр."""
        if not self._data:
            raise EmptyStructureError("Нельзя посмотреть элемент пустого стека")
        return self._data[-1]

    def __len__(self) -> int:
        """Длина списка."""
        return len(self._data)

    def __bool__(self) -> bool:
        """Проверка на непустоту."""
        return bool(self._data)
            