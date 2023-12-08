#!/usr/bin/env python3

import math, re

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

def all_pos_on_Z(positions: [str]) -> bool:
    for pos in positions:
        if pos[2] != 'Z':
            return False
    return True

# Count steps for every start position
n_instr = len(instr)
positions = [pos for pos in Map.keys() if pos[2] == 'A']
steps = {}
for pos in positions:
    step = 0
    p = pos
    while p[2] != 'Z':
        p = Map[p][instr[step % n_instr]]
        step += 1
    steps[pos] = step

# Get prime factors for all step numbers
highest_steps = sorted(list(steps.values()))[-1]

primes = list(range(0, highest_steps+1))
for n in range(2, int(math.sqrt(highest_steps))):
    for i in range(n * 2, highest_steps+1, n):
        primes[i] = 0
primes = [p for p in primes[2:] if p > 0]

# Split step numbers by prime factors
prime_factors = []
for step in steps.values():
    if step in primes:
        print(f'{step} is prime')
    else:
        for p in primes:
            if (step % p) == 0:
                if p not in prime_factors:
                    prime_factors.append(p)

# Result is product of all prime factors
result = 1
for f in prime_factors:
    result *= f

print(result)
