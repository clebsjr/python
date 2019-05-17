s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")
s3 = input("Digite a terceira string: ")

if len(s2) == len(s3):
    resultado = ""
    for letra in s1:
        posicao = s2.find(letra)
        if posicao != -1:
            resultado += s3[posicao]
        else:
            resultado += letra        
    if resultado == "":
        print("Nenhuma substituição feita")
    else:
        print(f"Resultado: {resultado}")
else:
    print("Erro, a segunda e terceira string deve conter o mesmo tamanho.")