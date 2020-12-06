import inputAoC as aoc
groups = aoc.get_input_file(6).split("\n\n")

res1 = 0
for group in groups:
    x = group.replace("\n","")
    letters = set(x)
    res1 += len(letters)

print(res1)

res2 = 0
for group in groups:
    x = group.split("\n")
    letters = set(x[0])
    for word in x[1:]:
        letters = letters.intersection(set(word))
    res2 += len(letters)

print(res2)