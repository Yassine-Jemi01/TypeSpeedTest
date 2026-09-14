RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
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
