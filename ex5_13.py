divida = float(input("Digite o valor da Dívida a ser paga: "))
taxa = float(input("Digite o valor da taxa,'10 para 10%': "))
pagamento = float(input("Digite o valor mensal a ser pago: "))
taxa /= 100
mes = 1 
if divida * taxa > pagamento:
    print("Você não poderá pagar sua dívida, pois o juros é maior que o pagamento mensal")
else:
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa
        saldo += juros - pagamento
        juros_pago += juros
        print(f"Mês {mes} - Saldo da Dívida R${saldo:5.2f}")
        mes += 1
    print(f"Sua dívida é de R${divida} com a taxa de {taxa:.2f}")
    print(f"Você precisará de {mes} mês/meses para pagar a dívida com a taxa de {juros_pago:.2f}")
    print(f"No último mês você ainda deverá R${saldo:5.2f}")