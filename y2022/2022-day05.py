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
input = aoc.get_input_file(5,2022)
stacks_input, instrs = input.split("\n\n")
stacks_input = stacks_input.splitlines()
n = int(re.findall('\d+',stacks_input[-1])[-1])
# n = 9 # 3 in example

stacks = dict()
for i in range(n):
    stacks[i+1] = deque()
    for line in stacks_input[:-1][::-1]:
        crate = line[4*i+1]
        if crate != " ": stacks[i+1].append(crate)

stacks2 = dict()
for i in range(1,n+1):
    stacks2[i] = stacks[i].copy()

for instr in instrs.splitlines():
    nb, from_stack, to_stack = map(int,re.match("move (\d+) from (\d) to (\d)",instr).groups())
    to_move = []
    for _ in range(nb):
        stacks[to_stack].append(stacks[from_stack].pop())
        to_move.append(stacks2[from_stack].pop())
    stacks2[to_stack].extend(to_move[::-1])

def top_crates(stacks):
    ans = ""
    for i in range(1,n+1):
        last = stacks[i].pop()
        ans += last
        stacks[i].append(last)
    return ans

res1 = top_crates(stacks)
print(res1)
res2 = top_crates(stacks2)
print(res2)