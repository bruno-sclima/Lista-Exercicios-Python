L = [0,1,2,3,14,7]
menor = 0
maior = 0
menor_maior = (menor,maior)
if len(L) == 0:
	menor_maior = (None,None)
for i in L:
	if i > maior:
		maior = i
	if i < menor:
		menor = i	
menor_maior = (menor,maior)
print(menor_maior)
