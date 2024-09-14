# Hi, Devs! 👋😊

### O meu nome é Anderson, Seja bem-vindo ao meu mini projeto bancario.
- 🔰 Sou de São Paulo/SP, Brasil
- ⚡ Apaixonado por Esporte e Tecnologia

#

### Codigo:

Este código implementa um sistema de banco simples com um menu interativo que oferece quatro opções: depositar, sacar, ver o extrato e sair.

Variáveis principais:

saldo: O saldo atual da conta.
limite: Limite máximo para saques (R$ 500).
numero_saques: Contador para o número de saques (máximo de 3).
extrato: Histórico de transações.
Menu de opções:

- 1 Depositar: Solicita ao usuário o valor a ser depositado e atualiza o saldo e o extrato.
- 2 Sacar: Solicita o valor do saque, verifica o saldo, limite e quantidade de saques, e realiza a operação se possível.
- 3 Extrato: Mostra o histórico de transações e o saldo atual.
- 4 Sair: Encerra o programa.
Validações:

Para saque, o código verifica se o valor excede o saldo, o limite ou o número de saques permitidos.
