"""Исключения пакета algopack."""

class AlgoPackError(Exception):
    """Базовая ошибка пакета."""


class InvalidInputError(AlgoPackError):
    """Переданы недопустимые входные данные."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidTypeError(AlgoPackError):
    """Передан объект неподходящего типа."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class EmptyStructureError(AlgoPackError):
    """Попытка операции над пустой структурой данных."""
    def __init__(self, message: str = "Структура данных пуста") -> None:
        super().__init__(message)