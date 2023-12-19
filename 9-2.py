#!/usr/bin/env python3

import numpy as np

def next_element(seq: [int]) -> int:
    np_seq = np.array(seq)
    arrays = [np_seq]
    while np.any(arrays[-1]):
        # Add ediff1d to arrays until new array only shows zeros
        arrays.append(np.ediff1d(arrays[-1]))
    arrays[-1] = np.insert(arrays[-1], 0, 0)
    for i in range(len(arrays)-2, -1, -1):
        arrays[i] = np.insert(arrays[i], 0, arrays[i][0] - arrays[i+1][0])
    return arrays[0][0]

result = 0
with open('in.9', 'r') as fd:
    for line in fd:
        seq = [int(n) for n in  line[:-1].split()]
        result += next_element(seq)

print(result)
