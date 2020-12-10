import inputAoC as aoc

chargeurs = [0] + sorted([int(i) for i in aoc.get_input_file(10,2020).split("\n")])
chargeurs += [chargeurs[-1]+3]

diffs = []

for i in range(1,len(chargeurs)):
    diff = chargeurs[i] - chargeurs[i-1]
    diffs.append(diff)

res1 = diffs.count(1)*diffs.count(3)
print(res1)

can_be_del = [True]*len(chargeurs)
can_be_del[0] = can_be_del[-1] = False

for i in range(1, len(chargeurs)-1):
    if diffs[i] == 3 or diffs[i-1] == 3:
        can_be_del[i] = False
# for i in range(len(chargeurs)): print(chargeurs[i], can_be_del[i])

nb_diff1_consec = []
temp = 0
for i in range(len(can_be_del)):
    if can_be_del[i]:
        temp += 1
    else:
        if temp != 0:
            nb_diff1_consec.append(temp)
            temp = 0
# print(nb_diff1_consec)

possibilities = 1
for nb in nb_diff1_consec:
    # 3 - 4 - 5 ou 3 - 5
    if nb == 1:
        possibilities *= 2
    # 3-4-5-6 ou 3-4-6 ou 3-5-6 ou 3-6
    elif nb == 2:
        possibilities *= 4
    # 3-4-5-6-7  3-4-5-7  3-4-6-7  3-5-6-7  3-4-7  3-5-7  3-6-7
    elif nb == 3:
        possibilities *= 7
    # je sais que dans l'input, il n'y a pas plus de 3 diff1 d'affilée

res2 = possibilities
print(res2)
