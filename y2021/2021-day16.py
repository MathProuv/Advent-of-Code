import inputAoC as aoc

operators_dict = ["sum","product","min","max",None,"gt","lt","eq"]

def get_reste(input):
    input += '0'
    res = ''
    for c in input: 
        ccc = bin(int(c,16))[2:]
        while len(ccc) < 4: ccc = '0' + ccc
        res += ccc
    return res

def vtr(input):
    vvv, ttt = input[:3], input[3:6]
    v, t = int(vvv,2), int(ttt,2)
    reste = input[6:]
    return v,t,reste

def literal(reste):
    res = ''
    while reste and reste[0] == '1':
        res += reste[1:5]
        reste = reste[5:]
    if reste and reste[0] == '0':
        res += reste[1:5]
        reste = reste[5:]
    return int(res,2), reste

def not_literal(t,reste): #paquet
    operators.append(operators_dict[t])
    i = int(reste[0],2)
    reste = reste[1:]
    res = ''
    if i == 0:
        l = int(reste[:15],2)
        paquet = reste[15:15+l]
        res = read_paquet(paquet)[0]
        reste = reste[15+l:]
    else: #i == 1
        l = int(reste[:11],2)
        reste = reste[11:]
        paquets = []
        while len(paquets) < l:
            paquet,reste = read_first_paquet(reste)
            paquets.append(paquet)
        res = paquets
    return res, reste

def read_first_paquet(reste):
    v,t,reste = vtr(reste)
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

#########################""

dem1 = "D2FE28" #-> 2021, v=1
dem2 = "38006F45291200" #-> (10,20), vs = 1+(6+2) = 8
dem3 = "EE00D40C823060" #-> (1,2,3), vs = 7+(v+v+v)
ex1 = "8A004A801A8002F478" #-> (((15))), vs = 4+(1+(5+(6))) = 23
ex2 = "620080001611562C8802118E34" #-> ((l,l),(l,l))
ex3 = "C0015000016115A2E0802F182340" #-> ((l,l),(l,l))
ex4 = "A0016C880162017C3686B18A3D4780" # ->

ex21 = "C200B40A82" #
ex22 = "04005AC33890" #
ex23 = "880086C3E88112" #
ex24 = "CE00C43D881120" #
ex25 = "D8005AC2A8F0" #
ex26 = "F600BC2D8F" #
ex27 = "9C005AC2F8F0" #
ex28 = "9C0141080250320F1802104A08" #

input = ex4
input = aoc.get_input_file(16,2021)

input = get_reste(input)
#print(input)

versions = []
operators = []
to_eval = read_paquet(input)[0]
res1 = sum(versions)
print("res1 =", res1)
print("versions =",versions)
print("to_eval =",to_eval)
print("operators =", operators)