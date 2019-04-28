kwh = int(input("Digite a quantidade de kWh consumida: "))
tipo = input("Digite o tipo de Instalação\nR - residências\nI - indústrias\nC - comércios")

if tipo == "R":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "I":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Digite uma opção válida!")

print(f"kWh consumido: {kwh}\nValor a pagar: R${kwh*preco:6.2f}")