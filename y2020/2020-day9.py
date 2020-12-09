import inputAoC as aoc
from collections import deque

PREAMBULE = 25
nbs = [int(i) for i in aoc.get_input_file(9,2020).split("\n")]

def is_sum(val,nbs):
    for elem in nbs:
        if val-elem in nbs:
            return True
    return False

res1 = int()
for index, val in list(enumerate(nbs))[PREAMBULE:]:
    if not is_sum(val, nbs[index-PREAMBULE:index]):
        res1 = val
        break
print(res1)

res2 = int()
acc = 0
queue = deque()
index = -1
while not acc == res1:
    index += 1
    elem = nbs[index]
    acc += elem
    queue.append(elem)
    while acc > res1:
        acc -= queue.popleft()

res2 = max(queue) + min(queue)
print(res2)