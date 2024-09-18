while True:
    numero = int(input("escolha um numero: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)