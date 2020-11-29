file = open("day5.txt", "r")

compt = 0

def check(s):
	if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
		return False
	if s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") < 3 :
		return False
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			return True
	return False

for line in file:
	compt += check(line)

file.close()

print(compt)