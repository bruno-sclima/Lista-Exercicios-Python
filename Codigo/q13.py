tupla = (1,3,4,7,8,14)
def funcao(tupla):
	li = list()
	par = list()
	impar = list()
	for i in range(len(tupla)):
		if tupla[i]%2==0:
			par.append(tupla[i])
		else:
			impar.append(tupla[i])	
	t1 = ()
	t2 = ()
	t1 = tuple(par)
	t2 = tuple(impar)
	li.append(t1)
	li.append(t2)
	return li
print(funcao(tupla))
