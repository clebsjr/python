T = [-10, -8, 0, 1, 2, 5, -2, -4]
maximo = T[0]
minimo = T[0]
media = 0
for e in T:
    if e > maximo:
        maximo = e
    elif e < minimo:
        minimo = e
    media += e
print(f"Maior temperatura: {maximo}°C")
print(f"Menor temperatura: {minimo}°C")
print(f"Temperatura média: {media/len(T)}°C")