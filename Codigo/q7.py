n = int (input("Digite o numero de linhas: "))
for i in range(n):
  print(' ' * (n - i - 1) + "*" * (2 * i + 1))


