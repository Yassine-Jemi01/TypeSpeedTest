import time

from input import read_key
from words import get_text
from ui import clear_screen, show_header, show_text

def calculate_accuracy(text, typed):
    if not typed:
        return 0

    correct = sum(
        expected == actual
        for expected, actual in zip(text, typed)
    )

    return correct / len(typed) * 100


def calculate_wpm(typed, start_time):
    elapsed = time.perf_counter() - start_time

    if elapsed <= 0:
        return 0

    minutes = elapsed / 60
    return (len(typed) / 5) / minutes


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
    clear_screen()

    show_header()
    show_text(text)

    wpm = calculate_wpm(typed, start_time)
    accuracy = calculate_accuracy(text, typed)

    print(
        f"WPM: {wpm:.1f}    "
        f"Accuracy: {accuracy:.1f}%    "
        f"Time: {time.perf_counter() - start_time:.1f}s"
    )

    print(f"Status: {speed_status(wpm)}")
    print()
    print(f"> {typed}", end="", flush=True)


def main():
    text = get_text()

    clear_screen()
    show_header()
    show_text(text)

    print("Press ENTER to start.")
    print("Press ESC to quit.")

    while True:
        key = read_key()

        if key == "ENTER":
            break

        if key == "ESC" or key == "CTRL_C":
            return

    typed = ""
    start_time = time.perf_counter()

    render(text, typed, start_time)

    while len(typed) < len(text):
        key = read_key()

        if key in ("ESC", "CTRL_C"):
            return

        if key == "BACKSPACE":
            typed = typed[:-1]

        elif len(key) == 1:
            typed += key

        render(text, typed, start_time)

    end_time = time.perf_counter()

    elapsed = end_time - start_time
    wpm = (len(typed) / 5) / (elapsed / 60)
    accuracy = calculate_accuracy(text, typed)

    clear_screen()

    show_header()
    show_text(text)

    print(f"WPM: {wpm:.1f}")
    print(f"Accuracy: {accuracy:.1f}%")
    print(f"Time: {elapsed:.2f}s")
    print(f"Status: {speed_status(wpm)}")

    print()
    print("Press ENTER to exit.")

    while read_key() != "ENTER":
        pass


if __name__ == "__main__":
    main()