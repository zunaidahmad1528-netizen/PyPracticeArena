"""Practice starting and joining threads."""

from threading import Thread


def print_numbers() -> None:
    for number in range(1, 6):
        print("Number:", number)


def print_letters() -> None:
    for letter in "ABCDE":
        print("Letter:", letter)


def main() -> None:
    number_thread = Thread(target=print_numbers)
    letter_thread = Thread(target=print_letters)
    number_thread.start()
    letter_thread.start()
    number_thread.join()
    letter_thread.join()
    print("Both threads finished")


if __name__ == "__main__":
    main()