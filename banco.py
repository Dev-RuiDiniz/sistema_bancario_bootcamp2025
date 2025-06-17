from funcoes import depositar, sacar, visualizar_extrato

def menu():
    print("""
    ========== MENU ==========
    [1] Depositar
    [2] Sacar
    [3] Visualizar Extrato
    [4] Sair
    ==========================
    """)

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            valor = float(input("Digite o valor para depósito: R$ "))
            mensagem = depositar(valor)
            print(mensagem)
        except ValueError:
            print("Valor inválido.")
    
    elif opcao == "2":
        try:
            valor = float(input("Digite o valor para saque: R$ "))
            mensagem = sacar(valor)
            print(mensagem)
        except ValueError:
            print("Valor inválido.")

    elif opcao == "3":
        visualizar_extrato()

    elif opcao == "4":
        print("Encerrando o sistema. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
