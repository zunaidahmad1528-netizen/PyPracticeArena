# PyPracticeArena

> A practical Python learning workspace that grows from core syntax to small, useful programs.

[![Python CI](https://github.com/zunaidahmad1528-netizen/PyPracticeArena/actions/workflows/ci.yml/badge.svg)](https://github.com/zunaidahmad1528-netizen/PyPracticeArena/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)

PyPracticeArena is a hands-on collection of Python exercises and mini-projects. Each file focuses on a concept that can be opened, run, changed, and explored directly.

## Highlights

- **Scientific calculator** with safe expression parsing, constants, trigonometry, logarithms, powers, and factorials.
- **Sales analytics demo** with revenue summaries, product rankings, insights, and JSON export.
- Focused practice files for conditionals, loops, functions, collections, recursion, file I/O, and object-oriented programming.
- A lightweight GitHub Actions check that keeps the main runnable demo syntactically valid.

## Quick Start

```bash
git clone https://github.com/zunaidahmad1528-netizen/PyPracticeArena.git
cd PyPracticeArena
python3 python_power_demo.py
```

The default command opens the scientific calculator. Try expressions such as:

```text
sqrt(144)
sin(pi / 2)
2 ** 10
factorial(5)
```

Type `help` to see supported functions and `quit` to exit.

## Sales Demo

Run the included data analysis example with:

```bash
python3 python_power_demo.py --sales
```

This prints a sales dashboard and writes the generated report to `sales_report.json`.

## Learning Map

| Topic | Practice file |
| --- | --- |
| Variables and conditionals | `if_else_exercise.py` |
| Loops | `loops_exercise.py` |
| Lists, tuples, sets, and dictionaries | `lists_exerise.py`, `tuple_exercise.py`, `sets_exercise.py`, `dictionary_exercise.py` |
| Functions | `function_exercise.py` |
| Recursion | `recursion_exercise.py` |
| File input and output | `file_input_output_exercise.py` |
| Object-oriented programming | `oops_exercise.py` |
| Larger examples | `advanced.py`, `python_power_demo.py` |

## Docker

Run the calculator in a container:

```bash
docker build -t pypracticearena .
docker run -it --rm pypracticearena
```

## Development

The project uses only Python's standard library, so no dependency installation is required. To run the same syntax check used by CI:

```bash
python3 -m py_compile python_power_demo.py
```

Contributions are welcome. Keep exercises focused, use clear names, and include a short explanation when adding a new learning topic.

## License

This project is currently shared for learning and practice. Add a license before distributing it as a reusable package.
