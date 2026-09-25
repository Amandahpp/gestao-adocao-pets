from src.models.animal import Animal

class Cachorro(Animal):

    def __init__(self, id_animal, nome, idade, sexo, raca):
        super().__init__(id_animal, nome, idade, sexo)
        self.__raca = raca

    def exibir_dados(self):
        return (
            f"Cachorro: {self.nome} | "
            f"Raça: {self.__raca} | "
            f"Idade: {self.idade}"
        )
