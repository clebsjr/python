cigarro = int(input("Digite quantos cigarros você fuma por dia: "))
tempo = int(input("Digite quantos anos você fuma: "))

dia = tempo*365

cigarro_por_dia = dia*cigarro

tempo_perdido = cigarro_por_dia*10

total_dias = tempo_perdido/1440


print(f"Se a pessoa fumar {cigarro} cigarros por dia em {tempo} anos, ela perderá {total_dias:.0f} dias de vida")
