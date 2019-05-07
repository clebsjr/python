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
L3 = L1[:]#L3 copia elementos de L1
L3.extend(L2)#L3 recebe elementos de L2
print(L3)
