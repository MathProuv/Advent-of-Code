import inputAoC as aoc
from collections import deque
import re

input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
n = 3
input, n = aoc.get_input_file(5,2022), 9
stacks_int, instrs = input.split("\n\n")

stacks = dict()
for i in range(1,n+1):
    stacks[i] = deque()
for line in stacks_int.split('\n')[:-1][::-1]:
    for i in range(n):
        item = line[4*i+1]
        if item != " ":
            stacks[i+1].append(item)

stacks9001 = dict()
for i in range(1,n+1):
    stacks9001[i] = stacks[i].copy()

for instr in instrs.splitlines():
    nb, from_stack, to_stack = map(int,re.match("move (\d+) from (\d) to (\d)",instr).groups())
    to_move = []
    for _ in range(nb):
        stacks[to_stack].append(stacks[from_stack].pop())
        to_move.append(stacks9001[from_stack].pop())
    stacks9001[to_stack].extend(to_move[::-1])

def res(stacks):
    ans = ""
    for i in range(1,n+1):
        last = stacks[i].pop()
        ans += last
        stacks[i].append(last)
    return ans

res1 = res(stacks)
print(res1)
res2 = res(stacks9001)
print(res2)