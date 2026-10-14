"""Practice for loops, while loops, and loop control."""


def main() -> None:
    print("Count with for:")
    for number in range(1, 6):
        print(number)

    print("Even numbers:")
    for number in range(2, 11, 2):
        print(number)

    print("Count down with while:")
    remaining = 3
    while remaining > 0:
        print(remaining)
        remaining -= 1
    print("Done")


if __name__ == "__main__":
    main()