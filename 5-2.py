#!/usr/bin/env python3

import sys

sections = ['seeds', 'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
            'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
            'humidity-to-location']
section = 0

seeds = []
seed2soil = []
soil2fertilizer = []
fertilizer2water = []
water2light = []
light2temperature = []
temperature2humidity = []
humidity2location = []

with open('in.5', 'r') as fd:
    for line in fd:
        if len(line) == 1:
            if section == 1:
                seed2soil = sorted(seed2soil, key=lambda e: e[1])
            if section == 2:
                soil2fertilizer = sorted(soil2fertilizer, key=lambda e: e[1])
            if section == 3:
                fertilizer2water = sorted(fertilizer2water, key=lambda e: e[1])
            if section == 4:
                water2light = sorted(water2light, key=lambda e: e[1])
            if section == 5:
                light2temperature = sorted(light2temperature, key=lambda e: e[1])
            if section == 6:
                temperature2humidity = sorted(temperature2humidity, key=lambda e: e[1])
            if section == 7:
                humidity2location = sorted(humidity2location, key=lambda e: e[1])
            section += 1
        if section == 0:
            sds = [int(n) for n in  line[7:-1].split(' ')]
            for r in range(0, len(sds), 2):
                seeds.append([sds[r], sds[r+1]])
        elif section == 1 and line[0] in '0123456789':
            m = [int(n) for n in line[:-1].split(' ')]
            seed2soil.append([m[1], m[1] + m[2], m[0] - m[1]])
        elif section == 2 and line[0] in '0123456789':
            m = [int(n) for n in line[:-1].split(' ')]
            soil2fertilizer.append([m[1], m[1] + m[2], m[0] - m[1]])
        elif section == 3 and line[0] in '0123456789':
            m = [int(n) for n in line[:-1].split(' ')]
            fertilizer2water.append([m[1], m[1] + m[2], m[0] - m[1]])
        elif section == 4 and line[0] in '0123456789':
            m = [int(n) for n in line[:-1].split(' ')]
            water2light.append([m[1], m[1] + m[2], m[0] - m[1]])
        elif section == 5 and line[0] in '0123456789':
            m = [int(n) for n in line[:-1].split(' ')]
            light2temperature.append([m[1], m[1] + m[2], m[0] - m[1]])
        elif section == 6 and line[0] in '0123456789':
            m = [int(n) for n in line[:-1].split(' ')]
            temperature2humidity.append([m[1], m[1] + m[2], m[0] - m[1]])
        elif section == 7 and line[0] in '0123456789':
            m = [int(n) for n in line[:-1].split(' ')]
            humidity2location.append([m[1], m[1] + m[2], m[0] - m[1]])

def source2dest(mapping: [[int,int,int]], source: int) -> int:
    for m in mapping:
        if source >= m[0] and source < m[1]:
            return source + m[2]
    return source

min_location = None
# Run all ten series in one shell
n = int(sys.argv[1])
print(n)
seed_range = seeds[n]
print(seed_range)
for seed in range(seed_range[0], seed_range[0]+seed_range[1]):
    location = source2dest(humidity2location,
                   source2dest(temperature2humidity,
                       source2dest(light2temperature,
                           source2dest(water2light,
                               source2dest(fertilizer2water,
                                   source2dest(soil2fertilizer,
                                       source2dest(seed2soil, seed)))))))
    if min_location == None or min_location > location:
        min_location = location
    if (seed - seed_range[0]) % 10000000 == 0:
        print(seed - seed_range[0], min_location)

print(min_location)
