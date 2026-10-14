"""Practice unique values and common set operations."""


def main() -> None:
    python_students = {"Aisha", "Bilal", "Zunaid", "Aisha"}
    java_students = {"Bilal", "Noor", "Zunaid"}

    print("Unique Python students:", sorted(python_students))
    print("In either class:", sorted(python_students | java_students))
    print("In both classes:", sorted(python_students & java_students))
    print("Only Python:", sorted(python_students - java_students))
    print("In exactly one class:", sorted(python_students ^ java_students))
    print("Aisha is enrolled:", "Aisha" in python_students)
    print("Subset check:", {"Bilal"}.issubset(python_students))


if __name__ == "__main__":
    main()