from functools import wraps
from datetime import datetime

def log_transacao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        
        # A lógica para extrair as informações da transação pode variar
        # Aqui, assumimos que 'args' terá a instância da conta e o valor
        # Ou que a transação é criada e passada em 'kwargs'
        
        if func.__name__ == "depositar" or func.__name__ == "sacar":
            conta = args[0] # Assume que o primeiro argumento é a conta
            tipo_transacao = func.__name__.capitalize()
            
            # Registra no histórico da conta a informação simplificada do log
            # O histórico já registra a transação completa no models.py
            # Este log é mais para uma auditoria externa ou console
            
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            log_msg = f"[{data_hora}] Operação: {tipo_transacao}, Conta: {conta.numero}, Cliente: {conta.cliente.nome}, Sucesso: {resultado}"
            print(f"LOG: {log_msg}") # Pode ser salvo em arquivo ou DB futuramente
            
        return resultado
    return wrapper