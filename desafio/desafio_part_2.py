import textwrap

menu = '''\n
        ================ MENU ================
        |  [1]\tDepositar                    |
        |  [2]\tSacar                        |
        |  [3]\tExtrato                      |
        |  [4]\tNovo usuario                 |
        |  [5]\tNova Conta                   |
        |  [6]\tListar Conta                 |
        |  [7]\tSair                         |
        ================ MENU ================
    =>'''


def depositar(saldo, valor, extrato, /):
    if valor > 0:
       saldo += valor
       extrato += f"Deposito: {valor:.2f}\n"
       print(f"\nSecesso: Valor: R$ {valor} depositad com sucesso!")
    else:
       print("\nErro: Operação falhou! Valor invalido!!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nErro: Operação falha! Saldo insuficiente. ")

    elif excedeu_limite:
        print("\nErro: Valor do saque excede o limite!")

    elif excedeu_saques:
        print("\nErro: Numero de saques exedido!")

    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque:\t\tR$:{valor:.2f}\n"
        numero_saques += 1
        print("\nSucesso: Saque realidado com sucesso!!!")

    else:
        print("\nErro: Valor informado invalido!")

    return saldo, extrato

def mostrar_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")   

def criar_novo_usuario(usuarios):
    cpf = input("Informe o CPF do cliente (SOMENTE NUMEROS): ")     
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nERRO: CPF ja existe em nosso banco de dados.")
        return
    nome = input("Nome completo: ")
    endereco = input("Informe seu indereço: ")
    data_de_nascimento = input("Informe a data de nascimento dd-mm-aaaa: ")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})

    print("Sucesso: Usuario criado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nSucesso: Conta criada com sucesso!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nERRO: Usuario não encontrado!!!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 750
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == '1':
            valor = float(input('''\n
            ______________________________________
            >>> Informe o valor do deposito: '''))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input('''\n
            ______________________________________
            >>> Informe o valor do Saque: '''))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
 
        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_novo_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
           listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("\nOperção invalida, informe uma operação valida!")


main()
            