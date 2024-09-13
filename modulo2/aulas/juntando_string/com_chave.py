nome = "Anderson"
idade = 32
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos, e trabalho como {} e estou matriculado no curso de {}".format (nome, idade, profissao, linguagem) )

print("")
print("*****************Ex: 02**************************")
print("")

nome = "Anderson"
idade = 32
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {3}. Eu tenho {2} anos, e trabalho como {1} e estou matriculado no curso de {0}".format (nome, idade, profissao, linguagem), "\n")

print("*****************Ex: 03**************************")
print("")

nome = "Anderson"
idade = 32
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {nome_usuario}. Eu tenho {idade_usuario} anos, e trabalho como {profissao_usuari} e estou matriculado no curso de {linguagem_usuario}".format (nome_usuario = nome, idade_usuario = idade, profissao_usuari = profissao, linguagem_usuario = linguagem), "\n")

print("*****************Ex: 04 Validar **************************")
print("")

dados = {"nome": "Anderson", "idade": 32, "profissao": "Programador", "linguagem": "Python"}

print("Olá, me chamo {nome}. Eu tenho {idade} anos, e trabalho como {profissao} e estou matriculado no curso de {linguagem}".format (**dados), "\n")

print("*****************Ex: 05**************************")
print("")

nome = "Anderson"
idade = 32
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos, e trabalho como {profissao} e estou matriculado no curso de {linguagem}", "\n")

print("*****************Ex: 06**************************")
PI = 3.14159

print(f"valor de PI: {PI:.2f}")

print(f"valor de PI: {PI:10.2f}")