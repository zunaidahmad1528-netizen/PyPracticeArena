"""Practice rotating a square matrix clockwise."""


def rotate_clockwise(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square")
    return [list(row) for row in zip(*matrix[::-1])]


def main() -> None:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in rotate_clockwise(matrix):
        print(row)


if __name__ == "__main__":
    main()