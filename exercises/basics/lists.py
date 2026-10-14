"""Practice common list operations."""


def main() -> None:
    numbers = [2, 5, 2, 4, 1]
    numbers.append(6)
    numbers.insert(0, 9)
    numbers.remove(2)
    print("Updated:", numbers)

    numbers.sort()
    print("Sorted:", numbers)
    print("First three:", numbers[:3])

    values = [1, 2, 3, 2, 1]
    print("List palindrome:", values == values[::-1])


if __name__ == "__main__":
    main()
