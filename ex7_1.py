s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")
p = 0
print(f"1ª String: {s1}")
print(f"2ª String: {s2}")
while(p > -1):
    p = s1.find(s2, p)
    if p >= 0:
        print(f"Resultado: {s2} encontrado na posição {p} de {s1}")
        p += 1
    else:
        print(f"Resultado: {s2} não foi encontrado em {s1}")