import re
s,b=[[]for _ in range(9)],1
for l in open(0):
	if l=='\n':b,t=0,[s[i].copy()for i in range(9)]
	elif b: 
		for i in range(9):
			if l[4*i+1]!=' ':s[i].insert(0,l[4*i+1])
	else:
		n,x,y=map(int,re.findall('\d+',l))
		z=[]
		for _ in range(n):
			s[y-1].append(s[x-1].pop())
			z.append(t[x-1].pop())
		t[y-1].extend(z[::-1])
def r(s):return "".join([s[i][-1]for i in range(9)])
print(r(s),r(t))