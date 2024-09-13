texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end="-")
else:
    print() # adiciona uma quebra de linha
    print("executa no final do laço")
    
