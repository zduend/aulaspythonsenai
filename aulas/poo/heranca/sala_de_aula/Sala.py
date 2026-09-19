from aulas.poo.heranca.diretoria.Coordenacao import Coordenacao


class Sala(Coordenacao):
    def __init__(self, laboratorio, tipo, professores, cursos, alumos):
        super().__init__(professores, cursos, alumos)
        self.__laboratorio = laboratorio
        self.__tipo = tipo

    def ter_aula(self):
        print(f"Aula de: {self.cursos}"
              f"No Laboratorio de: {self.__tipo}"
              f"\n com o professor: {self.professores}"
              f"\n com os alunos:")
        for aluno in self.alumos:
            print(aluno)




sala_1 = Sala("Lab 7",
              "Tecnologia",
              "João",
              "Python",
              ["Fulano", "Beltrano", "Cicrano"])


sala_1.ter_aula()
