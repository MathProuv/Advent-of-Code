import inputAoC as aoc
from math import prod

def gt(liste): return int(liste[0] > liste[1])
def lt(liste): return int(liste[0] < liste[1])
def eq(liste): return int(liste[0] == liste[1])
operators_dict = [sum,prod,min,max,None,gt,lt,eq]

def get_reste(input):
    input += '0'
    res = ''
    for c in input: 
        ccc = bin(int(c,16))[2:]
        while len(ccc) < 4: ccc = '0' + ccc
        res += ccc
    return res

def version_type_reste(input):
    return int(input[:3],2),int(input[3:6],2),input[6:]
    vvv, ttt = input[:3], input[3:6]
    v, t = int(vvv,2), int(ttt,2)
    reste = input[6:]
    return v,t,reste

def literal(reste):
    res = ''
    while reste and reste[0] == '1':
        res += reste[1:5]
        reste = reste[5:]
    res += reste[1:5]
    reste = reste[5:]
    return int(res,2), reste

def not_literal(t,reste):
    i = int(reste[0])
    reste = reste[1:]
    paquets_res = []
    if i == 0:
        l = int(reste[:15],2)
        paquet = reste[15:15+l]
        paquets_res += read_paquet(paquet)[0]
        reste = reste[15+l:]
    else: #i == 1
        l = int(reste[:11],2)
        reste = reste[11:]
        while len(paquets_res) < l:
            paquet,reste = read_first_paquet(reste)
            paquets_res.append(paquet)
    paquets_res.insert(0,operators_dict[t])
    return paquets_res, reste

def read_first_paquet(reste):
    v,t,reste = int(reste[:3],2), int(reste[3:6],2), reste[6:]
    #print(v,t,reste)
    versions.append(v)
    if t == 4:
        return literal(reste)
    else:
        return not_literal(t,reste)

def read_paquet(reste):
    paquets_res = []
    while '1' in reste:
        paquets, reste = read_first_paquet(reste)
        paquets_res.append(paquets)
    return paquets_res, reste


def eval(paquets_res):
    if isinstance(paquets_res,int):
        return paquets_res
    else:
        operator = paquets_res.pop(0)
        return operator([eval(paquet) for paquet in paquets_res])

##############################

exemple = True
dem1 = "D2FE28" #-> 2021, v=1
dem2 = "38006F45291200" #-> (10,20), vs = 1+(6+2) = 8
dem3 = "EE00D40C823060" #-> (1,2,3), vs = 7+(v+v+v)
ex1 = "8A004A801A8002F478" #-> (((15))), vs = 4+(1+(5+(6))) = 23
ex2 = "620080001611562C8802118E34" #-> ((l,l),(l,l))
ex3 = "C0015000016115A2E0802F182340" #-> ((l,l),(l,l))
ex4 = "A0016C880162017C3686B18A3D4780" # -> (((l,l,l,l)))

ex21 = "C200B40A82" #3
ex22 = "04005AC33890" #54
ex23 = "880086C3E88112" #7
ex24 = "CE00C43D881120" #9
ex25 = "D8005AC2A8F0" #1
ex26 = "F600BC2D8F" #0
ex27 = "9C005AC2F8F0" #0
ex28 = "9C0141080250320F1802104A08" #1

input = ex4
input,exemple = aoc.get_input_file(16,2021),False

input = get_reste(input)
if exemple: print(input)

versions = []
to_eval = read_paquet(input)[0].pop()

res1 = sum(versions)
print("res1 =", res1)
if exemple:
    print("versions =",versions)
    print("to_eval =",to_eval)

res2 = eval(to_eval)
print("res2 =",res2)