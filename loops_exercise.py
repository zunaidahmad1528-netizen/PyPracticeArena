"""Loop practice and a small menu-driven scientific calculator."""

import math


def get_number(prompt):
    """Read a number and keep asking until the input is valid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def show_menu():
    print("\n--- Scientific Calculator ---")
    print("1. Add                 7. Square root")
    print("2. Subtract            8. Power")
    print("3. Multiply            9. Sine (degrees)")
    print("4. Divide             10. Cosine (degrees)")
    print("5. Modulus            11. Tangent (degrees)")
    print("6. Factorial          12. Logarithm")
    print("13. Constants (pi, e) 0. Exit")


def scientific_calculator():
    """Run the calculator until the user chooses Exit."""
    while True:
        show_menu()
        choice = input("Choose an operation: ").strip()

        try:
            if choice == "0":
                print("Calculator closed.")
                break
            if choice in {"1", "2", "3", "4", "5", "8"}:
                first = get_number("Enter first number: ")
                second = get_number("Enter second number: ")
                if choice == "1":
                    result = first + second
                elif choice == "2":
                    result = first - second
                elif choice == "3":
                    result = first * second
                elif choice == "4":
                    result = first / second
                elif choice == "5":
                    result = first % second
                else:
                    result = first**second
            elif choice == "6":
                number = get_number("Enter a non-negative whole number: ")
                if number < 0 or not number.is_integer():
                    raise ValueError("factorial needs a non-negative whole number")
                result = math.factorial(int(number))
            elif choice == "7":
                number = get_number("Enter a number: ")
                result = math.sqrt(number)
            elif choice in {"9", "10", "11"}:
                angle = get_number("Enter angle in degrees: ")
                radians = math.radians(angle)
                if choice == "9":
                    result = math.sin(radians)
                elif choice == "10":
                    result = math.cos(radians)
                else:
                    result = math.tan(radians)
            elif choice == "12":
                number = get_number("Enter a positive number: ")
                base = get_number("Enter log base (for example, 10): ")
                result = math.log(number, base)
            elif choice == "13":
                print(f"pi = {math.pi}")
                print(f"e  = {math.e}")
                continue
            else:
                print("Please choose a number from 0 to 13.")
                continue

            print(f"Result: {result:g}")
        except (ValueError, ZeroDivisionError):
            print("That calculation is not valid. Check the values and try again.")


if __name__ == "__main__":
    scientific_calculator()
