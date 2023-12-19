#!/usr/bin/env python3
import math, re
from numpy import prod

time = None
distance = None
with open('in.6', 'r') as fd:
    for line in fd:
        if time:
            distance = [n for n in re.findall('(\d+)', line)]
            distance = int(''.join(distance))
        else:
            time = [n for n in re.findall('(\d+)', line)]
            time = int(''.join(time))

# distance = (t - t_w) * t_w = - t_w^2 + t_w * t
# distance(t_opt) = (t/2)^2

# How many times in ms could beat the best distance?
# low = t/2 - sqrt((t/2)^2 - d)
# high = t/2 + sqrt((t/2)^2 - d)

low = int(float(time)/2 - math.sqrt((float(time)/2)**2 - distance))
while (time - low) * low <= distance:
    low += 1

high = int(float(time)/2 + math.sqrt((float(time)/2)**2 - distance))
while (time - high) * high <= distance:
    high -= 1

print(high - low + 1)

