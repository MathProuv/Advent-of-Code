import inputAoC as aoc

input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
input = aoc.get_input_file(12,2021)

connections = [tuple(conn.split('-')) for conn in input.splitlines()]

connec_dict = {}
for a,b in connections:
    if a not in connec_dict.keys() and a != "end": connec_dict[a] = set()
    if b not in connec_dict.keys() and b != "end": connec_dict[b] = set()
    if b != "start" and a != "end": connec_dict[a].add(b)
    if a != "start" and b != "end": connec_dict[b].add(a)

chemins = []
stack = [['start']]
stack_double = []

while stack:
    temp = stack.pop()
    last = temp[-1]
    for next in connec_dict[last]:
        chemin = temp + [next]
        if next == 'end':
            chemins.append(chemin)
        elif next.isupper() or next not in temp:
            stack.append(chemin)
        #new for part 2
        elif next in temp:
            stack_double.append(chemin)

res1 = len(chemins)
print(res1)

while stack_double:
    temp = stack_double.pop()
    last = temp[-1]
    for next in connec_dict[last]:
        chemin = temp + [next]
        if next == 'end':
            chemins.append(chemin)
        elif next.isupper() or next not in temp:
            stack_double.append(chemin)

res2 = len(chemins)
print(res2)