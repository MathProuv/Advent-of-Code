import inputAoC as aoc

start = aoc.get_input_file(10,2015)

print(start)

def look_and_say(string):
    res = ""
    n = len(string)
    indice = 0
    while indice < n:
        carac = string[indice]
        compt = 1
        while indice+compt < n and string[indice+compt] == carac:
            compt += 1
        res += str(compt) + carac
        indice += compt
    return res

    """# Fonction itérative, avec une réécriture de string
    res = ""
    while string:
        carac = string[0]
        n = len(string)
        compt = 1
        while compt < n and string[compt] == carac:
            compt += 1
        res += str(compt) + carac
        string = string[compt:]
    return res"""
    
    """# Fonction récursive:
    if not string:
        return ""
    n = len(string)
    carac = string[0]
    compt = 1
    while compt < n and string[compt] == carac:
        compt += 1
    res = str(compt) + carac
    return res + look_and_say(string[compt:])"""

#print(look_and_say(start))

res1 = start
for i in range(40):
    print(i)
    res1 = look_and_say(res1)

print(len(res1))

res2 = res1
for i in range(40,50):
    print(i)
    res2 = look_and_say(res2)
print(len(res2))