#!/usr/bin/env python3

limits = {'red': 12, 'green': 13, 'blue': 14}
result = 0
with open('in.2', 'r') as fd:
    for line in fd:
        game = line[:-1].split(':')
        n_game = int(game[0].split(' ')[1])
        game_limit = {'red': 0, 'green': 0, 'blue': 0}
        sets = game[1].split(';')
        for s in sets:
            colors = s.split(',')
            for color in colors:
                n, c = color[1:].split(' ')
                if int(n) > game_limit[c]:
                    game_limit[c] = int(n)
        result += game_limit['red'] * game_limit['green'] * game_limit['blue']

print(result)
