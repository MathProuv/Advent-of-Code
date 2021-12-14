from os import replace
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
atoms = get_atoms(molecule)

def get_repls(replacements):
    repls = {}
    for repl in replacements:
        repl0,repl1 = repl
        if repl0 in repls.keys():
            repls[repl0].append(repl1)
        else:
            repls[repl0] = [repl1]
    return repls
def get_repls_atoms(replacements):
    res = {}
    for repl in replacements:
        repl0,repl1 = repl
        if repl0 in res.keys():
            res[repl0].append(get_atoms(repl1))
        else:
            res[repl0] = [get_atoms(repl1)]
    return res
repls = get_repls(replacements)
repls_atoms = get_repls_atoms(replacements)
print(repls_atoms)


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

print(repls)
print(repls_atoms)
#print(atoms)

