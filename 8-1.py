#!/usr/bin/env python3

import re

instr = ''
Map = {}

with open('in.8', 'r') as fd:
    for line in fd:
        if len(instr) == 0 and len(line) > 1:
            instr = list(line[:-1])
        elif len(line) > 1:
            expr = re.match('([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line[:-1])
            f, l, r = expr.group(1,2,3)
            Map[f] = {'L': l, 'R': r}

n_instr = len(instr)
steps = 0
pos = 'AAA'
while pos != 'ZZZ':
    pos = Map[pos][instr[steps % n_instr]]
    steps += 1

print(steps)
