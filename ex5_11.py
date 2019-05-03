deposito = float(input("Digite o valor do Depósito: "))
taxa = float(input("Digite o valor da taxa de juros: "))
mes = 1
saldo = deposito
while mes <= 24:
    saldo += (saldo * (taxa/100))
    print(f"Saldo de mês {mes} é de R${saldo:5.2f}")
    mes += 1
print(f"Ganho total é de R${saldo-deposito:5.2f}")