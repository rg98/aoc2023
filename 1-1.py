#!/usr/bin/env python3

numbers = []
with open('in.1', 'r') as fd:
    for line in fd:
        digits = [n for n in line if n >= '0' and n <= '9']
        numbers.append(int(digits[0])*10+int(digits[-1]))

print(sum(numbers))
