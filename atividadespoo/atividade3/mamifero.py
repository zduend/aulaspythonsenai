from Animal import Animal


class Mamifero (Animal):
    def __init__(self, nome, idade, nivel_fome, velocidade_kmh):
        super().__init__(nome, idade,nivel_fome)
        self.__velocidade_kmh = velocidade_kmh


    @property
    def velocidade_kmh(self):
        return self.__velocidade_kmh

    def correr(self):
        print(f"{self.nome} Correu a {self.velocidade_kmh} kmh")
        self.nivel_fome += 20

    def emitir_som(self):
        print(f"{self.nome} ruge/ruge alto!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Velocidade: {self.velocidade_kmh} kmh")
