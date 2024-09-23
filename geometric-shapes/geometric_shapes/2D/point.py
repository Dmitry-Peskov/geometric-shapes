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
