#!/usr/bin/env python3

def get_score(card: str) -> int:
    card, numbers = card.split(': ')
    winners, candidates = numbers.split(' | ')
    if winners[0] == ' ':
        winners = winners[1:]
    if candidates[0] == ' ':
        candidates = candidates[1:]
    winners = [int(n) for n in winners.replace('  ', ' ').split(' ')]
    candidates = [int(n) for n in candidates.replace('  ', ' ').split(' ')]
    winners = sorted(winners)
    candidates = sorted(candidates)
    n_winner = 0
    i_w = 0
    i_c = 0
    while i_w < len(winners) and i_c < len(candidates):
        if winners[i_w] < candidates[i_c]:
            i_w += 1
        elif winners[i_w] > candidates[i_c]:
            i_c += 1
        else:
            i_w += 1
            i_c += 1
            n_winner = 1 if n_winner == 0 else n_winner * 2
    return n_winner

result = 0
with open('in.4', 'r') as fd:
    for line in fd:
        result += get_score(line[:-1])

print(result)
