#!/usr/bin/env python3

number_strings = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
first_chars = list('123456789efnost')

numbers = []
with open('in.1', 'r') as fd:
    for line in fd:
        digits = []
        for n, c in enumerate(line):
            if c in first_chars:
                if c in '123456789':
                    digits.append(number_strings[c])
                elif c == 'o' and line[n:].startswith('one'):
                    digits.append(1)
                elif c == 't':
                    if line[n:].startswith('two'):
                        digits.append(2)
                    elif line[n:].startswith('three'):
                        digits.append(3)
                elif c == 'f':
                    if line[n:].startswith('four'):
                        digits.append(4)
                    elif line[n:].startswith('five'):
                        digits.append(5)
                elif c == 's':
                    if line[n:].startswith('six'):
                        digits.append(6)
                    elif line[n:].startswith('seven'):
                        digits.append(7)
                elif c == 'e' and line[n:].startswith('eight'):
                    digits.append(8)
                elif c == 'n' and line[n:].startswith('nine'):
                    digits.append(9)
        numbers.append(int(digits[0])*10+int(digits[-1]))

print(sum(numbers))
