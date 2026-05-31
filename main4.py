"""
Задание 4 — Тестирование классов ООП
Контрольная работа №1, Вариант 4
Версия: 1.0
Автор: Цепков Михаил Дмитриевич (35355018)
Дата: 2026-05-31
"""

from figures import Triangle


def get_float(prompt):
    """Запрашивает корректное положительное число."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  [!] Значение должно быть положительным.")
            else:
                return value
        except ValueError:
            print("  [!] Некорректный ввод, введите число.")


def get_angle(prompt):
    """Запрашивает угол от 0 до 180 градусов."""
    while True:
        try:
            value = float(input(prompt))
            if 0 < value < 180:
                return value
            print("  [!] Угол должен быть от 0 до 180 (не включая).")
        except ValueError:
            print("  [!] Некорректный ввод, введите число.")


def main():
    print("=" * 55)
    print("  ЗАДАНИЕ 4 — Геометрические фигуры (Треугольник)")
    print("  Вариант 4 | Контрольная работа №1")
    print("=" * 55)

    while True:
        print(f"\n  Фигура: {Triangle.get_name()}")
        a = get_float("  Введите сторону a: ")
        b = get_float("  Введите сторону b: ")
        c = get_angle("  Введите угол C между сторонами (градусы, 0-180): ")
        color = input("  Введите цвет фигуры: ").strip() or "синий"
        label = input("  Введите подпись фигуры: ").strip() or "Треугольник"

        triangle = Triangle(a, b, c, color)
        print("\n" + str(triangle))
        triangle.draw(label)

        again = input("\n  Запустить снова? (y/n): ").strip().lower()
        if again != "y":
            print("\n  До свидания!")
            break


if __name__ == "__main__":
    main()
