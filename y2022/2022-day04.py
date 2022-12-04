import inputAoC as aoc

input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
input = aoc.get_input_file(4,2022)
pairs = [pair.split(',') for pair in input.split('\n')]

res1 = 0
res2 = 0
for i1, i2 in pairs:
    left1, right1 = map(int, i1.split('-'))
    left2, right2 = map(int, i2.split('-'))
    if left2 <= left1 and right1 <= right2 or left1 <= left2 and right2 <= right1:
        res1 += 1
    #if not(right1 < left2 or right2 < left1):
    if left2 <= right1 and left1 <= right2:
        res2 += 1
print(res1)
print(res2)
