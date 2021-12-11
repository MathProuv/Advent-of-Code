import inputAoC as aoc
from math import inf as infty

input = """e => H
e => O
H => HO
H => OH
O => HH

HOH"""
input = aoc.get_input_file(19,2015)

replacements, molecule = input.split('\n\n')
replacements = [repl.split(' => ') for repl in replacements.splitlines()]
def get_repls(replacements):
    repls = {}
    for repl in replacements:
        repl0,repl1 = repl
        if repl0 in repls.keys():
            repls[repl0].append(repl1)
        else:
            repls[repl0] = [repl1]
    return repls
repls = get_repls(replacements)
#print(repls)

def get_atoms(molecule):
    res = []
    temp = ''
    for i in range(len(molecule)):
        carac = molecule[i]
        if not('a' <= carac <= 'z') and temp:
            res.append(temp)
            temp = ''
        temp += carac
    res.append(temp)
    return res
def get_molecule(atoms):
    return "".join(atoms)


def step(molecule, repls):
    atoms = get_atoms(molecule)
    #print(atoms)
    possibilities = set()
    for i in range(len(atoms)):
        atom = atoms[i]
        if atom in repls.keys():
            for cand in repls[atom]:
                poss = ""
                for j in range(len(atoms)):
                    if j==i: poss+= cand
                    else: poss += atoms[j]
                #poss = "".join(atoms[:i]+[cand]+atoms[i+1:])
                #print(poss)
                possibilities.add(poss)
    #print(possibilities)
    return possibilities

res1 = len(step("H2OrO",{"H":["OO"]}))
res1 = len(step(molecule,repls))
print(res1)

#print(repls)

def create_atoms(atoms,repls):
    return create(get_molecule(atoms),repls)

def create(molecule, repls):
    ln = len(get_atoms(molecule))
    possibilities = set()
    possibilities.add("e")
    n = 0
    while molecule not in possibilities and n <= ln:
        #print(possibilities)
        n += 1
        new_possibilities = set()
        for poss in possibilities:
            #print(poss,step(poss))
            for new_poss in step(poss,repls):
                if len(get_atoms(new_poss)) < ln:
                    new_possibilities.add(new_poss)
        print(n)
        #print(new_possibilities)
        possibilities = new_possibilities
    return n

#molecule = "HOHOHO"
#res2 = create(molecule, repls)
#print(res2)

# 180 < res2 < 293

def include(lit_list, big_list):
    petit, grand = len(lit_list), len(big_list)
    for deb in range(grand-petit+1):
        if big_list[deb:deb+petit] == lit_list:
            return deb
    return -1

def decompose(molecule,repls):
    return decompose_atoms(get_atoms(molecule),repls)

def decompose_atoms(atoms,repls):
    # on ne peut former "CaCaCa" que par "CaCa" avec Ca=>CaCa
    deb = include(['Ca','Ca','Ca'],atoms)
    if deb >= 0:
        return 1 + decompose_atoms(atoms[:deb+1]+atoms[deb+2:],repls)
    # on ne peut former "CaCa" au début que par "Ca" avec Ca=>CaCa
    deb = include(['Ca','Ca'],atoms)
    if deb == 0:
        return 1 + decompose_atoms(atoms[1:],repls)
    # 
    assert ("Ar" not in repls.keys())
    if "Ar" in atoms and atoms.index("Ar") != len(atoms)-1:
        idx = atoms.index("Ar")
        return decompose_atoms(atoms[:idx+1],repls) + decompose_atoms(atoms[idx+1:],repls)
    print(atoms)
    return create_atoms(atoms,repls)

def reduce_atoms(atoms,repls):
    # on cut après les Ar
    assert ("Ar" not in repls.keys())
    res = []
    while "Ar" in atoms and atoms.index("Ar") != len(atoms)-1:
        idx = atoms.index("Ar")
        res.append(atoms[:idx+1])
        atoms = atoms[idx+1:]
    res.append(atoms)
    return res

def create_atoms(atoms,repls):
    return

res2 = decompose(molecule, repls)
print(res2)
print("2nd star pas résolue")