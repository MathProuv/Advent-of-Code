import inputAoC as aoc

ex = """199
200
208
210
200
207
240
269
260
263
"""
depths = [int(i) for i in ex.splitlines()]
depths = [int(i) for i in aoc.get_input_file(1,2021).splitlines()]
n = len(depths)
#print(depths, n)

res1 = 0
old = depths[0]
for i in range(0,n-1):
    new = depths[i+1]
    res1 += new > old
    old = new
print(res1)

res2 = 0
old = sum(depths[0:3])
for i in range(0, n-3):
    new = old - depths[i] + depths[i+3]
    res2 += new > old
    old = new
print(res2)
