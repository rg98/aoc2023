#!/usr/bin/env python3

import numpy as np

result = 0

with open('in.13', 'r') as fd:
    group = []
    for line in fd:
        if len(line) == 1:
            pattern = np.array(group, dtype=np.uint8)
            # Search two equal rows or columns in pattern
            horizontal = False
            for n in range(pattern.shape[0] - 1):
                if (pattern[n] == pattern[n+1]).all():
                    height = min(n+1, pattern.shape[0] - 1 - n)
                    if (pattern[n+1-height:n+1] == np.flip(pattern[n+1:n+1+height], axis=0)).all():
                        result +=  (n + 1) * 100
                        horizontal = True
                        break
            if not horizontal:
                for n in range(pattern.shape[1] - 1):
                    if (pattern[:, n] == pattern[:, n+1]).all():
                        width = min(n+1, pattern.shape[1] - 1 - n)
                        if (pattern[:, n+1-width:n+1] == np.flip(pattern[:, n+1:n+1+width], axis=1)).all():
                            result += (n + 1)
                            break
            group = []
        else:
            group.append([int((ord(c)-46)/(-11)) for c in line[:-1]])

pattern = np.array(group, dtype=np.uint8)
# Search two equal rows or columns in pattern
horizontal = False
for n in range(pattern.shape[0] - 1):
    if (pattern[n] == pattern[n+1]).all():
        height = min(n+1, pattern.shape[0] - 1 - n)
        if (pattern[n+1-height:n+1] == np.flip(pattern[n+1:n+1+height], axis=0)).all():
            result +=  (n + 1) * 100
            horizontal = True
            break
if not horizontal:
    for n in range(pattern.shape[1] - 1):
        if (pattern[:, n] == pattern[:, n+1]).all():
            width = min(n+1, pattern.shape[1] - 1 - n)
            if (pattern[:, n+1-width:n+1] == np.flip(pattern[:, n+1:n+1+width], axis=1)).all():
                result += (n + 1)
                break
print(result)
