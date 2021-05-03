lc = [(1.0,4.06),(1.0,0.24),(2.0,8.12),(2.0,0.49),(100.0,406),(100.0,24.63)]
def funcao(li):
	cont =0
	cotacao1=""
	cotacao2=""
	cotacao=""
	for i in li:
		if cont%2==0:
			cotacao1 = " US$= "+ str(i[0]) + "   R$="+ str(i[1])
		else:
			cotacao2 = "  R$="+ str(i[0]) + "  US$="+str(i[1])+" \n "
		cotacao = cotacao+cotacao1+cotacao2	
		cont+=1
	return cotacao		
print(funcao(lc))
