"""Practice defining functions, parameters, and return values."""


def add(first: float, second: float) -> float:
    return first + second


def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("average requires at least one number")
    return sum(numbers) / len(numbers)


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def main() -> None:
    print("2 + 3 =", add(2, 3))
    print("Average:", average([2, 4, 6]))
    print(greet("Zunaid"))
    print(greet("Aisha", greeting="Welcome"))


if __name__ == "__main__":
    main()