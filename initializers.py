"""
Модуль инициализации входных последовательностей.
Предоставляет инициализацию через генератор и через ввод пользователя.
"""

import random


def init_from_user(prompt: str = "Введите текст: ") -> str:
    """
    Инициализация текста из ввода пользователя с клавиатуры.

    :param prompt: сообщение для пользователя
    :return: введённая строка
    """
    return input(prompt)


def init_from_generator(num_words: int = 8) -> str:
    """
    Генерирует случайный текст для тестирования.

    :param num_words: количество слов для генерации
    :return: сгенерированная строка
    """
    random.seed(42)
    words = [
        "hello", "world", "python", "programming",
        "test", "data", "code", "function",
        "variable", "class", "module", "import"
    ]
    chosen = random.choices(words, k=num_words)
    return " ".join(chosen)
