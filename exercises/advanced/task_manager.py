"""Practice lists and input handling in a small command-line task manager."""


def main() -> None:
    tasks: list[str] = []
    while True:
        print("\n1. Add  2. View  3. Delete  4. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            task = input("Task: ").strip()
            if task:
                tasks.append(task)
        elif choice == "2":
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            if not tasks:
                print("No tasks")
        elif choice == "3":
            try:
                index = int(input("Task number: ")) - 1
                removed = tasks.pop(index)
            except (ValueError, IndexError):
                print("Invalid task number")
            else:
                print("Removed:", removed)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()