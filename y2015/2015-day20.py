import inputAoC as aoc
from math import sqrt as lsqrt

input = int(aoc.get_input_file(20,2015))

def facteurs(x):
    """facteurs(n): décomposition d'un nombre entier n en facteurs premiers"""
    F = set()
    F.add(1)
    for i in range(1, x + 1):
        if x % i == 0:
            F.add(i)
    return F

def house(n):
    F = facteurs(n)
    return sum(F)*10

def ex(N):
    for n in range(1,N+1):
        print("House", n, "receives", house(n), "gifts")

#ex(10)

def first_house(N):
    N = N//10
    houses = [0] * N
    for elf in range(1,N+1):
        #print(elf)
        for house in range(N//elf):
            houses[elf*house] += 10*elf
    N = N*10
    for i in range(1,len(houses)):
        if houses[i]>=N: return i

res1 = first_house(input)
print(res1)

def first_house2(N):
    N2 = N
    N = N//11
    houses = [0] * N
    for elf in range(1,N+1):
        #print(elf)
        for house in range(min(N//elf,50)):
            houses[elf*house] += 11*elf
    N = N2
    for i in range(1,len(houses)):
        if houses[i]>=N: return i

res2 = first_house2(input)
print(res2)