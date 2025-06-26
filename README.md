# Sistema Bancário Simplificado (Desafios DIO)

Este projeto apresenta a evolução de um sistema bancário simples, desenvolvido como parte dos desafios propostos pela DIO (Digital Innovation One). Ele demonstra a transição de um código monolítico para uma arquitetura mais organizada e modular, culminando na implementação de Programação Orientada a Objetos (POO) para um sistema mais robusto e escalável.

---

## Desafio 01: Sistema Básico (Sem Modularização)

Nesta primeira etapa, o código implementa as funcionalidades básicas de um banco: depósito, saque e visualização de extrato. Todas as funções e variáveis globais estão contidas em um único arquivo. Embora funcional para projetos pequenos, essa abordagem pode dificultar a manutenção e escalabilidade à medida que o sistema cresce.

**Funcionalidades:**
* **Depositar**: Adiciona um valor ao saldo.
* **Sacar**: Retira um valor do saldo, com limites de saque diário e por transação.
* **Visualizar Extrato**: Mostra todas as movimentações (depósitos e saques) e o saldo atual.

---

## Desafio 02: Sistema Modularizado e Atualizado

A segunda fase do projeto foca na modularização e na adição de recursos mais complexos. As funcionalidades foram divididas em dois arquivos (`banco_funcoes.py` e `main.py`), melhorando a organização e a legibilidade do código. Além disso, foram introduzidos os conceitos de usuários e contas correntes, permitindo que o sistema gerencie múltiplas pessoas e suas respectivas contas.

**Principais Atualizações:**
* **Modularização**: Separação das funções lógicas em `banco_funcoes.py` e da interface do usuário em `main.py`.
* **Criação de Usuários**: Permite cadastrar novos usuários com nome, data de nascimento, CPF (único) e endereço.
* **Criação de Contas Correntes**: Vincula uma nova conta corrente a um usuário existente, com número de agência fixo e número de conta sequencial. Cada conta possui seu próprio saldo, extrato e limites de saque.
* **Listagem**: Novas opções para listar todos os usuários cadastrados e listar todas as contas correntes existentes.
* **Melhoria na Interação**: As operações de depósito, saque e extrato agora exigem o número da conta, garantindo que a transação seja realizada na conta correta.
* **Tratamento de Erros**: Implementação de tratamento de exceções para entradas inválidas do usuário.

---

## Desafio 03: Sistema Orientado a Objetos (POO)

A etapa mais avançada do projeto refatora completamente o sistema para utilizar os princípios da Programação Orientada a Objetos (POO). Essa reestruturação visa aprimorar a organização, reusabilidade, manutenibilidade e escalabilidade do código, modelando as entidades do banco como classes e objetos.

### O Poder da Programação Orientada a Objetos (POO)

A refatoração para POO permitiu modelar as entidades do banco de forma mais intuitiva e organizada, utilizando classes que representam conceitos do mundo real e suas interações.

**Estrutura de Classes:** O sistema é construído sobre as seguintes classes, que encapsulam dados e comportamentos específicos:
* `Historico`: Responsável por registrar todas as transações de uma conta.
* `Transacao` (Classe Abstrata): Define a interface para qualquer tipo de transação bancária.
* `Deposito` (Herda de `Transacao`): Implementa a lógica para operações de depósito.
* `Saque` (Herda de `Transacao`): Implementa a lógica para operações de saque, incluindo validações de limite.
* `Conta` (Classe Abstrata): A classe base para todos os tipos de contas, contendo atributos como saldo, número, agência e um `Historico`. Define os métodos abstratos `sacar` e `depositar`.
* `ContaCorrente` (Herda de `Conta`): Especializa a `Conta` com regras adicionais, como limite de valor por saque e limite de saques diários.
* `Cliente`: A classe base para qualquer tipo de cliente, contendo atributos como endereço e uma lista das contas vinculadas.
* `PessoaFisica` (Herda de `Cliente`): Representa um cliente pessoa física, adicionando atributos como nome, data de nascimento e CPF.

**Principais Conceitos de POO Aplicados:**
* **Encapsulamento**: Dados e métodos são agrupados dentro das classes, e o acesso é controlado por propriedades (`@property`).
* **Herança**: Classes mais específicas (`PessoaFisica`, `ContaCorrente`, `Saque`, `Deposito`) reutilizam e estendem a funcionalidade de classes mais genéricas.
* **Polimorfismo**: Diferentes objetos podem responder ao mesmo método de maneiras distintas (ex: o método `registrar` em `Deposito` e `Saque`).
* **Abstração**: Classes como `Transacao` e `Conta` são definidas como abstratas, focando no "o que" em vez do "como", impondo uma estrutura clara e forçando a implementação de métodos essenciais nas subclasses.
* **Modularização**: O código é dividido em arquivos (`models.py` para as classes e `main.py` para a interface do usuário), promovendo uma melhor organização e manutenção.

---

## Desafio 04: Logs, Relatórios e Limites de Operação Diária (Atualização Recente)

Esta fase representa uma evolução crucial na funcionalidade e na robustez do sistema, introduzindo recursos essenciais para auditoria, análise e controle de operações.

**Novas Funcionalidades e Melhorias:**

* **Logs Detalhados com Decorator (`decorators.py`)**:
    * Implementação de um **decorador `@log_transacao`** que agora registra automaticamente informações detalhadas de cada operação de depósito e saque.
    * Cada entrada de log inclui: **data e hora exatas**, **nome da função** executada, **argumentos** passados para a função e o **valor retornado**.
    * Todos os logs são persistidos em um arquivo dedicado chamado `log.txt`. Se o arquivo já existir, as novas entradas são adicionadas no final, garantindo um histórico completo e contínuo.

* **Gerador de Relatórios (`utils.py`)**:
    * Adição da função `gerar_relatorio_transacoes` que permite visualizar um extrato consolidado de transações de todas as contas.
    * Oferece a capacidade de **filtrar as transações por tipo** (Depósito ou Saque), facilitando a análise específica das movimentações.

* **Iterador Personalizado (`utils.py`)**:
    * Introdução da classe `ContasIterator`, um iterador customizado que permite **percorrer todas as contas do banco** de forma programática.
    * Retorna informações formatadas sobre cada conta (número, agência, saldo, cliente), otimizando a exibição e o acesso aos dados das contas.

* **Limite de Operações Diárias por Conta**:
    * Implementado um controle rigoroso que limita cada `ContaCorrente` a um máximo de **10 operações (depósitos ou saques) por dia**.
    * O sistema agora **rastreia a data da última operação** para cada conta, resetando o contador de operações diárias automaticamente quando um novo dia é detectado.
    * Mensagens informativas são exibidas ao usuário quando o limite de operações diárias é atingido para a conta, impedindo novas transações naquele período.
    * O extrato e a listagem de contas exibem claramente as operações diárias restantes, fornecendo transparência ao usuário.

**Estrutura de Arquivos:**
Para acomodar essas novas funcionalidades e manter a modularidade, o projeto agora é organizado em:
* `main.py`: A interface principal do usuário e a lógica de interação.
* `models.py`: Contém todas as classes do modelo de dados (Contas, Clientes, Transações, Histórico).
* `decorators.py`: Onde o decorador de log `@log_transacao` é definido.
* `utils.py`: Contém funções utilitárias como o gerador de relatórios e o iterador de contas.

Este repositório continua a servir como um ótimo exemplo prático de como refatorar e expandir um sistema simples, aplicando progressivamente princípios de organização de código e, finalmente, as poderosas ferramentas da Programação Orientada a Objetos, com um foco crescente em robustez e funcionalidades de auditoria.