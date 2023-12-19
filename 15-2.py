#!/usr/bin/env python3

import re

def hash_string(s: str) -> int:
    Hash = 0
    for c in s:
        Hash += ord(c)
        Hash = (Hash * 17) % 256
    return Hash

def insert_lens(name: str, f: int, box: int, boxes: [[(str, int)]]) -> [[(str, int)]]:
    n = [n for n, e in enumerate(boxes[box]) if e[0] == name]
    if op == '=':
        if len(n):
            boxes[box][n[0]] = (name, f)
        else:
            boxes[box].append((name, f))
    else:
        if len(n):
            del boxes[box][n[0]]
    return boxes

with open('in.15', 'r') as fd:
    line = fd.read()

# Remove newline
line = line[:-1]

# Split by ,
hashes = line.split(',')

boxes = [[] for i in range(256)]

for s in hashes:
    m = re.fullmatch('(.*)([-=])(\d+)?', s)
    if m:
        name, op, f = m.group(1, 2, 3)
        f = int(f) if f else 0
        boxes = insert_lens(name, int(f), hash_string(name), boxes)
    else:
        raise RuntimeError(f'{s} could not split')

result = 0
for nbox, box in enumerate(boxes):
    for n, element in enumerate(box):
        result += (nbox+1) * (n+1) * element[1]

print(result)
