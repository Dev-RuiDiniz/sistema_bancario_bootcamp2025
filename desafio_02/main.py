from banco_funcoes import (
    criar_usuario, criar_conta_corrente, depositar,
    sacar, visualizar_extrato, listar_usuarios, listar_contas
)

def menu():
    print("""
    ========== MENU ==========
    [1] Criar Novo Usuário
    [2] Criar Nova Conta Corrente
    [3] Depositar
    [4] Sacar
    [5] Visualizar Extrato
    [6] Listar Usuários
    [7] Listar Contas
    [8] Sair
    ==========================
    """)

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Criar Novo Usuário ---")
        nome = input("Nome completo: ")
        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço (Logradouro, Nº - Bairro - Cidade/Estado): ")
        
        mensagem = criar_usuario(nome, data_nascimento, cpf, endereco)
        print(mensagem)

    elif opcao == "2":
        print("\n--- Criar Nova Conta Corrente ---")
        cpf_usuario = input("Digite o CPF do usuário para vincular a conta: ")
        mensagem = criar_conta_corrente(cpf_usuario)
        print(mensagem)

    elif opcao == "3":
        print("\n--- Depositar ---")
        try:
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor para depósito: R$ "))
            mensagem = depositar(numero_conta, valor)
            print(mensagem)
        except ValueError:
            print("Número da conta ou valor inválido.")
    
    elif opcao == "4":
        print("\n--- Sacar ---")
        try:
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor para saque: R$ "))
            mensagem = sacar(numero_conta, valor)
            print(mensagem)
        except ValueError:
            print("Número da conta ou valor inválido.")

    elif opcao == "5":
        print("\n--- Visualizar Extrato ---")
        try:
            numero_conta = int(input("Digite o número da conta: "))
            visualizar_extrato(numero_conta)
        except ValueError:
            print("Número da conta inválido.")

    elif opcao == "6":
        listar_usuarios()

    elif opcao == "7":
        listar_contas()

    elif opcao == "8":
        print("Encerrando o sistema. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")