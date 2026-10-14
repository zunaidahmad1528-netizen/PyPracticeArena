"""Practice recursive functions with clear base cases."""


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("factorial is undefined for negative numbers")
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def fibonacci(index: int) -> int:
    if index < 0:
        raise ValueError("index must not be negative")
    if index < 2:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)


def greatest_common_divisor(first: int, second: int) -> int:
    if second == 0:
        return abs(first)
    return greatest_common_divisor(second, first % second)


def main() -> None:
    print("5! =", factorial(5))
    print("Fibonacci at index 7 =", fibonacci(7))
    print("GCD of 48 and 18 =", greatest_common_divisor(48, 18))


if __name__ == "__main__":
    main()