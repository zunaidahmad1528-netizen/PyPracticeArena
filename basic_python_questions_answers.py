"""Basic Python questions and answers for practice and interview prep."""


QUESTIONS = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted, and beginner-friendly programming language used for web development, automation, data analysis, AI, scripting, and more.",
    },
    {
        "question": "What are variables in Python?",
        "answer": "Variables are containers used to store data values. Example: age = 25; name = 'Aman'.",
        "example": "age = 25\nname = 'Aman'\nprint(age, name)",
    },
    {
        "question": "What is the difference between a list and a tuple?",
        "answer": "A list is mutable (can be changed), while a tuple is immutable (cannot be changed after creation).",
        "example": "numbers = [1, 2, 3]  # list\nnums = (1, 2, 3)     # tuple\nnumbers.append(4)\nprint(numbers)",
    },
    {
        "question": "What is a dictionary in Python?",
        "answer": "A dictionary stores data in key-value pairs. Keys are unique and used for quick access.",
        "example": "student = {'name': 'Rahul', 'age': 21}\nprint(student['name'])",
    },
    {
        "question": "What is a function in Python?",
        "answer": "A function is a block of reusable code that performs a specific task.",
        "example": "def add(a, b):\n    return a + b\n\nprint(add(3, 5))",
    },
    {
        "question": "What is an if-else statement?",
        "answer": "It is used to make decisions in a program. The code executes a conditionally selected block.",
        "example": "num = 10\nif num > 0:\n    print('Positive')\nelse:\n    print('Not positive')",
    },
    {
        "question": "What is a loop?",
        "answer": "A loop repeats a block of code multiple times until a condition is met.",
        "example": "for i in range(1, 4):\n    print(i)",
    },
    {
        "question": "What is the difference between append() and extend()?",
        "answer": "append() adds one element to the end of a list, while extend() adds multiple elements from another iterable.",
        "example": "my_list = [1, 2]\nmy_list.append(3)\nmy_list.extend([4, 5])\nprint(my_list)",
    },
    {
        "question": "What is slicing in Python?",
        "answer": "Slicing is used to access a part of a string, list, or tuple using indexes.",
        "example": "word = 'Python'\nprint(word[0:3])  # Pyt",
    },
    {
        "question": "What is the use of a for loop and while loop?",
        "answer": "A for loop is used when the number of iterations is known, while a while loop runs until a condition becomes false.",
        "example": "for i in range(3):\n    print(i)\n\ncount = 0\nwhile count < 3:\n    print(count)\n    count += 1",
    },
]


def print_question_and_answer(index, item):
    print(f"Q{index}: {item['question']}")
    print(f"A{index}: {item['answer']}")
    if "example" in item:
        print("Example:")
        print(item["example"])
    print("-" * 70)
    print()


def main():
    print("Python Basic Questions and Answers")
    print("=" * 70)
    print()

    for index, item in enumerate(QUESTIONS, start=1):
        print_question_and_answer(index, item)


if __name__ == "__main__":
    main()
