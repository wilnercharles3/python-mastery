#!/usr/bin/env python3
"""
Chapter 9 - Project 3: Phone & Email Extractor
Automate the Boring Stuff with Python (3e)

Finds phone numbers and email addresses in a block of text.
Built from the Ch 9 regex skills: \\d, character classes, quantifiers,
groups, alternation, escaping, and re.findall.
"""
import re

# Phone: optional area code (bare 415 or in parens (415)), then 555-1234.
# Separators can be a dash, dot, or whitespace.
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code, optional - bare or wrapped in parens
    [-.\s]?             # separator after area code
    \d{3}               # first 3 digits
    [-.\s]              # separator
    \d{4}               # last 4 digits
    )''', re.VERBOSE)

# Email: username @ domain . tld
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    \.[a-zA-Z]{2,4}     # dot-something (.com, .org, .co)
    )''', re.VERBOSE)


def extract(text):
    """Return (phones, emails) found in text."""
    phones = [match[0] for match in phone_regex.findall(text)]
    emails = email_regex.findall(text)
    return phones, emails


if __name__ == '__main__':
    sample = """
    Front desk: 415-555-1234 or (212) 555-0199.
    Sales line 800.555.7600. Questions? charles.dev@example.com
    or wilner_99@gmail.com.
    """
    phones, emails = extract(sample)

    print('Phones found:')
    for p in phones:
        print('  ' + p)

    print('Emails found:')
    for e in emails:
        print('  ' + e)
