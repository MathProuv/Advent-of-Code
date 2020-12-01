file = open("day2.txt", "r")

res1 = 0
res2 = 0

for line in file:
	x = sorted([int(i) for i in line.split("x")])
	res1 += 3*x[0]*x[1] + 2*x[0]*x[2] + 2*x[1]*x[2]
	res2 += 2*x[0] + 2*x[1] + x[0]*x[1]*x[2]

file.close()

print(res1, res2)