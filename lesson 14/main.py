from students import Student
from Group import Group

if __name__ == "__main__":
    g = Group("PD1")

    s1 = Student("female", 19, "Liza", "Taylor", "123")
    s2 = Student("male", 20, "Steve", "Jobs", "234")

    g.add_student(s1)
    g.add_student(s2)
    print(g)

    g.remove_student(s1)
    print(g)
