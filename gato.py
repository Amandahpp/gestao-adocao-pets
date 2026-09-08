from animal import Animal

class Gato(Animal):

    def __init__(self, id_animal, nome, idade, sexo, pelagem):
        super().__init__(id_animal, nome, idade, sexo)
        self.__pelagem = pelagem

    def exibir_dados(self):
        return (
            f"Gato: {self.nome} | "
            f"Pelagem: {self.__pelagem} | "
            f"Idade: {self.idade}"
        )