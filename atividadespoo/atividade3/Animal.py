class Animal():
    def __init__(self, idade, nivel_fome):
        self.__idade = idade
        self.__nivel_fome = nivel_fome

    @property
    def idade(self,nova_idade):
        return self.__idade

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @nivel_fome.setter
    def nivel_fome(self,nivel_fome):
        self.__nivel_fome = nivel_fome


