"""Practice lazy sequences with generator functions."""

from collections.abc import Iterator


def even_numbers(limit: int) -> Iterator[int]:
    for number in range(2, limit + 1, 2):
        yield number


def main() -> None:
    print(list(even_numbers(10)))


if __name__ == "__main__":
    main()