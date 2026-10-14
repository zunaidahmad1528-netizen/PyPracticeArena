"""Practice dictionary creation, access, updates, and iteration."""


def main() -> None:
    student = {
        "name": "Aisha Khan",
        "age": 20,
        "city": "Lucknow",
        "skills": ["Python", "SQL"],
        "scores": {"math": 80, "science": 88, "english": 70},
    }

    print("Name:", student["name"])
    print("Missing key:", student.get("email", "not provided"))
    student["age"] = 21
    student.setdefault("email", "aisha@example.com")
    student["skills"].append("Git")

    print("Keys:", list(student.keys()))
    print("Values:", list(student.values()))
    for key, value in student.items():
        print(f"{key}: {value}")

    scores = student["scores"]
    highest_subject = max(scores, key=scores.get)
    print(f"Highest score: {highest_subject} = {scores[highest_subject]}")


if __name__ == "__main__":
    main()

