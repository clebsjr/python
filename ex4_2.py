velocidade = int(input("Digite a velocidade do seu carro: "))
if velocidade <= 80:
    print("Você está dentro do limite de velocidade")
if velocidade > 80:
    multa = (velocidade-80) * 5
    print(f"Você ultrapassou o limite de velocidade, você pagará uma mulda de R${multa:5.2f}")