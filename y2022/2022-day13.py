import inputAoC as aoc
from functools import cmp_to_key

input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
input = aoc.get_input_file(13,2022)

def compare(item1,item2) -> int:
    """ returns:
    -1 if item1 < item2 (right order)
    0 if item1 == item2
    +1 if item1 > item2 (wrong order)"""
    if type(item1) is type(item2):
        if type(item1) is int:
            if item1 == item2: return 0
            else: return (item1-item2)/abs(item1-item2)
        elif type(item1) is list:
            i = 0
            while len(item1) > i < len(item2):
                comp = compare(item1[i],item2[i])
                if comp: return comp
                i += 1
            return compare(len(item1),len(item2))
        else: raise TypeError()
    else:
        if type(item1) is int and type(item2) is list:
            return compare([item1],item2)
        elif type(item1) is list and type(item2) is int:
            return compare(item1,[item2])
        else: raise TypeError()

div1, div2, zero = [[2]],[[6]],[]
packets = [div2,div1] + list(map(eval,input.replace('\n\n','\n').splitlines())) + [zero]
# [div2,div1] at the begining is helpful for res1 indexes to start at 1
# zero at the end is helpful for res2 indexes to start at 1 while not changing res1
res1 = 0
for i in range(len(packets)//2):
    if compare(packets[2*i],packets[2*i+1]) < 0: res1 += i
print(res1)

packets.sort(key=cmp_to_key(compare))
print(res2 := packets.index(div1) * packets.index(div2))
