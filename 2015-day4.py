import inputAoC

file = inputAoC.get_input_file(4,2015)

import hashlib

compt = 0

while True:
	chaine = file + str(compt)
	result = hashlib.md5(chaine.encode())
	res = result.hexdigest()
	if not (int("0x"+res,16)>>104): #108 pour 5
		break
	compt += 1

print(compt)
