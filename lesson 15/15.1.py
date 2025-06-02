class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self.get_square() == other.get_square()

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_area: float = self.get_square() + other.get_square()
        new_height: float = new_area / self.width
        return Rectangle(self.width, new_height)

    def __mul__(self, n: float) -> 'Rectangle':
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area: float = self.get_square() * n
        new_height: float = new_area / self.width
        return Rectangle(self.width, new_height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width:.2f}, height={self.height:.2f}, area={self.get_square():.2f})"


if __name__ == "__main__":
    r1: Rectangle = Rectangle(2, 4)
    r2: Rectangle = Rectangle(3, 6)

    assert r1.get_square() == 8, 'Test1'
    assert r2.get_square() == 18, 'Test2'

    r3: Rectangle = r1 + r2
    assert abs(r3.get_square() - 26) < 1e-9, 'Test3'

    r4: Rectangle = r1 * 4
    assert abs(r4.get_square() - 32) < 1e-9, 'Test4'

    assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

    print("Всі тести пройшли успішно!")
