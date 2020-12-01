file = open("2015-day5.txt", "r")

compt = 0

def check1(s):
	if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
		return False
	if s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") < 3 :
		return False
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			return True
	return False

def check(s):
	paire, sandwitch = False, False
	for i in range(len(s)-2):
		if not sandwitch and s[i] == s[i+2]:
			sandwitch = True
		if not paire and s[i:i+2] in s[i+2:]:
			paire = True
	return sandwitch and paire

for line in file:
	compt += check(line)

file.close()

print(compt)