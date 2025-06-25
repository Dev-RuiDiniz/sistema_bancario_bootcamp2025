from models import PessoaFisica, ContaCorrente, Deposito, Saque
import re # Para validação de CPF

def menu():
    print("""
    ========== MENU ==========
    [nu] Novo Usuário (Pessoa Física)
    [nc] Nova Conta Corrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [lc] Listar Contas
    [lu] Listar Usuários
    [q] Sair
    ==========================
    """)
    return input("Escolha uma opção: ").lower()

def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf: # Acessa o CPF via propriedade
            return cliente
    return None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n!!! Cliente não possui conta. !!!")
        return None
    
    if len(cliente.contas) == 1:
        return cliente.contas[0]
    else:
        # Se o cliente tiver múltiplas contas, pedir para escolher uma
        print("\nContas do Cliente:")
        for i, conta in enumerate(cliente.contas):
            print(f"  [{i+1}] {conta.numero} - Saldo: R$ {conta.saldo:.2f}") # Mostra mais detalhes da conta
        
        while True:
            try:
                escolha = int(input("Escolha o número da conta para operar: ")) - 1
                if 0 <= escolha < len(cliente.contas):
                    return cliente.contas[escolha]
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n!!! Cliente não encontrado! !!!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)
    except ValueError:
        print("Valor inválido. Digite um número.")


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n!!! Cliente não encontrado! !!!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    try:
        valor = float(input("Informe o valor do saque: R$ "))
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)
    except ValueError:
        print("Valor inválido. Digite um número.")


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n!!! Cliente não encontrado! !!!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            print(f"{transacao['data']}: {transacao['tipo']}: R$ {transacao['valor']:.2f}")

    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_novo_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    if not re.fullmatch(r'\d{11}', cpf):
        print("\n!!! CPF inválido! Digite 11 dígitos numéricos. !!!")
        return

    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n!!! Já existe cliente com este CPF! !!!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Agora instanciamos PessoaFisica
    novo_cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(novo_cliente)
    print("\n=== Cliente (Pessoa Física) criado com sucesso! ===")


def criar_nova_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n!!! Cliente não encontrado, fluxo de criação de conta encerrado! !!!")
        return

    # Opcional: Adicionar lógica para não permitir múltiplos contas correntes do mesmo tipo para o mesmo cliente
    for conta in cliente.contas:
        if isinstance(conta, ContaCorrente):
            print("\n!!! Cliente já possui uma conta corrente. !!!")
            return

    # Agora instanciamos ContaCorrente
    nova_conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(nova_conta)
    cliente.adicionar_conta(nova_conta) # Adiciona a conta ao cliente
    print(f"\n=== Conta corrente criada com sucesso! Número da conta: {nova_conta.numero} ===")


def listar_contas(contas):
    if not contas:
        print("\n!!! Nenhuma conta cadastrada. !!!")
        return
    for conta in contas:
        print("=" * 100)
        # O __str__ de ContaCorrente é chamado automaticamente
        print(conta) 
    print("=" * 100)

def listar_usuarios(clientes):
    if not clientes:
        print("\n!!! Nenhum usuário cadastrado. !!!")
        return
    
    print("\n============== USUÁRIOS CADASTRADOS ==============")
    for cliente in clientes:
        # O __str__ de PessoaFisica é chamado automaticamente
        print(cliente)
        print("-" * 50)
    print("==================================================")


def main():
    clientes = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "nu":
            criar_novo_cliente(clientes)
        elif opcao == "nc":
            # Passa clientes e contas para que a função possa adicionar a nova conta
            # e vincular ao cliente correto.
            # Incrementa numero_conta apenas se a conta for criada com sucesso
            # (validando se o cliente existe e não tem conta corrente já).
            temp_len_contas = len(contas)
            criar_nova_conta(numero_conta, clientes, contas)
            if len(contas) > temp_len_contas: # Se uma nova conta foi adicionada
                numero_conta += 1
        elif opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "lu":
            listar_usuarios(clientes)
        elif opcao == "q":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("\n!!! Operação inválida, por favor selecione novamente a operação desejada. !!!")

if __name__ == "__main__":
    main()