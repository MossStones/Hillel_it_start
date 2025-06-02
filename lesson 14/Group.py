from students import Student
from typing import Set

class Group:
    def __init__(self, name: str) -> None:
        self.name = name
        self.group: Set[Student] = set()

    def add_student(self, student: Student) -> None:
        self.group.add(student)

    def remove_student(self, student: Student) -> None:
        self.group.discard(student)

    def __str__(self) -> str:
        return f"Group {self.name}:\n" + "\n".join(str(student) for student in self.group)
