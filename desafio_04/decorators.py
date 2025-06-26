from functools import wraps
from datetime import datetime

def log_transacao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nome_funcao = func.__name__
        
        # Captura os argumentos da função
        # args[0] será 'self' (a instância da ContaCorrente), então começamos de args[1:] para argumentos da função
        # Se a função for um método de instância, args[0] é a instância (self), então os argumentos reais começam de args[1]
        
        # Simplificando a captura de argumentos para log
        # Para 'depositar(self, valor)' e 'sacar(self, valor)', o valor é args[1]
        args_log = f"args={args[1:] if args else '()'}" # Ignora 'self'
        kwargs_log = f"kwargs={kwargs}"

        # Executa a função original
        resultado = func(*args, **kwargs)

        # Captura o valor retornado pela função
        valor_retornado = resultado

        # Monta a mensagem de log
        log_msg = (
            f"[{data_hora}] Função: {nome_funcao}, "
            f"Argumentos: ({args_log}, {kwargs_log}), "
            f"Valor Retornado: {valor_retornado}\n" # Adiciona quebra de linha
        )
        
        # Escreve no arquivo de log
        try:
            with open("log.txt", "a") as f: # 'a' para append (adicionar no final)
                f.write(log_msg)
            # print(f"Log gravado em log.txt: {log_msg.strip()}") # Opcional: imprimir no console que o log foi gravado
        except IOError as e:
            print(f"Erro ao escrever no arquivo de log: {e}")

        return resultado
    return wrapper