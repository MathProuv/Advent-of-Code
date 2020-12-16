import inputAoC as aoc
import my_utils

def bin16(nb):
    return my_utils.bin_n(nb,16)

def _and_ (args): 
    x, y = bin16(args[0]), bin16(args[1])
    res = ""
    for i in range(16):
        res += '1' if x[i]=='1' and y[i]=='1' else '0'
    return int(res,2)
def _or_ (args):
    x, y = bin16(args[0]), bin16(args[1])
    res = ""
    for i in range(16):
        res += '1' if x[i]=='1' or y[i]=='1' else '0'
    return int(res,2)
def _lshift_ (args): 
    x, y = args[0], args[1] 
    return x << y
def _rshift_ (args): 
    x, y = args[0], args[1]
    return x >> y
def _not_ (args): 
    x = bin16(args[0])
    res = ''
    for i in range(16):
        res += '0' if x[i] == '1' else '1'
    return int(res,2)

GATES = dict()
GATES["AND"] = _and_
GATES["OR"] = _or_
GATES["LSHIFT"] = _lshift_
GATES["RSHIFT"] = _rshift_
GATES["NOT"] = _not_


def get_value(expr, values, fcts=GATES):
    if expr.isnumeric():
        return int(expr)
    args = []
    fct = None
    for word in expr.split():
        if word in fcts:
            fct = fcts[word]
        elif word in values:
            args.append(values[word])
        elif word.isnumeric():
            args.append(int(word))
        else:
            return None
    if fct:
        return fct(args)
    else:
        return args[0]

def get_wire(instrs, wire):
    values = dict()
    instrs = instrs[::]
    repeat = True
    while repeat:
        repeat = False
        for instr in instrs:
            i = instr.index(" -> ")
            expr, value = instr[:i], instr[i+4:] #len(" -> ")
            # print(expr, value)
            val = get_value(expr,values)
            if val != None:
                values[value] = val
                instrs.remove(instr)
                repeat = True
    # my_utils.print_dict(values)

    return values[wire]

instrs = aoc.get_input_file(7,2015).splitlines()

res1 = get_wire(instrs, 'a')
print(res1)

res_b = get_wire(instrs,"b")
instrs.remove(str(res_b) + " -> b")
instrs.append(str(res1) + " -> b")

res2 = get_wire(instrs, 'a')
print(res2)