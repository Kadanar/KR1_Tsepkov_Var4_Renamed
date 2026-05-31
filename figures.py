"""
Задание 4 — ООП: Геометрические фигуры
Контрольная работа №1, Вариант 4
Версия: 1.0
Автор: Цепков Михаил Дмитриевич (35355018)
Дата: 2026-05-31

Вариант 4: Построить треугольник по сторонам a, b и углу C между ними.
Площадь = 0.5 * a * b * sin(C)
"""

import math
from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    """Абстрактный класс, представляющий геометрическую фигуру."""

    @abstractmethod
    def area(self) -> float:
        """Вычислить и вернуть площадь фигуры."""
        pass


class FigureColor:
    """Хранит и предоставляет цвет геометрической фигуры."""

    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        """Получить цвет фигуры."""
        return self._color

    @color.setter
    def color(self, value: str):
        """Установить цвет фигуры."""
        if not value.strip():
            raise ValueError("Цвет не может быть пустым.")
        self._color = value


class Triangle(GeometricFigure):
    """
    Треугольник, заданный сторонами a, b и углом C между ними.
    Площадь = 0.5 * a * b * sin(C)
    """

    figure_name = "Треугольник"

    def __init__(self, a: float, b: float, angle_c: float, color: str):
        """
        Инициализация треугольника.

        :param a: длина первой стороны
        :param b: длина второй стороны
        :param angle_c: угол между сторонами в градусах
        :param color: цвет заливки
        """
        if a <= 0 or b <= 0:
            raise ValueError("Стороны должны быть положительными.")
        if not (0 < angle_c < 180):
            raise ValueError("Угол C должен быть от 0 до 180 градусов.")
        self._a = a
        self._b = b
        self._angle_c = angle_c
        self._color_obj = FigureColor(color)

    @classmethod
    def get_name(cls) -> str:
        """Вернуть название типа фигуры."""
        return cls.figure_name

    def area(self) -> float:
        """
        Вычислить площадь треугольника.
        Формула: 0.5 * a * b * sin(C)

        :return: площадь
        """
        return round(0.5 * self._a * self._b * math.sin(math.radians(self._angle_c)), 4)

    def __str__(self) -> str:
        """Вернуть строковое представление."""
        return (
            "Фигура    : {name}\n"
            "Сторона a : {a}\n"
            "Сторона b : {b}\n"
            "Угол C    : {c}°\n"
            "Цвет      : {color}\n"
            "Площадь   : {area}"
        ).format(
            name=self.get_name(),
            a=self._a, b=self._b, c=self._angle_c,
            color=self._color_obj.color, area=self.area()
        )

    def draw(self, label: str = "") -> None:
        """
        Рисует треугольник ASCII-артом.

        :param label: текстовая подпись
        """
        h = max(3, int(self._a / 2))
        print(f"\n  [{self._color_obj.color.upper()}] {self.get_name()}")
        for i in range(h):
            spaces = " " * (h - i - 1)
            stars = "*" * (2 * i + 1)
            print("  " + spaces + stars)
        print("  " + "*" * (2 * h - 1))
        if label:
            print(f"  {label}")
        print()
