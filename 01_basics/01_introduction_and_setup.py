"""Introduction to Python and a quick check of your development setup.

Run this file from the repository root with:
    python3 01_basics/01_introduction_and_setup.py
"""

import sys


def main():
    """Print a greeting and show which Python installation is running."""
    print("Welcome to Python!")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Python executable: {sys.executable}")

    if sys.version_info >= (3, 10):
        print("Your Python version meets this project's requirement (3.10+).")
    else:
        print("Please install Python 3.10 or newer to follow this project.")

    print("\nSetup check complete. You are ready to start practicing.")


if __name__ == "__main__":
    main()
