print(l:=input(),list(min([i+n for i in range(len(l)) if len(set(l[i:i+n]))==n]) for n in[4,14]))
#print(l:=input(),list([len(set(l[i:i+n]))==n for i in range(len(l))].index(1)+n for n in [4,14]))