from math import gcd

class Fraction:
    def __init__(self, a: int, b: int) -> None:
        if b == 0:
            raise ValueError("Знаменник не може бути 0")
        self.a = a
        self.b = b
        self._simplify()

    def _simplify(self) -> None:

        common = gcd(self.a, self.b)
        self.a //= common
        self.b //= common

        if self.b < 0:
            self.a = -self.a
            self.b = -self.b

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return False
        return self.a == other.a and self.b == other.b

    def __gt__(self, other: 'Fraction') -> bool:
        return self.a * other.b > other.a * self.b

    def __lt__(self, other: 'Fraction') -> bool:
        return self.a * other.b < other.a * self.b

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"


if __name__ == "__main__":
    f_a: Fraction = Fraction(2, 3)
    f_b: Fraction = Fraction(3, 6)
    f_c: Fraction = f_b + f_a
    assert str(f_c) == 'Fraction: 7, 6'   # 2/3 + 1/2 = 7/6
    f_d: Fraction = f_b * f_a
    assert str(f_d) == 'Fraction: 1, 3'   # 1/2 * 2/3 = 1/3
    f_e: Fraction = f_a - f_b
    assert str(f_e) == 'Fraction: 1, 6'   # 2/3 - 1/2 = 1/6

    assert f_d < f_c
    assert f_d > f_e
    assert f_a != f_b
    f_1: Fraction = Fraction(2, 4)
    f_2: Fraction = Fraction(3, 6)
    assert f_1 == f_2

    print('OK')
