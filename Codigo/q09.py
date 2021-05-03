n = int(input("Digite o numero de linhas: "))
for i in range(n):
  print(' ' * (n - i - 1) + "*" * (2 * i + 1))

for j in range(int(n/2)):
  print(' ' * int(n - n/4) + '*' * int(n/2))
