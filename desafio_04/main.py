from models import PessoaFisica, ContaCorrente, Deposito, Saque
from utils import gerar_relatorio_transacoes, ContasIterator # Importa as novas funções
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
    [rt] Relatório de Transações
    [q] Sair
    ==========================
    """)
    return input("Escolha uma opção: ").lower()

def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n!!! Cliente não possui conta. !!!")
        return None
    
    if len(cliente.contas) == 1:
        return cliente.contas[0]
    else:
        print("\nContas do Cliente:")
        for i, conta in enumerate(cliente.contas):
            print(f"  [{i+1}] {conta.numero} - Saldo: R$ {conta.saldo:.2f}")
        
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

    novo_cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(novo_cliente)
    print("\n=== Cliente (Pessoa Física) criado com sucesso! ===")


def criar_nova_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n!!! Cliente não encontrado, fluxo de criação de conta encerrado! !!!")
        return

    for conta in cliente.contas:
        if isinstance(conta, ContaCorrente):
            print("\n!!! Cliente já possui uma conta corrente. !!!")
            return

    nova_conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(nova_conta)
    cliente.adicionar_conta(nova_conta)
    print(f"\n=== Conta corrente criada com sucesso! Número da conta: {nova_conta.numero} ===")


def listar_contas(contas):
    if not contas:
        print("\n!!! Nenhuma conta cadastrada. !!!")
        return
    
    # Usando o iterador personalizado
    print("\n============== LISTA DE CONTAS (ITERADOR) ==============")
    for conta_info in ContasIterator(contas):
        print(conta_info)
    print("========================================================\n")


def listar_usuarios(clientes):
    if not clientes:
        print("\n!!! Nenhum usuário cadastrado. !!!")
        return
    
    print("\n============== USUÁRIOS CADASTRADOS ==============")
    for cliente in clientes:
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
            temp_len_contas = len(contas)
            criar_nova_conta(numero_conta, clientes, contas)
            if len(contas) > temp_len_contas:
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
        elif opcao == "rt":
            print("\n--- Gerar Relatório de Transações ---")
            tipo_filtro = input("Filtrar por tipo de transação (Depósito/Saque) ou vazio para todas: ").strip()
            gerar_relatorio_transacoes(contas, tipo_filtro if tipo_filtro else None)
        elif opcao == "q":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("\n!!! Operação inválida, por favor selecione novamente a operação desejada. !!!")

if __name__ == "__main__":
    main()