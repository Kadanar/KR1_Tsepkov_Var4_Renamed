"""
Zadanie 2B - Modul analiza teksta s regulyarnymi vyrazheniyami
Kontrolnaya rabota №1, Variant 4
Versiya: 1.0
Avtor: Tsepkov Mikhail Dmitrievich (35355018)
Data: 2026-05-31
"""

import re
import zipfile
import os


def replace_spaces(text: str, char: str) -> str:
    """
    Replaces all spaces in text with given character.

    :param text: input text
    :param char: replacement character
    :return: text with spaces replaced
    """
    return re.sub(r' ', char, text)


def is_guid(s: str) -> bool:
    """
    Checks if string is a valid GUID with or without brackets.
    Format: 8-4-4-4-12 hex digits separated by dashes.

    :param s: input string
    :return: True if valid GUID
    """
    pattern = r'^\{?[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}\}?$'
    return bool(re.fullmatch(pattern, s.strip()))


def count_sentences(text: str) -> dict:
    """
    Counts sentences by type.

    :param text: input text
    :return: dict with sentence counts
    """
    declarative   = len(re.findall(r'[^.!?]*\.', text))
    interrogative = len(re.findall(r'[^.!?]*\?', text))
    exclamatory   = len(re.findall(r'[^.!?]*!', text))
    total = declarative + interrogative + exclamatory
    return {"total": total, "declarative": declarative,
            "interrogative": interrogative, "exclamatory": exclamatory}


def avg_sentence_length(text: str) -> float:
    """
    Calculates average sentence length in characters.

    :param text: input text
    :return: average length rounded to 2 decimals
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return 0.0
    lengths = [len(re.sub(r'[^A-Za-z]', '', s)) for s in sentences]
    return round(sum(lengths) / len(lengths), 2)


def avg_word_length(text: str) -> float:
    """
    Calculates average word length in characters.

    :param text: input text
    :return: average length rounded to 2 decimals
    """
    words = re.findall(r'\b[A-Za-z]+\b', text)
    if not words:
        return 0.0
    return round(sum(len(w) for w in words) / len(words), 2)


def count_smileys(text: str) -> int:
    """
    Counts smileys matching pattern.

    :param text: input text
    :return: count of smileys
    """
    return len(re.findall(r'[:;]-*[()\[\]]+', text))


def read_text_file(filepath: str) -> str:
    """
    Reads text from file.

    :param filepath: path to input file
    :return: file contents as string
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def save_results(filepath: str, content: str) -> None:
    """
    Saves results to text file.

    :param filepath: path to output file
    :param content: text to write
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def zip_file(source: str, archive: str) -> dict:
    """
    Archives file using zipfile module.

    :param source: path to file for archiving
    :param archive: path for output ZIP archive
    :return: dict with archive file info
    """
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(source, os.path.basename(source))
    info = {}
    with zipfile.ZipFile(archive, 'r') as zf:
        for zi in zf.infolist():
            info = {"filename": zi.filename, "file_size": zi.file_size,
                    "compress_size": zi.compress_size, "date_time": zi.date_time}
    return info
