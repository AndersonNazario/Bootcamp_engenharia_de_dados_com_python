opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato[3] \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exebindo o extrato ...")
else:
    print("Obrigado por usar nosso sistema bancario, até logo")
