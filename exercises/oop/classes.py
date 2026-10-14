"""Practice classes, instance attributes, methods, and inheritance."""


class Student:
    def __init__(self, name: str, marks: list[int]) -> None:
        self.name = name
        self.marks = marks

    def average_mark(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)


class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def describe(self) -> str:
        return f"{self.name} earns {self.salary:,} per month"


class Developer(Employee):
    def __init__(self, name: str, salary: int, language: str) -> None:
        super().__init__(name, salary)
        self.language = language

    def describe(self) -> str:
        return f"{super().describe()} and writes {self.language}"


def main() -> None:
    student = Student("Aisha", [88, 94, 91])
    developer = Developer("Bilal", 50000, "Python")
    print(f"{student.name}'s average: {student.average_mark():.1f}")
    print(developer.describe())


if __name__ == "__main__":
    main()