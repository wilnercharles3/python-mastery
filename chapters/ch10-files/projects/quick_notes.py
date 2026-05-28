#!/usr/bin/env python3
"""
Chapter 10 - Quick Notes
Automate the Boring Stuff with Python (3e)

Appends a timestamped note to notes.txt, then prints the whole file back.
Practices: open() in append mode, the with statement, .write() (no auto
newline, so add \\n yourself), and .read().
"""
from datetime import datetime

NOTES_FILE = 'notes.txt'


def add_note(text):
    """Append one timestamped line to the notes file (keeps existing content)."""
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(NOTES_FILE, 'a') as f:
        f.write(f'[{stamp}] {text}\n')


def show_notes():
    """Read and print everything saved so far."""
    with open(NOTES_FILE) as f:
        print(f.read())


if __name__ == '__main__':
    add_note('Bought groceries')
    show_notes()
