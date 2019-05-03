deposito = float(input("Digite o valor do Depósito: "))
taxa = float(input("Digite o valor da taxa de juros: "))
investimento = float(input("Depósito mensal: "))
mes = 1
saldo = deposito
while mes <= 24:
    if mes == 1:
        saldo += (saldo * (taxa/100))
        print(f"Saldo de mês {mes} é de R${saldo:5.2f}")
        mes += 1
    else:
        saldo += (saldo * (taxa/100)) + investimento
        print(f"Saldo de mês {mes} é de R${saldo:5.2f}")
        mes += 1

print(f"Ganho total é de R${saldo:5.2f}")