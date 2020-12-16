

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

