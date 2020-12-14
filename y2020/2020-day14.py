import inputAoC as aoc
import my_utils
from collections import deque

instrs = [instr.split(" = ") for instr in aoc.get_input_file(14,2020).split("\n")]
# my_utils.print_matrice(instrs)

def bin_n(val, n):
    """ Returns the string of val written in binary of size n"""
    res = bin(val)[2:]
    return "0" * (n-len(res)) + res

def masked1(mask, val):
    n = len(mask)
    result = ""
    value = bin_n(val, n)
    for i in range(n):
        m = mask[i]
        if m == 'X':
            result += value[i]
        else:
            result += m
    return int(result,2)

def masked2(mask, adress):
    n = len(mask)
    result = ""
    index = bin_n(adress, n)
    for i in range(n):
        m = mask[i]
        if m == '0':
            result += index[i]
        else:
            result += m
    res = replaceX(result)
    return res

def replaceX(result):
    res = []
    stack = [result] #deque([result])
    while stack:
        string = stack.pop()
        if string.count("X") >= 1:
            stack.extend(replace1X(string))
        else:
            res.append(string)
            res.append(stack.pop())
    return res

def replace1X(string):
    return [string.replace("X","0",1), string.replace("X","1",1)]

def write_mem(mem, index, val):
    mem[index] = val

def traiter(instrs, tour: int):
    """ Traite les instructions \n
    tour == 1 => masked = masked1(mask,val); 
    tour == 2 => masked = masked2(mask,adress) (default)"""
    mem = {}
    if tour == 1: vide = "X"
    else: vide = "0"
    mask = vide * 36

    for instr in instrs:
        if instr[0] == "mask":
            mask = instr[1]
        else:
            val = int(instr[1])
            adress = int(instr[0][4:-1]) #[len("mem["):-len("]")]
            if tour == 1:
                val = masked1(mask, val)
                adresses = [adress]
            else:
                adresses = masked2(mask, adress)
            for adress in adresses:
                write_mem(mem, adress, val)
    return sum(mem.values())

res1 = traiter(instrs, 1)
print(res1)

res2 = traiter(instrs, 2)
print(res2)