#!/usr/bin/env python3

import numpy as np

def tilt_north(dish: np.array) -> np.array:
    only_cubes = np.full((dish[:, 0].shape), ord('#'), dtype=np.uint8)
    only_rounded = np.full((dish[:, 0].shape), ord('O'), dtype=np.uint8)
    for col in range(dish.shape[1]):
        cubes = dish[:, col] == only_cubes
        rounded = dish[:, col] == only_rounded
        # Move up all rounded rocks up to next cube
        column = []
        row = 0
        while row < dish.shape[0]:
            if cubes[row]:
                column.append(ord('#'))
                row += 1
                n_rounded = 0
                while row < dish.shape[1] and not cubes[row]:
                    if rounded[row]:
                        n_rounded += 1
                    row += 1
                for r in range(n_rounded):
                    column.append(ord('O'))
                for r in range(len(column), row):
                    column.append(ord('.'))
            elif row == 0:
                n_rounded = 0
                while row < dish.shape[1] and not cubes[row]:
                    if rounded[row]:
                        n_rounded += 1
                    row += 1
                for r in range(n_rounded):
                    column.append(ord('O'))
                for r in range(len(column), row):
                    column.append(ord('.'))
            else:
                column.append(ord('.'))
                row += 1
        dish[:,col] = np.array(column, dtype=np.uint8)
    return dish

def get_load(dish: np.array) -> int:
    # np_dish = np.array(dish, dtype=np.uint8)
    n = 0
    height = dish.shape[0]
    for y in range(height):
        n += (height - y) * np.count_nonzero(dish[y] == ord('O'))
    return n

dish = []
with open('in.14', 'r') as fd:
    for line in fd:
        dish.append([ord(c) for c in line[:-1]])

dish = np.array(dish, dtype=np.uint8)
tilt_north(dish)
#for y in range(dish.shape[0]):
#    for x in range(dish.shape[1]):
#        print(chr(dish[y][x]), end='')
#    print()

result = get_load(dish)
print(result)
