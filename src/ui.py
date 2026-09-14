RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"


def clear_screen():
    print("\033[2J\033[H", end="")


def show_header():
    print(f"{BOLD}{CYAN}TypeTest{RESET}")
    print()
    print("Type the following text as fast and accurately as you can.")
    print()


def show_text(text):
    print(f"{DIM}{text}{RESET}")
    print()


def show_stats(wpm, accuracy, elapsed):
    print(
        f"WPM: {wpm:.1f}    "
        f"Accuracy: {accuracy:.1f}%    "
        f"Time: {elapsed:.1f}s"
    )


def show_results(test):
    results = test.results()

    print()
    print("-" * 45)
    print("Results")
    print("-" * 45)

    print(f"Time:     {results['time']:.2f}s")
    print(f"WPM:      {results['wpm']:.1f}")
    print(f"Accuracy: {results['accuracy']:.1f}%")

    print("-" * 45)