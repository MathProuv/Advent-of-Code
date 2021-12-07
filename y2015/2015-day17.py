import inputAoC as aoc

combien, input = 150, aoc.get_input_file(17,2015)
#combien, input = 25, "20\n15\n10\n5\n5"
input = list(map(int,input.splitlines()))

def resultats(combien,nombres):
    lens = []
    for i in range(2**len(nombres)):
        x = bin(i)[2:] #pour enlever le '0b' du début
        x = '0'*(len(nombres)-len(x)) + x #pour remettre les 0 non significatifs
        somme = 0
        for i in range(len(nombres)):
            if x[i]=='1': somme += nombres[i]
        if somme == combien: 
            lens.append(sum([int(b) for b in x]))
    res1 = len(lens)
    res2 = lens.count(min(lens))
    return res1,res2

res1,res2 = resultats(combien,input)
print(res1,res2)