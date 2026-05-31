"""
Module for input initialization.
Provides generator and user input methods.
"""

import random


def init_from_user(prompt: str = "Vvedite tekst: ") -> str:
    """
    Gets text from user input.

    :param prompt: message for user
    :return: entered string
    """
    return input(prompt)


def init_from_generator(num_words: int = 8) -> str:
    """
    Generates random text for testing.

    :param num_words: number of words to generate
    :return: generated string
    """
    random.seed(42)
    words = [
        "hello", "world", "python", "programming",
        "test", "data", "code", "function",
        "variable", "class", "module", "import"
    ]
    chosen = random.choices(words, k=num_words)
    return " ".join(chosen)
