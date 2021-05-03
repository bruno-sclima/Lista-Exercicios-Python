n = int(input("Digite um numero natural: "))
li = list()
for i in range(1,n+1,1):
  li.append((i,i*i,i*i*i))
print(li)
