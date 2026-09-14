import time

from .input import read_key
from .ui import clear_screen, show_header, show_text, show_stats
from .words import get_text


def calculate_accuracy(text, typed):
    if not typed:
        return 0

    correct = sum(
        expected == actual
        for expected, actual in zip(text, typed)
    )

    return correct / len(typed) * 100


def calculate_wpm(typed, elapsed):
    if elapsed <= 0:
        return 0

    return (len(typed) / 5) / (elapsed / 60)


def speed_status(wpm):
    if wpm < 20:
        return "Slow AF"
    if wpm < 40:
        return "Slow"
    if wpm < 60:
        return "Getting there"
    if wpm < 80:
        return "Fast"
    if wpm < 100:
        return "On fire"

    return "Insane"


def render(text, typed, start_time):
    elapsed = time.perf_counter() - start_time
    wpm = calculate_wpm(typed, elapsed)
    accuracy = calculate_accuracy(text, typed)

    clear_screen()
    show_header()
    show_text(text)
    show_stats(wpm, accuracy, elapsed)

    print(f"Status: {speed_status(wpm)}")
    print()
    print(f"> {typed}", end="", flush=True)


def wait_for_start():
    print("Press ENTER to start.")
    print("Press ESC to quit.")

    while True:
        key = read_key()

        if key == "ENTER":
            return True

        if key in ("ESC", "CTRL_C"):
            return False


def run_test(text):
    typed = ""
    start_time = time.perf_counter()

    render(text, typed, start_time)

    while len(typed) < len(text):
        key = read_key()

        if key in ("ESC", "CTRL_C"):
            return None

        if key == "BACKSPACE":
            typed = typed[:-1]
        elif len(key) == 1:
            typed += key

        render(text, typed, start_time)

    elapsed = time.perf_counter() - start_time

    return {
        "typed": typed,
        "elapsed": elapsed,
        "wpm": calculate_wpm(typed, elapsed),
        "accuracy": calculate_accuracy(text, typed),
    }


def show_results(text, results):
    clear_screen()
    show_header()
    show_text(text)

    print(f"WPM: {results['wpm']:.1f}")
    print(f"Accuracy: {results['accuracy']:.1f}%")
    print(f"Time: {results['elapsed']:.2f}s")
    print(f"Status: {speed_status(results['wpm'])}")
    print()
    print("Press ENTER to exit.")

    while read_key() != "ENTER":
        pass


def main():
    text = get_text()

    clear_screen()
    show_header()
    show_text(text)

    if not wait_for_start():
        return

    results = run_test(text)

    if results is None:
        return

    show_results(text, results)


if __name__ == "__main__":
    main()
