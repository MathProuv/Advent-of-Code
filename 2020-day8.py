import inputAoC as aoc

instrs = aoc.get_input_file(8,2020).split("\n")

acc1 = 0
i1 = 0
indexes1 = []

while i1 not in indexes1:
    indexes1.append(i1)
    instr = instrs[i1].split(" ")
    if instr[0] == "acc":
        acc1 += int(instr[1])
        i1 += 1
    elif instr[0] == "jmp":
        i1 += int(instr[1])
    else: # instr[0] == "nop"
        i1 += 1

print(acc1)


def search_loop(etat) -> (bool,dict):
    acc = etat["acc"]
    i = etat["i"]
    indexes = [i for i in etat["indexes"]]
    try:
        while i not in indexes:
            indexes.append(i)
            instr = instrs[i].split(" ")
            if instr[0] == "acc":
                acc += int(instr[1])
                i += 1
            elif instr[0] == "jmp":
                i += int(instr[1])
            else: # instr[0] == "nop"
                i += 1
    except IndexError:
        return False, dict(acc=acc, i=i, indexes=indexes)
    return True, 0


etat = dict(acc=0,i=0,indexes=[])
while True:
    etat["indexes"].append(etat["i"])
    instr = instrs[etat["i"]].split()
    if instr[0] == "acc":
        etat["acc"] += int(instr[1])
        etat["i"] += 1
    elif instr[0] == "jmp":
        etatBis = dict(acc=etat["acc"], i=etat["i"]+1, indexes=etat["indexes"])
        is_loop, etat2 = search_loop(etatBis)
        if is_loop:
            etat["i"] += int(instr[1])
        else:
            etat = etat2
            break
    else: #elif instr[0] == "nop":
        etatBis = dict(acc=etat["acc"], i=etat["i"]+int(instr[1]), indexes=etat["indexes"])
        is_loop, etat2 = search_loop(etatBis)
        if is_loop:
            etat["i"] += 1
        else:
            etat = etat2
            break
    #print(dict(acc=etat["acc"], i=etat["i"]))

print(etat["acc"])