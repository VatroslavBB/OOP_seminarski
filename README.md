# Boolean Function Minimizer (OOP Seminar Project)

Desktop GUI application for entering, validating, analyzing, and minimizing Boolean expressions.

The app is built with Python and Tkinter, and supports:
- manual expression input,
- loading expressions from a text file,
- truth table generation,
- Boolean function minimization (Quine-McCluskey-style implementation),
- saving the current function to a file.

## Features

- Input a Boolean function with 1 to 5 variables.
- Validate variable set and expression syntax.
- Generate a truth table for the current function.
- Calculate a minimized form of the function.
- Save or Save As to `.txt` files.

## Tech Stack

- Python 3
- Tkinter (minimalist Python GUI library)

## Project Structure

```
OOP_seminarski/
	README.md
	grafika/
	src/
		main.py
		AppClass.py
		BooleanFunctionClass.py
	testData/
		FirstInput.txt
		SecondInput.txt
		ThirdInput.txt
		drugisave.txt
```

## How to Run

1. Open a terminal in the project root.
2. Run:

```bash
python src/main.py
```

If your system uses `py` launcher on Windows, you can also run:

```bash
py src/main.py
```

## Input Rules

### Variables

- Allowed: letters only (`A-Z`, `a-z`)
- Number of variables: minimum 1, maximum 5
- Example variable lines:
	- `x y Z w`
	- `ab` (interpreted as variables `a` and `b`)

Spaces in variable input are removed internally, so `x y z` becomes `xyz`.

### Expression Syntax

- Negation: `!`
- AND: `&`
- OR: `|`
- Parentheses: `(` and `)`

Examples:
- `Z&w|(x&Z)`
- `c|!(d|A&B)`
- `p&q|!(r|s|!(t&r))`

### Expression Notes

- Use explicit operators between variables (`a&b`, not `ab`).
- Parentheses must be balanced.
- Variables used in expression must exist in the variable list.

## File Input / Output Format

When loading from a file, the app expects:
- line 1: variable list
- line 2: Boolean expression

Example:

```txt
x y Z w
Z&w|(x&Z)
```

When saving, the app writes the same two-line format.

## UI Workflow

1. Start app.
2. Select input mode:
	 - Manual input
	 - File input
3. Confirm selection.
4. Use actions:
	 - Enter function
	 - Minimize
	 - Truth table
	 - Save / Save As
	 - Back

## Core Implementation Overview

- `src/main.py`: Application entry point, Tkinter root setup.
- `src/AppClass.py`: GUI logic, event handling, file dialogs, and app flow.
- `src/BooleanFunctionClass.py`:
	- syntax and variable validation, parser,
	- expression tree construction and evaluation,
	- truth table creation,
	- minimization logic.


## Author

- Vatroslav Bundara
- OOP seminar project
