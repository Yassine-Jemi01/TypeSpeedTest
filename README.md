# TypeSpeedTest

A simple cross-platform terminal typing speed test written in Python.

Type the given text as quickly and accurately as possible while your WPM, accuracy, and elapsed time update live in the terminal.

## Features

* Live WPM calculation
* Live typing accuracy
* Elapsed time
* Random typing prompts
* Speed status such as `Slow AF`, `Fast`, and `On fire`
* Backspace support
* ANSI terminal output
* Cross-platform design for Linux, macOS, and Windows

## Requirements

* Python 3

No external Python packages are required.

## Run

Clone the repository:

```bash
git clone https://github.com/Yassine-Jemi01/TypeSpeedTest.git
cd TypeSpeedTest
```

Run the program:

```bash
python3 -m src.main
```

On Windows, use:

```powershell
python -m src.main
```

## Project Structure

```text
TypeSpeedTest/
└── src/
    ├── main.py
    ├── input.py
    ├── ui.py
    └── words.py
```

### `main.py`

Controls the typing test, calculates WPM and accuracy, and handles the main program loop.

### `input.py`

Provides cross-platform keyboard input.

### `ui.py`

Handles terminal output and ANSI escape sequences.

### `words.py`

Contains the typing prompts used by the test.

## Speed Status

Your typing speed is classified as:

|   WPM | Status        |
| ----: | ------------- |
|  < 20 | Slow AF       |
| 20–39 | Slow          |
| 40–59 | Getting there |
| 60–79 | Fast          |
| 80–99 | On fire       |
|  100+ | Insane        |

## Status

TypeSpeedTest is currently under development.

More improvements and features will be added over time.

## License

This project is open source.
