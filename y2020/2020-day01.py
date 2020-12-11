import inputAoC

file = inputAoC.get_input(1, 2020)

x = list(map(int, file.split("\n")))

for nb1 in x:
    nb2 = 2020-nb1
    if nb2 in x:
        print(nb1*nb2)
        break

for i in range(len(x)):
    nb1 = x[i]
    objectif = 2020-nb1
    for j in range(i+1, len(x)):
        nb2 = x[j]
        nb3 = objectif - nb2
        if nb3 in x[j+1:]:
            print(nb1*nb2*nb3) # nb1, nb2, nb3
