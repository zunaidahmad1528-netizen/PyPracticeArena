# PyPracticeArena

A practical Python learning workspace with small, runnable examples grouped by topic.

## Quick Start

Run the scientific calculator:

```bash
python3 exercises/advanced/scientific_calculator.py
```

Try `sqrt(144)`, `sin(pi / 2)`, or `2 ** 10`. Type `help` for supported operations and `quit` to exit.

Run the sales analysis demo:

```bash
python3 exercises/data_analysis/sales_analysis.py
```

The report is written to `data/output/sales_report.json`.

## Learning Map

| Topic | Files |
| --- | --- |
| Conditions, loops, functions | `exercises/basics/conditionals.py`, `loops.py`, `functions.py` |
| Lists, tuples, sets, dictionaries | `exercises/basics/lists.py`, `tuples.py`, `sets.py`, `dictionaries.py` |
| Recursion | `exercises/basics/recursion.py` |
| Object-oriented programming | `exercises/oop/classes.py` |
| File input and output | `exercises/file_io/text_files.py` |
| Advanced math and programming | `exercises/advanced/` |
| Data analysis | `exercises/data_analysis/` |
| Data cleaning | `data_cleaning/` |
| Python questions and answers | `questions/` |

Run an individual exercise from the repository root, for example:

```bash
python3 exercises/basics/loops.py
```

## Data Cleaning

The standard-library example needs no installation:

```bash
python3 data_cleaning/standard_library.py
```

Pandas and Excel examples use optional dependencies:

```bash
python3 -m pip install -r requirements.txt
python3 data_cleaning/pandas_example.py
python3 data_cleaning/file_cleaner.py data/examples/cleaned_customers.xlsx
```

Sample datasets are kept in `data/examples/`. Generated files go to `data/output/`.

## Docker

```bash
docker build -t pypracticearena .
docker run -it --rm pypracticearena
```

## Development

Compile all maintained Python examples with:

```bash
python3 -m compileall -q exercises data_cleaning questions
```

GitHub Actions runs this syntax check on Python 3.10, 3.11, and 3.12.