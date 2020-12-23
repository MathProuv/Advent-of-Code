import inputAoC as aoc
from collections import deque

MOVES = 10000000
PICK = 3

cups = [int(cup) for cup in aoc.get_input_file(23, 2020)]
cups_ex = [3, 8, 9, 1, 2, 5, 4, 6, 7]

def move1(cups, turn):
    LEN = len(cups)
    MIN = min(cups)
    MAX = max(cups)
    turn -= 1
    turn %= LEN
    cups_this_turn = cups[turn:] + cups[:turn]
    cup = cups_this_turn[0]
    pick_up = [cups_this_turn.pop(1) for _ in range(PICK)]
    destination = cup - 1
    while destination in pick_up or destination == cup or destination < MIN:
        destination -= 1
        if destination < MIN: destination = MAX
    i = cups_this_turn.index(destination) + 1
    cups_this_turn = cups_this_turn[:i] + pick_up + cups_this_turn[i:]
    res = cups_this_turn[LEN-turn:] + cups_this_turn[:LEN-turn]
    return res

def moves(cups, N=MOVES, to_print=False):
    for turn in range(1, N+1):
        if to_print: print(turn, cups)
        cups = move1(cups, turn)
        print(turn)
    if to_print: print("final", cups)
    return cups

def score(cups):
    i = cups.index(1)
    res = cups[i+1:] + cups[:i]
    return "".join([str(cup) for cup in res])


res1 = score(moves(cups, 100))
print(res1)

cups2 = cups[::]
for cup in range(max(cups), 1000000+1):
    cups2.append(cup)

def score2(cups):
    i = cups.index(1)
    return cups[i+1] * cups[i+2]

res2 = score2(moves(cups2))
print(res2)