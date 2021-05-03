tupla = (1,3,4,7,8,14)
def funcao(tupla):
	li = list()
	a = int(len(tupla)/2)
	t1 = ()
	t2 = ()
	t1 += tupla[:a]
	t2 += tupla[a:]
	li.append(t1)
	li.append(t2)
	return li
print(funcao(tupla))
