import inputAoC as aoc
import re

input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
input = aoc.get_input_file(4,2022)
pairs = input.split('\n')

res1 = 0
res2 = 0
for pair in pairs:
    # two splits
    i1, i2 = pair.split(',')
    left1, right1 = map(int, i1.split('-'))
    left2, right2 = map(int, i2.split('-'))
    # one split
    left1, right1, left2, right2 = map(int, pair.replace(",", "-").split("-"))
    # regex match find all digits
    left1, right1, left2, right2 = map(int, re.findall("[0-9]+", pair))
    # regex match exactly
    left1, right1, left2, right2 = map(int, re.match("(\d+)-(\d+),(\d+)-(\d+)", pair).groups())

    res1 += left2 <= left1 and right1 <= right2 or left1 <= left2 and right2 <= right1
    res2 += left2 <= right1 and left1 <= right2
    #       not(right1 < left2 or right2 < left1)
print(res1)
print(res2)
