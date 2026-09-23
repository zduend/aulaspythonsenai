class Animal():
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.idade = idade
        self.nivel_fome = nivel_fome


    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Erro: Idade inválida")
        else:
            self.__idade = nova_idade


    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, novo_nivel_fome):
        if novo_nivel_fome < 0:
            self.__nivel_fome = 0
        elif novo_nivel_fome > 100:
            self.__nivel_fome = 100
        else:
            self.__nivel_fome = novo_nivel_fome

    def alimentar(self, porcao):
        if porcao > 0:
            self.nivel_fome = self.nivel_fome - porcao
        else:
            print("Erro: Porção inválida")


    def emitir_som(self):
        print(f"{self.nome} fez um som genérico!")

    def exibir_resumo(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nível de fome: {self.nivel_fome}")














