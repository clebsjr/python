distancia = float(input("Digite a distância de KM que você irá viajar: "))

if distancia <= 200:
    precoKM = 0.50
    viagem = distancia * precoKM
else:
    precoKM = 0.45
    viagem = distancia * precoKM
print(f"Distância: {distancia}km\nPreço por KM: R${precoKM:5.2f}\nO preço da passagem é R${viagem:5.2f}")