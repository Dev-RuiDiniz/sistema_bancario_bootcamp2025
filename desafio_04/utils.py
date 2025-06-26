from collections.abc import Iterator # Para o iterador personalizado

# --- Gerador de Relatórios ---
def gerar_relatorio_transacoes(contas, tipo_transacao=None):
    print("\n========== RELATÓRIO DE TRANSAÇÕES ==========")
    encontrou_transacao = False
    
    for conta in contas:
        print(f"\n--- Conta: {conta.numero} (Cliente: {conta.cliente.nome}) ---")
        transacoes_filtradas = []
        
        if tipo_transacao:
            transacoes_filtradas = [
                t for t in conta.historico.transacoes
                if t['tipo'].lower() == tipo_transacao.lower()
            ]
        else:
            transacoes_filtradas = conta.historico.transacoes
        
        if transacoes_filtradas:
            for t in transacoes_filtradas:
                print(f"  [{t['data']}] Tipo: {t['tipo']} - Valor: R$ {t['valor']:.2f}")
            encontrou_transacao = True
        else:
            print("  Nenhuma transação encontrada para este filtro.")
            
    if not encontrou_transacao and not contas:
        print("Nenhuma conta registrada no sistema.")
    elif not encontrou_transacao and contas:
        print("Nenhuma transação encontrada para o filtro especificado em nenhuma conta.")
        
    print("=============================================\n")


# --- Iterador Personalizado ---
class ContasIterator(Iterator):
    def __init__(self, contas):
        self._contas = contas
        self._index = 0

    def __next__(self):
        try:
            conta = self._contas[self._index]
            self._index += 1
            return (
                f"Conta: {conta.numero}\n"
                f"Agência: {conta.agencia}\n"
                f"Saldo: R$ {conta.saldo:.2f}\n"
                f"Cliente: {conta.cliente.nome} (CPF: {conta.cliente.cpf})\n"
                f"Tipo: {conta.__class__.__name__}\n"
                "--------------------"
            )
        except IndexError:
            raise StopIteration

    def __iter__(self): # O próprio iterador já é um iterável
        return self