"""Practice validating text with regular expressions."""

import re


def is_strong_password(password: str) -> bool:
    return bool(
        len(password) >= 8
        and re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[0-9]", password)
    )


def main() -> None:
    for candidate in ("Python123", "python", "SecurePass9"):
        status = "strong" if is_strong_password(candidate) else "weak"
        print(f"{candidate}: {status}")


if __name__ == "__main__":
    main()