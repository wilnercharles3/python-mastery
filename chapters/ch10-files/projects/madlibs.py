#!/usr/bin/env python3
"""
Chapter 10 - Madlibs (capstone project)
Automate the Boring Stuff with Python (3e)

Reads a template file containing ALL-CAPS placeholders (ADJECTIVE, NOUN, VERB),
prompts the user to fill each one, swaps them in, and writes the finished story
to an output file.

Practices the Ch 10 core:
  - open() in read mode + .read()          (pull the template into one string)
  - str.replace(old, new)                  (returns a NEW string; reassign to stack swaps)
  - open() in write mode 'w' + .write()    (creates/overwrites the output file)

Key idea locked this session: each .replace() is reassigned back to `text` so
the swaps BUILD on each other instead of getting lost in separate variables.
"""

TEMPLATE_FILE = 'template.txt'
OUTPUT_FILE = 'output.txt'

# Placeholders to look for, in the order we'll ask about them.
PLACEHOLDERS = ['ADJECTIVE', 'NOUN', 'VERB']


def article(word):
    """Pick 'an' for vowel-starting placeholders, else 'a' (just for a nicer prompt)."""
    return 'an' if word[0] in 'AEIOU' else 'a'


def fill_template(text):
    """Replace every placeholder in `text` with user input and return the result."""
    for placeholder in PLACEHOLDERS:
        # Only ask if the placeholder actually appears in the template.
        if placeholder in text:
            word = input(f'Enter {article(placeholder)} {placeholder}: ')
            # Reassign to text so each swap builds on the previous ones.
            text = text.replace(placeholder, word)
    return text


def main():
    # 1. Read the template into a single string.
    with open(TEMPLATE_FILE) as f:
        text = f.read()

    # 2. Fill every placeholder.
    text = fill_template(text)

    # 3. Write the finished story out (write mode creates/overwrites the file).
    with open(OUTPUT_FILE, 'w') as f:
        f.write(text)

    print('\n--- Your story ---')
    print(text)
    print(f'(also saved to {OUTPUT_FILE})')


if __name__ == '__main__':
    main()
