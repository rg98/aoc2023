#!/usr/bin/env python3

import numpy as np

space = []

# Read input
with open('in.11', 'r') as fd:
    for line in fd:
        space.append([int((ord(c)-46)/(-11)) for c in line[:-1]])

space = np.array(space, dtype=np.uint8)

# Get galaxies
m_ones = np.argwhere(space)
n_m_ones = m_ones.shape[0]

# Get measured distances
results_measured = []
for i in range(n_m_ones):
    for j in range(i):
        results_measured.append(abs(m_ones[i][0]-m_ones[j][0])+abs(m_ones[i][1]-m_ones[j][1]))

# Expand space
for i in range(space.shape[0]-1, -1, -1):
    if not np.any(space[i]):
        space = np.insert(space, i, space[i], axis=0)
    if not np.any(space[:,i]):
        space = np.insert(space, i, space[:,i], axis=1)

# Get galaxies
ones = np.argwhere(space)
n_ones = ones.shape[0]

results = []
for i in range(n_ones):
    for j in range(i):
        results.append(abs(ones[i][0]-ones[j][0])+abs(ones[i][1]-ones[j][1]))

result_difference = sum(results) - sum(results_measured)

print(sum(results_measured)+999999*result_difference)
