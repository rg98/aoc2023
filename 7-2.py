#!/usr/bin/env python3

import functools

games = []

with open('in.7', 'r') as fd:
    for line in fd:
        hand, bid = line[:-1].split(' ')
        games.append((hand, int(bid)))

trans_table = str.maketrans('J23456789TQKA', 'abcdefghijklm')

def compareHands(a: (str, int), b: (str, int)) -> int:
    # Build dictionaries with the number of cards in the hand
    c_a = {c:a[0].count(c) for c in a[0]}
    c_a = {k: v for k, v in sorted(c_a.items(), key=lambda item: item[1], reverse=True)}
    c_b = {c:b[0].count(c) for c in b[0]}
    c_b = {k: v for k, v in sorted(c_b.items(), key=lambda item: item[1], reverse=True)}
    # If there are jockers, translate them into first best cards
    j_a = c_a['J'] if 'J' in c_a else 0
    j_b = c_b['J'] if 'J' in c_b else 0
    if j_a > 0:
        if j_a == 5:
            c_a =  {'A': 5}
        else:
            del c_a['J']
            c_a[list(c_a.keys())[0]] += j_a
    if j_b > 0:
        if j_b == 5:
            c_b =  {'A': 5}
        else:
            del c_b['J']
            c_b[list(c_b.keys())[0]] += j_b
    # Early out if a hand has more multiples
    if list(c_a.values())[0] < list(c_b.values())[0]:
        return -1
    elif list(c_a.values())[0] > list(c_b.values())[0]:
        return 1
    else:
        if list(c_a.values())[0] == 3:
            # print(f'{a} and {b} have at least three of a kind')
            if len(c_a) < len(c_b):
                # print(f'{a} is full house')
                return 1
            elif len(c_a) > len(c_b):
                # print(f'{b} is full house')
                return -1
            elif len(c_a) == 2 and len(c_b) == 2:
                # print(f'{a} and {b} are full house')
                if a[0].translate(trans_table) < b[0].translate(trans_table):
                    return -1
                elif a[0].translate(trans_table) > b[0].translate(trans_table):
                    return 1
            else:
                # print(f'{a} and {b} are three of a kind')
                if a[0].translate(trans_table) < b[0].translate(trans_table):
                    return -1
                elif a[0].translate(trans_table) > b[0].translate(trans_table):
                    return 1
        elif list(c_a.values())[0] == 2:
            # print(f'{a} and {b} have at least two of a kind')
            if list(c_a.values())[0:2] == [2, 1] and list(c_b.values())[0:2] == [2, 2]:
                # print(f'{b} has two pairs')
                return -1
            elif list(c_a.values())[0:2] == [2, 2] and list(c_b.values())[0:2] == [2, 1]:
                # print(f'{a} has two pairs')
                return 1
            elif list(c_a.values())[0:2] == [2, 2] and list(c_b.values())[0:2] == [2, 2]:
                # print(f'{a} and {b} have two pairs')
                if a[0].translate(trans_table) < b[0].translate(trans_table):
                    return -1
                elif a[0].translate(trans_table) > b[0].translate(trans_table):
                    return 1
            else:
                if a[0].translate(trans_table) < b[0].translate(trans_table):
                    return -1
                elif a[0].translate(trans_table) > b[0].translate(trans_table):
                    return 1
        else:
            if a[0].translate(trans_table) < b[0].translate(trans_table):
                return -1
            elif a[0].translate(trans_table) > b[0].translate(trans_table):
                return 1
    return 0

games = sorted(games, key=functools.cmp_to_key(compareHands))

result = 0
for i, game in enumerate(games):
    result += (i+1) * game[1]
    # print(i+1, game, (i+1) * game[1])


print(result)
