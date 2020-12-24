import inputAoC as aoc
from collections import deque

MOVES = 10000000
PICK = 3

cups = [int(cup) for cup in aoc.get_input_file(23, 2020)]
cups_ex = [3, 8, 9, 1, 2, 5, 4, 6, 7]


class Cups:
    PICK = 3

    def __init__(self, cups, MAX=-1):
        self.cups = [int(cup) for cup in cups]
        self.MAX = max(cups)
        if MAX > 0:
            for i in range(self.MAX+1, MAX+1): 
                self.cups.append(i)
            self.MAX = MAX
    
    def move1(self, turn):
        turn -= 1 #turn commence à 1
        turn %= self.MAX
        cup = self.cups[turn]

        pick_up = []
        for pick in range(self.PICK):
            try:
                pick_up.append(self.cups.pop(turn+1))
            except IndexError: # circulaire
                pick_up.append(self.cups.pop(0))

        dest = cup - 1
        if dest == 0: dest = self.MAX
        while dest in pick_up:
            dest -= 1
            if dest == 0: dest = self.MAX

        index = self.cups.index(dest) + 1
        for i in range(index, index+self.PICK):
            self.cups.insert(i, pick_up.pop(0))
        
        # le début doit se retrouver à la fin
        nb_slice = self.cups.index(cup) - turn
        for _ in range(nb_slice):
            self.cups.append(self.cups.pop(0))
        
        assert cup == self.cups[turn]


    def moves(self, n, to_print=False):
        for turn in range(1, n+1):
            if to_print: print(turn, ":", self.cups)
            self.move1(turn)
            # print(turn)
        if to_print: print("final", self.cups)

    def score(self):
        i = self.cups.index(1)
        res = self.cups[i+1:] + self.cups[:i]
        return "".join([str(cup) for cup in res])
    
    def score2(self):
        i = self.cups.index(1)
        try:
            return self.cups[i+1] * self.cups[i+2]
        except IndexError:
            if i == len(self.cups) - 1:
                return self.cups[0] * self.cups[1]
            else: # i == len(self.cups) - 2
                return self.cups[i+1] * self.cups[0]

cups2_ex = Cups(cups_ex)
cups2_ex.moves(10, True)


cups1 = Cups(cups)
cups1.moves(100)
res1 = cups1.score()
print(res1)



cups2 = Cups(cups, 1000000)
#cups2.moves(10000000)
res2 = cups2.score2()
print(res2)