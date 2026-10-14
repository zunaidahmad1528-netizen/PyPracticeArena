"""Practice conditional statements with small, focused examples."""


def describe_number(number: int) -> str:
	if number > 0:
		return "positive"
	if number < 0:
		return "negative"
	return "zero"


def grade_for_score(score: int) -> str:
	if not 0 <= score <= 100:
		return "Invalid score"
	if score >= 90:
		return "A"
	if score >= 80:
		return "B"
	if score >= 70:
		return "C"
	if score >= 60:
		return "D"
	return "F"


def main() -> None:
	for number in (-5, 0, 8):
		print(f"{number} is {describe_number(number)}")

	for score in (95, 82, 73, 64, 42, 120):
		print(f"Score {score}: {grade_for_score(score)}")


if __name__ == "__main__":
	main()
