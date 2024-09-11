saldo = 2000.0
saque = float(input('Informe o valor do saque: '))

if saque <= saldo:
    print('Feito saque de:', saque, "- Seu saldo atal é: ", saldo - saque)
else:
    print("Saldo", saldo, "insuficiente")

print("************Ex2**************  ")
valor1 = 1
valor2 = 2
valor3 = 3

valor = int(input("Informe um valor: "))

if valor == valor1:
    print("Vc escolhei o valor: ", valor1)
elif valor == valor2:
    print("Vc escolhei o valor: ", valor2)
elif valor == valor3:
    print("Vc escolhei o valor: ", valor3)
else:
    print("Valor não encontrado")
print("************Ex3**************  ")
maior_idade = 18

idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Pode tirar CNH")
if idade < maior_idade:
    print("não pode tirar CNH")

print("************Ifi-Alinhado**************  ")
conta_normal = True
conta_universitaria = False


saldo = 2000
saque = 200
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com uso do cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realida com sucessso")
    else:
        print("Saldo insuficiente")