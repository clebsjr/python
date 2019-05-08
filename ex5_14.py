soma = 0
x = 0
while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    soma += n
    x += 1
print(f"A soma dos números é {soma}")
print(f"A média aritmética é {soma/x:.2f}")