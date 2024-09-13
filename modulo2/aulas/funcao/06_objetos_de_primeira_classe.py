def somar(a, b):
  return a + b
    

def subtrair(a, b):
   return a - b


def dividir (a, b):
    return a / b
 

def exibir_resultado(a, b, funcao):
    simbolo = ""
    resultado = funcao(a, b)
    return print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, dividir)  # O resultado da operação 10 + 10 = 20

op = somar
print(op(5, 6))