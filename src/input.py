import os
import sys


def read_key():
    if os.name == "nt":
        return _read_windows()

    return _read_unix()


def _read_windows():
    import msvcrt

    key = msvcrt.getwch()

    if key == "\r":
        return "ENTER"

    if key == "\x08":
        return "BACKSPACE"

    if key == "\x03":
        return "CTRL_C"

    if key == "\x1b":
        return "ESC"

    return key


def _read_unix():
    import termios
    import tty

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)

        if key == "\x03":
            return "CTRL_C"

        if key in ("\r", "\n"):
            return "ENTER"

        if key in ("\x7f", "\b"):
            return "BACKSPACE"

        if key == "\x1b":
            return "ESC"

        return key

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)