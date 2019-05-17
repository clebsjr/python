# Programa 6.22 - Exemplo de dicionário com estoque de operações de venda
# Exercício 6.17
estoque = {"tomate": [1000, 2.30],
            "alface": [500, 0.45],
            "batata": [2001, 1.20],
            "feijão": [100, 1.50]}
total = 0
while True:
    produto = input("Digite o produto, (fim para terminar): ")
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}\n")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade indisponível!")   
    else:
        print("Produto não encontrado!!")
print(f" Custo total: {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")