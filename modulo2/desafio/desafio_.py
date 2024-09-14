menu = '''
    ================ MENU ================
    |  [1]\tDepositar                  |
    |  [2]\tSacar                      |
    |  [3]\tExtrato                    |
    |  [4]\tSair                       |
    ================ MENU ================
=>'''

LIMITE_SAQUES = 3

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input('''
______________________________________
>>> Informe o valor do deposito: '''))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: {valor:.2f}\n"
            print(f"Valor: R$ {valor} depositad com sucesso!")
        else:
            print("Operação falhou! Valor invalido!!")
        

    elif opcao == "2":
        valor = float(input('''
     ______________________________________
    >>> Informe o valor do Saque: '''))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('''
        ____________________________________________
       |                                            |
       |           Saldo insuficiente               |
       |____________________________________________|
       ''')
        
        if excedeu_limite:
            print('''
        ____________________________________________
       |                                            |
       |   Não executado. valor excede o limite!   |
       |____________________________________________|
       ''')     


        elif excedeu_saques:
            print('''
        ____________________________________________
       |                                            |
       |   Não executado. valor excede o limite!    |
       |____________________________________________|
            ''')        
        elif valor > 0:
            saldo -= valor 
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque: R$ {valor} efetuado com sucesso!")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação invalida, por favor elecione novamente a operação desejada.")