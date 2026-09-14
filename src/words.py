import random


TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Linux gives you the freedom to understand how your computer works.",
    "Programming is not about knowing everything, but knowing how to solve problems.",
    "A good programmer writes code that is easy to understand and maintain.",
    "The best way to learn programming is to build things and make mistakes.",
    "Open source software allows people to study, modify, and share code.",
    "Simple code is easier to read, debug, and maintain.",
    "Every bug is a chance to understand your code a little better.",
    "Good software is built one small improvement at a time.",
    "The terminal may look intimidating, but it is just another way to talk to your computer.",
    "Learning a new programming language takes patience, practice, and a lot of broken code.",
    "You do not need to memorize everything when you know how to find the answer.",
    "A computer does exactly what you tell it to do, not what you meant it to do.",
    "The fastest way to become better at programming is to keep building real projects.",
    "Clean code is not about writing less code, it is about making the code easier to understand.",
]


def get_text():
    return random.choice(TEXTS)