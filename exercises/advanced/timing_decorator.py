"""Practice decorators by timing a function call."""

from functools import wraps
from time import perf_counter
from typing import Callable, TypeVar


Result = TypeVar("Result")


def timed(function: Callable[..., Result]) -> Callable[..., Result]:
    @wraps(function)
    def wrapper(*args: object, **kwargs: object) -> Result:
        started = perf_counter()
        result = function(*args, **kwargs)
        elapsed = perf_counter() - started
        print(f"{function.__name__} took {elapsed:.6f} seconds")
        return result

    return wrapper


@timed
def sum_squares(limit: int) -> int:
    return sum(number * number for number in range(limit))


def main() -> None:
    print("Result:", sum_squares(100_000))


if __name__ == "__main__":
    main()