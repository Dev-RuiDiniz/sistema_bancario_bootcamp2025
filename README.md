Sistema Bancário Simplificado (Desafios DIO)
Este projeto apresenta a evolução de um sistema bancário simples, desenvolvido como parte dos desafios propostos pela DIO (Digital Innovation One). Ele demonstra a transição de um código monolítico para uma arquitetura mais organizada e modular, adicionando funcionalidades essenciais de gerenciamento de usuários e contas.

Desafio 01: Sistema Básico (Sem Modularização)
Nesta primeira etapa, o código implementa as funcionalidades básicas de um banco: depósito, saque e visualização de extrato. Todas as funções e variáveis globais estão contidas em um único arquivo, o que é comum em projetos pequenos, mas pode dificultar a manutenção e escalabilidade à medida que o sistema cresce.

Funcionalidades:

Depositar: Adiciona um valor ao saldo.
Sacar: Retira um valor do saldo, com limites de saque diário e por transação.
Visualizar Extrato: Mostra todas as movimentações (depósitos e saques) e o saldo atual.

Desafio 02: Sistema Modularizado e Atualizado
A segunda fase do projeto foca na modularização e na adição de recursos mais complexos. As funcionalidades foram divididas em dois arquivos (banco_funcoes.py e main.py), melhorando a organização e a legibilidade do código. Além disso, foram introduzidos o conceito de usuários e contas correntes, permitindo que o sistema gerencie múltiplas pessoas e suas respectivas contas.

Principais Atualizações:

Modularização: Separação das funções lógicas em banco_funcoes.py e da interface do usuário em main.py.
Criação de Usuários: Permite cadastrar novos usuários com nome, data de nascimento, CPF (único) e endereço.
Criação de Contas Correntes: Vincula uma nova conta corrente a um usuário existente, com número de agência fixo e número de conta sequencial. Cada conta possui seu próprio saldo, extrato e limites de saque.
Listagem: Novas opções para listar todos os usuários cadastrados e listar todas as contas correntes existentes.
Melhoria na Interação: As operações de depósito, saque e extrato agora exigem o número da conta, garantindo que a transação seja realizada na conta correta.
Tratamento de Erros: Implementação de tratamento de exceções para entradas inválidas do usuário.
Este repositório serve como um ótimo exemplo prático de como refatorar e expandir um sistema simples, aplicando princípios de organização de código e adicionando funcionalidades complexas de gerenciamento de dados.