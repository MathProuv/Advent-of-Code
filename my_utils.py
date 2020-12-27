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

def agrandir_grid(grid, n=1):
    res = [0] * (len(grid) + 2*n)
    for z in range(len(res)):
        res[z] = [0] * (len(grid[0]) + 2*n)
        for y in range(len(res[z])):
            if n <= z < len(grid)+n and n <= y < len(grid[z-n])+n:
                res[z][y] = '.' * n + grid[z-n][y-n] + '.' * n
            else:
                res[z][y] = '.' * (len(grid[0][0]) + 2*n)
    return res
