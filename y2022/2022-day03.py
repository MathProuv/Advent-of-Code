import inputAoC as aoc

input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
input = aoc.get_input_file(3,2022)
backpacks = input.split('\n')

def priority(letter):
    #return (ord(letter)-91)%58-5
    if letter == letter.upper():
        return 26 + ord(letter) - ord('A') + 1
    else:
        return ord(letter) - ord('a') + 1

res1 = 0
for backpack in backpacks:
    n = len(backpack)
    comp1, comp2 = backpack[:n//2], backpack[n//2:]
    common = set(comp1).intersection(set(comp2)).pop()
    res1 += priority(common)
print(res1)

groups = []
for i in range(len(backpacks)//3):
    group = [backpacks[3*i], backpacks[3*i+1], backpacks[3*i+2]]
    groups.append(group)

res2 = 0
for group in groups:
    common = set(group[0]).intersection(group[1]).intersection(group[2]).pop()
    res2 += priority(common)
print(res2)