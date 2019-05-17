s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")
s3 = ""

for letra in s1:
    if letra not in s2:
        s3 += letra
if s3 == "":
    print("Todos caracteres removidos")
else:
    print(f"Resultado: {s3}")