"""
Задание 2Б — Главный модуль
Контрольная работа №1, Вариант 4
Версия: 1.0
Автор: Цепков Михаил Дмитриевич (35355018)
Дата: 2026-05-31
"""

from regex_analyzer import (
    replace_spaces, is_guid, count_sentences,
    avg_sentence_length, avg_word_length,
    count_smileys, read_text_file, save_results, zip_file
)


def main():
    input_file = "input.txt"
    output_file = "output.txt"
    archive_file = "output.zip"

    text = read_text_file(input_file)

    lines = []
    lines.append("=" * 55)
    lines.append("  ЗАДАНИЕ 2Б — Анализ текста, Вариант 4")
    lines.append("=" * 55)

    char = input("Введите символ для замены пробелов: ").strip() or "_"
    replaced = replace_spaces(text, char)
    lines.append(f"\n1. Текст с заменёнными пробелами (символ '{char}'):")
    lines.append(replaced)

    lines.append(f"\n2. Проверка GUID:")
    guids = [
        "e02fd0e4-00fd-090A-ca30-0d00a0038ba0",
        "{e02fd0e4-00fd-090A-ca30-0d00a0038ba0}",
        "e02fd0e400fd090Aca300d00a0038ba0",
        "12345678-1234-1234-1234-123456789abc"
    ]
    for g in guids:
        lines.append(f"   {g} -> {is_guid(g)}")

    sentences = count_sentences(text)
    lines.append(f"\n3. Предложения: {sentences}")
    lines.append(f"\n4. Средняя длина предложения: {avg_sentence_length(text)}")
    lines.append(f"\n5. Средняя длина слова: {avg_word_length(text)}")

    smileys = count_smileys(text)
    lines.append(f"\n6. Количество смайликов: {smileys}")

    result = "\n".join(lines)
    print(result)

    save_results(output_file, result)
    info = zip_file(output_file, archive_file)
    print(f"\nАрхив создан: {info}")


if __name__ == "__main__":
    main()
