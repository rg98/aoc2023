#!/usr/bin/env python3

limits = {'red': 12, 'green': 13, 'blue': 14}
result = 0
with open('in.2', 'r') as fd:
    for line in fd:
        game = line[:-1].split(':')
        n_game = int(game[0].split(' ')[1])
        sets = game[1].split(';')
        try:
            for s in sets:
                colors = s.split(',')
                for color in colors:
                    n, c = color[1:].split(' ')
                    if int(n) > limits[c]:
                        raise RuntimeError(f'Limit on {c} reached in game {n_game}')
            result += n_game
        except RuntimeError as e:
           print(e)
           pass

print(result)
