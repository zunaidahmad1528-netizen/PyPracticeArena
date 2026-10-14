from pathlib import Path


def main():
	repository_root = Path(__file__).resolve().parents[2]
	file_path = repository_root / "data" / "output" / "file_io_example.txt"
	file_path.parent.mkdir(parents=True, exist_ok=True)
	sample_text = "Hello, Python file I/O!\nThis file was created by the exercise.\n"

	with file_path.open("w", encoding="utf-8") as file:
		characters_written = file.write(sample_text)

	print(f"Wrote {characters_written} characters to {file_path}")

	with file_path.open("r", encoding="utf-8") as file:
		contents = file.read()

	print("Full file contents:")
	print(contents)
	print(f"Data type: {type(contents).__name__}")

	with file_path.open("r", encoding="utf-8") as file:
		first_line = file.readline().strip()

	print(f"First line: {first_line}")


if __name__ == "__main__":
	main()