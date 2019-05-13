#Exercício 6.12 - Verificação do menor valor
L = [1, 7, 2, 7]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)