saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)

print(saldo >= saque or saque <= limite)

print(1000 > 1500)
print(not 1000 > 1500)

contatos_emergencia = []
print(not contatos_emergencia)

print("********************************************************")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

conta_com_saldo = saldo >= saque and saque <= limite
conta_expecial_com_saldo = conta_especial and saldo >= saque

print("conta_expecial_com_saldo or conta_com_saldo:", conta_expecial_com_saldo or conta_com_saldo)
