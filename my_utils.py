def print_dict(dictionaire: dict) -> None:
    for key, value in dictionaire.items():
        print(key, ":", value)
    print()

def print_list(liste: list) -> None:
    for line in liste:
        print(line)
    print()

def rindex(liste: list, elem) -> int:
    if elem not in liste:
        return -1
    for i in range(len(liste)-1,-1,-1):
        if liste[i] == elem:
            return i

def bin_n(number: int, n: int) -> str:
    """Renvoie la string de number en binaire de taille n"""
    res = bin(number)[2:]
    res = '0'*(n-len(res)) + res
    return res
