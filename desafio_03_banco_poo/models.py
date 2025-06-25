from datetime import datetime
from abc import ABC, abstractmethod # Importa ABC e abstractmethod para classes abstratas

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })


class Transacao(ABC): # Transacao agora é uma classe abstrata
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        return sucesso_transacao # Retorna True/False do depósito


class Saque(Transacao):
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        return sucesso_transacao # Retorna True/False do saque


class Conta(ABC): # Conta agora é uma classe abstrata
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados_hoje = 0

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_limite = valor > self._limite
        excedeu_saques = self._saques_realizados_hoje >= self._limite_saques
        excedeu_saldo = valor > saldo # Já existia, mas mantemos a clareza

        if excedeu_saldo:
            print("\n!!! Operação falhou! Você não tem saldo suficiente. !!!")
        elif excedeu_limite:
            print(f"\n!!! Operação falhou! O valor do saque excede o limite de R$ {self._limite:.2f}. !!!")
        elif excedeu_saques:
            print("\n!!! Operação falhou! Número máximo de saques diários excedido. !!!")
        elif valor > 0:
            self._saldo -= valor
            self._saques_realizados_hoje += 1
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n!!! Operação falhou! O valor informado é inválido. !!!")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n!!! Operação falhou! O valor informado é inválido. !!!")
            return False

    def __str__(self):
        return (f"Agência:\t{self.agencia}\n"
                f"C/C:\t\t{self.numero}\n"
                f"Titular:\t{self.cliente.nome}\n")


class Cliente: # Classe base para clientes
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente): # Herda de Cliente
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco) # Chama o construtor da classe base Cliente
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def cpf(self):
        return self._cpf

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Endereço: {self.endereco}")