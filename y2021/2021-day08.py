import inputAoC as aoc

input = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""
input = aoc.get_input_file(8,2021)
entries = input.splitlines()

for i in range(len(entries)):
    entry = entries[i]
    patterns, values = entry.split(" | ")
    values = values.split(" ")
    entries[i] = (patterns, values)

#print(entries)

nbs = [0] * 10

for entry in entries:
    values = entry[1]
    for val in values:
        if len(val) == 2: nbs[1] += 1
        elif len(val) == 3: nbs[7] += 1
        elif len(val) == 4: nbs[4] += 1
        elif len(val) == 7: nbs[8] += 1

res1 = nbs[1] + nbs[4] + nbs[7] + nbs[8]
print(res1)