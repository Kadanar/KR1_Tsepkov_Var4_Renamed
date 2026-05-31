"""
Zadanie 2A - Glavnyj modul programmy
Kontrolnaya rabota №1, Variant 4
Versiya: 1.0
Avtor: Tsepkov Mikhail Dmitrievich (35355018)
Data: 2026-05-31
"""

import time
from text_analyzer import count_whitespace, find_whitespace_chars
from initializers import init_from_user, init_from_generator


def timer(func):
    """Decorator that prints execution time."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [timer] Vypolneno za {elapsed:.6f}s")
        return result
    return wrapper


@timer
def analyze_text(text: str) -> None:
    """
    Business function: analyzes text and prints results.

    :param text: input text
    """
    count = count_whitespace(text)
    chars = find_whitespace_chars(text)
    print(f"\n  Tekst           : {text}")
    print(f"  Probelnye simv. : {chars}")
    print(f"  Kolichestvo     : {count}")


def get_valid_choice(prompt: str, valid: set) -> str:
    """
    Requests input until valid choice entered.

    :param prompt: displayed message
    :param valid: set of valid answers
    :return: validated user input
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid:
            return choice
        print(f"  [!] Nekorektnyj vvod. Dopustimye: {valid}")


def choose_input_mode() -> str:
    """
    Asks user how to initialize input text.

    :return: text string ready for analysis
    """
    print("\n  Rezhim vvoda:")
    print("  [1] Vvesti svoj tekst")
    print("  [2] Ispolzovat generatsiyu")
    mode = get_valid_choice("  Vash vybor (1/2): ", {"1", "2"})

    if mode == "1":
        return init_from_user("  Vvedite tekst: ")
    else:
        text = init_from_generator()
        print(f"  Sgenerovano : {text}")
        return text


def main():
    """Main program loop with repeat support."""
    print("=" * 55)
    print("  ZADANIE 2A - Podschet probelnyh simvolov")
    print("  Variant 4 | Kontrolnaya rabota №1")
    print("=" * 55)

    while True:
        text = choose_input_mode()

        if not text:
            print("  [!] Pustoj vvod, povtorite.")
            continue

        analyze_text(text)

        again = get_valid_choice("\n  Zapustit snova? (y/n): ", {"y", "n"})
        if again == "n":
            print("\n  Do svidaniya!")
            break


if __name__ == "__main__":
    main()
