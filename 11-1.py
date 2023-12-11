#!/usr/bin/env python3

import numpy as np

space = []

# Read input
with open('rin.11', 'r') as fd:
    for line in fd:
        space.append([int((ord(c)-46)/(-11)) for c in line[:-1]])

space = np.array(space, dtype=np.uint8)

# Expand space
for i in range(space.shape[0]-1, -1, -1):
    if not np.any(space[i]):
        space = np.insert(space, i, space[i], axis=0)
    if not np.any(space[:,i]):
        space = np.insert(space, i, space[:,i], axis=1)

# Get galaxies
ones = np.argwhere(space)
n_ones = ones.shape[0]

result = 0
for i in range(n_ones):
    for j in range(i):
        result += abs(ones[i][0]-ones[j][0])+abs(ones[i][1]-ones[j][1])

print(result)
