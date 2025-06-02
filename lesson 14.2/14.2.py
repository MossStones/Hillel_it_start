class TooManyStudentsError(Exception):
    """Виняток для ситуації, коли в групі вже є 10 студентів."""
    pass
class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{super().__str__()} — Record book: {self.record_book}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self) -> int:
        return hash(self.record_book)


class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise TooManyStudentsError(f"Група {self.number} вже має 10 студентів.")
        self.group.add(student)

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self) -> str:
        all_students = "\n".join(str(s) for s in self.group)
        return f"Number: {self.number}\n{all_students}"
gr = Group('PD1')

for i in range(1, 11):
    st = Student('Male', 20 + i, f'Name{i}', f'LastName{i}', f'RB{i:03}')
    gr.add_student(st)

try:
    gr.add_student(Student('Female', 22, 'Anna', 'Extra', 'RB011'))
except TooManyStudentsError as e:
    print(f"[Помилка]: {e}")

print(gr)
