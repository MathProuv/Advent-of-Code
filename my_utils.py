def print_dict(dict):
    for key, value in dict.items():
        print(key, ":", value)
    print()

def print_matrice(matrice):
    for line in matrice:
        print(line)
    print()

def rindex(liste, elem):
    if elem not in liste:
        return -1
    for i in range(len(liste)-1,-1,-1):
        if liste[i] == elem:
            return i

def bin_n(number, n):
    """Renvoie la string de number en binaire de taille n"""
    res = bin(number)[2:]
    res = '0'*(n-len(res)) + res
    return res
