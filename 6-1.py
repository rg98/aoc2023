#!/usr/bin/env python3
import math, re
from numpy import prod

times = None
distances = None
with open('in.6', 'r') as fd:
    for line in fd:
        if times:
            distances = [int(n) for n in re.findall('(\d+)', line)]
        else:
            times = [int(n) for n in re.findall('(\d+)', line)]

# distance = (t - t_w) * t_w = - t_w^2 + t_w * t
# distance(t_opt) = (t/2)^2

# How many times in ms could beat the best distance?
# low = t/2 - sqrt((t/2)^2 - d)
# high = t/2 + sqrt((t/2)^2 - d)

results = []
for i in range(len(times)):
    low = int(float(times[i])/2 - math.sqrt((float(times[i])/2)**2 - distances[i]))
    while (times[i] - low) * low <= distances[i]:
        low += 1

    high = int(float(times[i])/2 + math.sqrt((float(times[i])/2)**2 - distances[i]))
    while (times[i] - high) * high <= distances[i]:
        high -= 1
    
    results.append(high - low + 1)

print(prod(results))
