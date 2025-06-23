extrato = []
saldo = 0.0
LIMITE_SAQUE = 3
saques_realizados = 0
LIMITE_VALOR_SAQUE = 500.0

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")
        return "Depósito realizado com sucesso!"
    else:
        return "Valor inválido para depósito."

def sacar(valor):
    global saldo, extrato, saques_realizados
    if valor <= 0:
        return "Valor inválido para saque."
    if valor > saldo:
        return "Saldo insuficiente."
    if saques_realizados >= LIMITE_SAQUE:
        return "Limite de saques diários atingido."
    if valor > LIMITE_VALOR_SAQUE:
        return f"Limite por saque é de R$ {LIMITE_VALOR_SAQUE:.2f}."

    saldo -= valor
    saques_realizados += 1
    extrato.append(f"Saque: -R$ {valor:.2f}")
    return "Saque realizado com sucesso!"

def visualizar_extrato():
    global extrato, saldo
    print("\n===== EXTRATO =====")
    if extrato:
        for linha in extrato:
            print(linha)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("====================\n")
