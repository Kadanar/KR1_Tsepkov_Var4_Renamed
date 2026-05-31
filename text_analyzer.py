"""
Zadanie 2A - Analiz teksta bez regulyarnyh vyrazhenij
Kontrolnaya rabota №1, Zadanie 2A
Versiya: 1.0
Avtor: Tsepkov Mikhail Dmitrievich (35355018), Variant 4
Data: 2026-05-31

Variant 4: Podschitat kolichestvo probelnyh simvolov v stroke.
"""


def is_whitespace(ch: str) -> bool:
    """
    Checks if character is whitespace.

    :param ch: input character
    :return: True if whitespace
    """
    return ch in (' ', '\t', '\n', '\r', '\f', '\v')


def count_whitespace(text: str) -> int:
    """
    Counts whitespace characters in string without regex.

    :param text: input string
    :return: count of whitespace characters
    """
    return sum(1 for ch in text if is_whitespace(ch))


def find_whitespace_chars(text: str) -> list:
    """
    Returns list of all whitespace characters found.

    :param text: input string
    :return: list of whitespace characters
    """
    return [repr(ch) for ch in text if is_whitespace(ch)]
