from __future__ import annotations
from typing import TypeAlias

Number: TypeAlias = int | float


class Point:

    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Точка({self.x}, {self.y})"

    def __eq__(self, other: Point) -> bool:
        if not isinstance(other, Point):
            raise TypeError(f"Не корректный тип {type(other)}. Операнд справа должен иметь тип Point")
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Point) -> bool:
        if not isinstance(other, Point):
            raise TypeError(f"Не корректный тип {type(other)}. Операнд справа должен иметь тип Point")
        return self.x != other.x or self.y != other.y

    def distance_to(self, point: Point) -> float:
        """
        Вычислить расстояние от текущей точки до любой другой на плоскости.


        :param point: произвольная точка на плоскости
        :return: расстояние между точками
        """
        if not isinstance(point, Point):
            raise TypeError(f"Не корректный тип {type(point)}. Для вычисления расстояния между точками, аргумент должен иметь тип Point")
        return ((self.x - point.x)**2 - (self.y - point.y)**2) ** 0.5
