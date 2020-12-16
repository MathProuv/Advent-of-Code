import inputAoC as aoc
import my_utils

ex = """0,3,6"""

start = [int(nb) for nb in aoc.get_input_file(15,2020).split(",")]
start_ex = [int(nb) for nb in ex.split(",")]

def turn1(start):
    last = start[-1]
    new = 0
    if last in start[:-1]:
        new = len(start)-1 - my_utils.rindex(start[:-1],last)
    start.append(new)
    return new

def play1(start, n=2020):
    for i in range(len(start), n):
        turn1(start)
        # print(i,turn1(start))
    return start[-1]

def turn2(mem, last_elem, turn):
    if last_elem in mem:
        new = turn - mem[last_elem]
        mem[last_elem] = turn
    else:
        new = 0
        mem[last_elem] = turn
    #print("last_elem =", last_elem,"c'était le tour", turn,"(+1 cf tour 0)")
    #print(mem)
    return new

def play2(mem, n=30000000):
    start_index = -1
    last_elem = 0
    for key, value in mem.items():
        if value > start_index:
            start_index = value
            last_elem = key
    start_index = mem[last_elem]
    del mem[last_elem]
    for turn in range(start_index-1, n-2):
        last_elem = turn2(mem, last_elem, turn+1)
    return last_elem

mem_ex = dict()
for index, elem in enumerate(start_ex):
    mem_ex[int(elem)] = index
# print(play1(start_ex, 10))
# print(play2(mem_ex, 10))

assert play1(start_ex,2020) == 436
assert play2(mem_ex,2020) == 436


res1 = play1(start)
print(res1)

mem = dict()
for index, elem in enumerate(start):
    mem[int(elem)] = index
# print(mem)

#print("""C'est un peu long (~15s)...""")

res2 = play2(mem)
print(res2)