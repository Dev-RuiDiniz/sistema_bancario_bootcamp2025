usuarios = []
contas = []
numero_conta_sequencial = 1

def criar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    # Verifica se o CPF já existe
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return "Erro: Já existe um usuário com este CPF."

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    return "Usuário criado com sucesso!"

def criar_conta_corrente(cpf_usuario):
    global contas, numero_conta_sequencial
    # Verifica se o usuário existe
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        return "Erro: Usuário não encontrado para o CPF informado."

    # Verifica se o usuário já tem uma conta (opcional, pode ser alterado)
    for conta in contas:
        if conta["cpf_usuario"] == cpf_usuario:
            return "Erro: Este usuário já possui uma conta corrente."

    nova_conta = {
        "agencia": "0001",  # Agência fixa
        "numero_conta": numero_conta_sequencial,
        "cpf_usuario": cpf_usuario,
        "saldo": 0.0,
        "extrato": [],
        "limite_saque": 3,
        "saques_realizados_hoje": 0,
        "limite_valor_saque": 500.0
    }
    contas.append(nova_conta)
    numero_conta_sequencial += 1
    return f"Conta corrente criada com sucesso! Número da conta: {nova_conta['numero_conta']}"

def depositar(numero_conta, valor):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            if valor > 0:
                conta["saldo"] += valor
                conta["extrato"].append(f"Depósito: +R$ {valor:.2f}")
                return "Depósito realizado com sucesso!"
            else:
                return "Valor inválido para depósito."
    return "Conta não encontrada."

def sacar(numero_conta, valor):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            if valor <= 0:
                return "Valor inválido para saque."
            if valor > conta["saldo"]:
                return "Saldo insuficiente."
            if conta["saques_realizados_hoje"] >= conta["limite_saque"]:
                return "Limite de saques diários atingido."
            if valor > conta["limite_valor_saque"]:
                return f"Limite por saque é de R$ {conta['limite_valor_saque']:.2f}."

            conta["saldo"] -= valor
            conta["saques_realizados_hoje"] += 1
            conta["extrato"].append(f"Saque: -R$ {valor:.2f}")
            return "Saque realizado com sucesso!"
    return "Conta não encontrada."

def visualizar_extrato(numero_conta):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            print(f"\n===== EXTRATO CONTA {numero_conta} =====")
            if conta["extrato"]:
                for linha in conta["extrato"]:
                    print(linha)
            else:
                print("Não foram realizadas movimentações.")
            print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
            print("====================\n")
            return
    print("Conta não encontrada.")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\n===== USUÁRIOS CADASTRADOS =====")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"Endereço: {usuario['endereco']}")
        print("-" * 30)
    print("==============================\n")

def listar_contas():
    if not contas:
        print("Nenhuma conta corrente cadastrada.")
        return

    print("\n===== CONTAS CORRENTES =====")
    for conta in contas:
        # Encontra o nome do usuário associado à conta
        nome_usuario = "Desconhecido"
        for usuario in usuarios:
            if usuario["cpf"] == conta["cpf_usuario"]:
                nome_usuario = usuario["nome"]
                break

        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"CPF do Usuário: {conta['cpf_usuario']} ({nome_usuario})")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
        print("-" * 30)
    print("===========================\n")