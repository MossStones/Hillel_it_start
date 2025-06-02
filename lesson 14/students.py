class Student:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Student) and str(self) == str(other)

    def __hash__(self) -> int:
        return hash(str(self))
