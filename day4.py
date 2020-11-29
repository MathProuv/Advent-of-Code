file = "yzbqklnj"

import hashlib

compt = 0

while True:
	chaine = file + str(compt)
	result = hashlib.md5(chaine.encode())
	res = result.hexdigest()
	#print(hex(int("0x"+res,16)>>104), res)
	if not (int("0x"+res,16)>>104):
		break
	compt += 1

print(compt)
