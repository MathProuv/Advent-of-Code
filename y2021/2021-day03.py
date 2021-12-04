import inputAoC as aoc

numbers = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()
numbers = aoc.get_input_file(3,2021).splitlines()
n = len(numbers)
m = len(numbers[0])

#print(input)

gamma_bin = ""
epsilon_bin = ""
for bit in range(m):
    compt1 = 0
    for number in numbers:
        if number[bit] == '1' : compt1 += 1
    if compt1 > n/2: 
        gamma_bin += '1'
        epsilon_bin += '0'
    else :
        gamma_bin += '0'
        epsilon_bin += '1'

gamma = int(gamma_bin,2)
epsilon = int(epsilon_bin,2)
#print(gamma, epsilon)
res1 = gamma * epsilon
print(res1)


o2 = numbers[:]
for bit in range(m):
    compt1 = 0
    for number in o2:
        if number[bit] == '1': compt1 += 1
    compt0 = len(o2) - compt1
    if compt1 >= compt0 : most = '1'
    else : most = '0'
    candidates = []
    for number in o2:
        if number[bit] == most: candidates.append(number)
    o2 = candidates[:]
o2_rate = int(o2[0],2)
#print(o2_rate)

co2 = numbers[:]
for bit in range(m):
    compt1 = 0
    for number in co2: 
        if number[bit] == '1': compt1 += 1
    compt0 = len(co2) - compt1
    if compt1 >= compt0 : least = '0'
    else : least = '1'
    candidates = []
    for number in co2:
        if number[bit] == least: candidates.append(number)
    co2 = candidates[:]
    if len(co2) == 1: break
co2_rate = int(co2[0],2)
#print(co2_rate)

res2 = o2_rate * co2_rate
print(res2)