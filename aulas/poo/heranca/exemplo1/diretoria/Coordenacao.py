class Coordenacao:
    def __init__(self, professores, cursos, alumos):
        self.__professores = professores
        self.__cursos = cursos
        self.__alumos = alumos

    @property
    def cursos(self):
        return self.__cursos
    @property
    def professores(self):
        return self.__professores
    @property
    def alumos(self):
        return self.__alumos

    def escolher_professores(self, index_professores):
        return self.__professores[index_professores]

