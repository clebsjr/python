print("Aprovação de crédito para compra de imóvel")
valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu sálario: "))
ano = int(input("Digite a quantidade de anos a pagar: "))

meses = ano*12

parcela = valor_casa / meses

salario_30 = salario*0.3 #Calcula 30% do salário

if parcela <= salario_30:
    print(f"Valor da Casa: R${valor_casa:6.2f}\nNúmero de parcelas: {meses}\nValor de cada parcela: R${parcela:6.2f}\nSeu crédito foi Aprovado pois o valor da parcela é menor que 30% do seu salário.")
else:
    print(f"Valor da Casa: R${valor_casa:6.2f}\nNúmero de parcelas: {meses}\nValor de cada parcela: R${parcela:6.2f}\nSeu crédito foi Negado pois o valor da parcela é maior que 30% do seu salário.")