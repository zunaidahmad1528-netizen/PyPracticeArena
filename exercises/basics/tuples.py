"""Practice tuple creation, indexing, unpacking, and methods."""


def main() -> None:
    coordinates = (12, 8)
    print("Coordinates:", coordinates)
    print("X:", coordinates[0])

    scores = (88, 91, 76, 91)
    print("First two scores:", scores[:2])
    print("Number of 91s:", scores.count(91))
    print("Index of 76:", scores.index(76))

    x_position, y_position = coordinates
    print(f"Position: x={x_position}, y={y_position}")

    single_item = ("Python",)
    print("One-item tuple:", single_item)


if __name__ == "__main__":
    main()