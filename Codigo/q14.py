L = [13,71,49,18,92]
a = len(L)
tupla = ([],)*a
for i in range(len(L)):
	tupla[i].append(L[i])
print(tupla)
