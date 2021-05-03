L = [(7,8,9),(5,6),(10,11,12,13)]
n = 19
def funcao(l,n):
	li = list()
	t1 = ()
	t2 = (n,)
	for j in  l:
		for i in range(len(j)):
			if i !=len(j)-1:
				t1 +=j[i:i+1]
			else:
				t1 += t2	
		li.append(t1)
		t1 = ()
	return li
print(funcao(L,n))
