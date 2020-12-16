import inputAoC as aoc

instrs = aoc.get_input_file(7,2015).split("\n")

def __and__ (x, y): return x & y
def __or__ (x, y): return x | y
def __lshift__ (x, y): return x << y
def __rshift__ (x, y): return x >> y
def __not__ (x): return ~ x

gates = [("AND", "OR", "LSHIFT", "RSHIFT", "NOT"), 
        (__and__, __or__, __lshift__, __rshift__, __not__)]

wires = {}
        
for instr in instrs:
    
    pass