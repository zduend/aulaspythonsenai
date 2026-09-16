class Carros:
    def __init__(self, modelo, ano, portas, marchas, lugares):        #CONSTRUTOR
        self.modelo = modelo
        self.ano = ano
        self.portas = portas          #ATRIBUTOS
        self.marchas = marchas
        self.lugares = lugares


    def mostrarmodelocarros(self):
        print(self.modelo)

    def ligar(self):
        print(f"O {self.modelo} foi ligado!")                       # METODOS CONVÊNCIONAIS

    def desligar(self):
        print(f"O {self.modelo} está desligado!")

    def __str__(self):
        return f"Modelo do carro: {self.modelo}\nAno do carro: {self.ano}\nQuantas portas: {self.portas}\nMarchas: {self.marchas}\nlugares: {self.lugares}\n"  # METODOS ESPECIAIS

Carro1 = Carros("Gol", "1999", 2, 5, 5)
Carro2 = Carros("Civic", "2001", 4, 6, 5)
Carro3 = Carros("Uno", "2013", 2, 5, 5)                     #OBJETOS E INSTÂNCIAS
Carro4 = Carros("Corolla", "2014", 2, 5, 5)
Carro5 = Carros("Onix", "2015", 2, 5, 5)

todosOsCarros = [Carro1, Carro2, Carro3, Carro4, Carro5]

for carro in todosOsCarros:
    print(carro)
    carro.desligar()
    carro.ligar()
    print()

