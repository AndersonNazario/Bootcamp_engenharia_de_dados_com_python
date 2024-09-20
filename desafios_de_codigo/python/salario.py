def calcular_imposto(salario):
    alicota = 0.00
    if (salario >= 0 and salario <= 1100):
        alicota = 0.05

    return alicota * salario

valor_salario = float(input())
valor_beneficios = float(input())

valor_imposto = calcular_imposto(valor_salario)

saida = valor_salario - valor_imposto + valor_beneficios
print(f"{saida:.2f}")