class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.macha = 1

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("parando bicicleta ....")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummm .............")

    def trocar_macha(self, numero_da_macha = 1):
        print("Trocando macha ....")
        
        def _trocar_macha():
            if numero_da_macha > self.macha:
                print("macha trocada\n")
        print("Macha não alterada .....\n")
                
    def __str__(self):
        return f"{self.__class__.__name__}: {' - '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

bicicleta1 = Bicicleta("Laranja", "barra-forte", 2021, 752)

bicicleta1.correr()

print("\n",bicicleta1.cor, bicicleta1.modelo, bicicleta1.ano, bicicleta1.valor, "\n")

print(bicicleta1)

print(bicicleta1.trocar_macha())