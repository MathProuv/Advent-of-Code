import inputAoC as aoc
from math import inf as infty

input = "16,1,2,0,4,2,7,1,2,14"
input = aoc.get_input_file(7,2021)
input = list(map(int,input.split(',')))

def fuel(liste,pos):
    return sum([abs(elem-pos) for elem in liste])
    res = 0
    for elem in liste:
        dist = abs(elem-pos)
        res += dist
    return res

def min_fuel(liste):
    return min([fuel(liste,pos) for pos in range(min(liste),max(liste)+1)])
    res = infty
    for pos in range(min(liste),max(liste)+1):
        res = min(res, fuel(liste,pos))
    return res

res1 = min_fuel(input)
print(res1)

def fuel(liste,pos):
    return sum([abs(elem-pos)*(abs(elem-pos)+1) for elem in liste])//2
    #return sum([abs(elem-pos)*-~abs(elem-pos) for elem in liste])//2 #(x+1) == -~x with ~ > * in order of operations
    res = 0
    for elem in liste:
        dist = abs(elem-pos)
        res += dist*(dist+1)//2
    return res

res2 = min_fuel(input)
print(res2)