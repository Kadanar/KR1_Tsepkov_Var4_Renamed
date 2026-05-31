"""
Задание 2А — Главный модуль программы
Контрольная работа №1, Вариант 4
Версия: 1.0
Автор: Цепков Михаил Дмитриевич (35355018)
Дата: 2026-05-31

Подсчитывает количество пробельных символов в строке.
Регулярные выражения не используются.
"""

import time
from text_analyzer import count_whitespace, find_whitespace_chars
from initializers import init_from_user, init_from_generator


def timer(func):
    """Декоратор, выводящий время выполнения функции."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [таймер] Выполнено за {elapsed:.6f}с")
        return result
    return wrapper


@timer
def analyze_text(text: str) -> None:
    """
    Бизнес-функция: анализирует текст и выводит результаты.

    :param text: входной текст для анализа
    """
    count = count_whitespace(text)
    chars = find_whitespace_chars(text)
    print(f"\n  Текст           : {text}")
    print(f"  Пробельные симв.: {chars}")
    print(f"  Количество      : {count}")


def get_valid_choice(prompt: str, valid: set) -> str:
    """
    Запрашивает ввод до тех пор, пока не будет введён допустимый вариант.

    :param prompt: отображаемое сообщение
    :param valid: множество допустимых ответов
    :return: проверенный ввод пользователя
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid:
            return choice
        print(f"  [!] Некорректный ввод. Допустимые значения: {valid}")


def choose_input_mode() -> str:
    """
    Спрашивает пользователя, как инициализировать входной текст.

    :return: строка текста, готовая к анализу
    """
    print("\n  Режим ввода:")
    print("  [1] Ввести свой текст")
    print("  [2] Использовать автоматически сгенерированный текст")
    mode = get_valid_choice("  Ваш выбор (1/2): ", {"1", "2"})
    if mode == "1":
        return init_from_user("  Введите текст: ")
    else:
        text = init_from_generator()
        print(f"  Сгенерировано : {text}")
        return text


def main():
    """Главный цикл программы с поддержкой повторного запуска."""
    print("=" * 55)
    print("  ЗАДАНИЕ 2А — Подсчёт пробельных символов")
    print("  Вариант 4 | Контрольная работа №1")
    print("=" * 55)

    while True:
        text = choose_input_mode()
        if not text:
            print("  [!] Пустой ввод, попробуйте снова.")
            continue
        analyze_text(text)
        again = get_valid_choice("\n  Запустить снова? (y/n): ", {"y", "n"})
        if again == "n":
            print("\n  До свидания!")
            break


if __name__ == "__main__":
    main()
