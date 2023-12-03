#!/usr/bin/env python3

# Read in schema
schema = []
with open('in.3', 'r') as fd:
    for line in fd:
        line = line[:-1]
        schema.append(line)

# is_part
# we check the following positions
# 123
# 4X6
# 789
def is_star(schema: [str], num: str, x: int, y: int) -> (int, int, int):
    height = len(schema)
    width = len(schema[0])
    n_chars = len(num)
    for c in range(n_chars):
        if c == 0:
            # On the left edge, check 1, 2, 4, 7, 8
            if y > 0 and x > 0 and schema[y-1][x-1] in '*':
                return num, x-1, y-1
            if y > 0 and schema[y-1][x] in '*':
                return num, x, y-1
            if x > 0 and schema[y][x-1] in '*':
                return num, x-1, y
            if y < height - 1 and x > 0 and schema[y+1][x-1] in '*':
                return num, x-1, y+1
            if y < height - 1 and schema[y+1][x] in '*':
                return num, x, y+1
            if n_chars == 1:
                if y > 0 and x < width - 1 and schema[y-1][x+1] in '*':
                    return num, x+1, y-1
                if x < width - 1 and schema[y][x+1] in '*':
                    return num, x+1, y
                if y < height - 1 and x < width - 1 and schema[y+1][x+1] in '*':
                    return num, x+1, y+1
        elif c == n_chars - 1:
            # On the right edge check 2, 3, 6, 8, 9
            if y > 0 and x + c < width and schema[y-1][x+c] in '*':
                return num, x+c, y-1
            if y > 0 and x + c < width - 1 and schema[y-1][x+c+1] in '*':
                return num, x+c+1, y-1
            if x + c < width - 1 and schema[y][x+c+1] in '*':
                return num, x+c+1, y
            if y < height - 1 and x + c < width and schema[y+1][x+c] in '*':
                return num, x+c, y+1
            if y < height - 1 and x + c < width - 1 and schema[y+1][x+c+1] in '*':
                return num, x+c+1, y+1
        else:
            # In the middle check 2, 8
            if y > 0 and x + c < width and schema[y-1][x+c] in '*':
                return num, x+c, y-1
            if y < height - 1 and x + c < width and schema[y+1][x+c] in '*':
                return num, x+c, y+1
    return None, -1, -1

def next_num(schema: [str], x: int, y: int) -> (str, int, int):
    i = y
    j = x
    for row in schema[y:]:
        for c in row[j:]:
            if c in '0123456789':
                n = c
                k =  j + 1
                while k < len(row) and row[k] in '0123456789':
                    n += row[k]
                    k +=  1
                return n, j, i
            else:
                j += 1
        j = 0
        i += 1
    return None, -1, -1

# Find numbers and check for parts
x = 0
y = 0
n = ''
stars = []
while True: 
    n, x, y = next_num(schema, x + len(n), y)
    if n:
        star = is_star(schema, n, x, y)
        if star[0]:
            stars.append(star)
    else:
        break

stars = sorted(stars, key=lambda e: (e[1], e[2]))

result = 0
oldstar = stars[0]
for star in stars[1:]:
    if oldstar[1] == star[1] and oldstar[2] == star[2]:
        result += int(oldstar[0]) * int(star[0])
    oldstar = star

print(result)
