L = ['jdke','kjs','jose','1241','1331','joaozinho']
cont = 0
for i in L:
	if len(i)>=2:
		for j in L:
			if i !=j:
				if i[0] == j[0] and i[len(i)-1] == j[len(j)-1]:
					cont = cont +1
print("exercicio_4(lista) = %d" % cont)
