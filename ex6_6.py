#Simulação de um fila de banco 2
ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1")
    print(f"Fila 1 atual {fila1}")
    print(f"\nExistem {len(fila2)} clientes na fila 2")
    print(f"Fila 2 atual {fila2}")
    print("-"*40)
    print("Digite F para adicionar um cliente ao fim da fila 1,")
    print("ou A para realizar o atendimento da fila 1.")
    print("-"*40)
    print("Digite G para adicionar um cliente ao fim da fila 2,")
    print("ou B para realizar o atendimento da fila 2. ")
    print("-"*40)
    operacao = input("Operação\nA, F para fila 1\nB, G para fila 2\nS para sair\nOpção: ")
    print("-"*40)
    x = 0
    sair = False
    while x < len(operacao):
        #Operações Fila 1
        if operacao[x] == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")

        elif operacao[x] == "F":
            ultimo += 1 #incrementa o ticket do novo cliente na fila 1
            fila1.append(ultimo)

        #Operações Fila 2
        elif operacao[x] == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")

        elif operacao[x] == "G":
            ultimo += 1 #incrementa o ticket do novo cliente na fila 2
            fila2.append(ultimo)

        #Sair
        elif operacao[x] == "S":
            sair = True
            break

        else:
            print("Operação inválida! Digite apenas A, B, F, G ou S!")
        x += 1
    if sair:
        break