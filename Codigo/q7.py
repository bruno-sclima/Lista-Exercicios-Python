n = int (input("Digite o numero de linhas: "))
for i in range(n):
  print(' ' * (n - i - 1) + "*" * (2 * i + 1))

n = int (input("Digite o numero de linhas: "))
j = n
while j > 0:
    print(' '* (n - j - 1)+ "*"*(2*j +1))
    j= j -1
