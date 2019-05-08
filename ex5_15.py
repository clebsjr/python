compra = 0
while True:
    produto = int(input("Digite o código do produto: "))
    if produto == 1:
        valor = 0.50
    elif produto == 2:
        valor = 1.00
    elif produto == 3:
        valor = 4.00
    elif produto == 5:
        valor = 7.00
    elif produto == 9:
        valor = 8.00
    elif produto == 0:
        break
    else:
        print("Código inválido")
    quant = int(input("Digita a quantidade: "))
    compra += quant * valor
print(f"Valor total da compra: R${compra:5.2f}")
        