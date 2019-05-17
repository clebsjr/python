s1 = input("Digite uma string: ")
cont = {}
for letra in s1:
    if letra in cont:
        cont[letra]+=1
    else:
        cont[letra]=1

for chave in cont:
    print(f"{chave}: {cont[chave]}x")