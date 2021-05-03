n = int (input("Digite o numero de linhas: "))
j = n
while j > 0:
    print(' '* (n - j - 1)+ "*"*(2*j +1))
    j= j -1
