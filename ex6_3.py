L1 = []
L2 = []
x = 0
#Adiciona 3 elementos na lista L1
while x < 3:
    n = int(input(f"Número {x + 1} da lista 1: "))
    L1.append(n)
    x += 1
x = 0
print("-"*15)
#Adiciona 3 elementos na lista L2
while x < 3:
    n = int(input(f"Número {x + 1} da lista 2: "))
    L2.append(n)
    x += 1

L3 = []
lista = L1[:]#lista copia elementos de L1
lista.extend(L2)#lista recebe elementos de L2

i = 0
while i < len(lista):
    z = 0
    while z < len(L3):
        if lista[i] == L3[z]:
            break
        z += 1
    if z == len(L3):
        L3.append(lista[i])
    i += 1
print(L3)


