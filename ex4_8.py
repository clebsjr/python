op = int(input("Operações matemáticas:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha uma operação: "))

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if op == 1:
    resultado = n1 + n2
    print(f"{n1} + {n2} = {resultado}")
elif op == 2:
    resultado = n1 - n2
    print(f"{n1} - {n2} = {resultado}")
elif op == 3:
    resultado = n1 * n2
    print(f"{n1} * {n2} = {resultado}")
elif op == 4:
    resultado = n1 / n2
    print(f"{n1} / {n2} = {resultado}")