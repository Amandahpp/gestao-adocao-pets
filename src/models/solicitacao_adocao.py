from src.models.estados import EstadoPendente

class SolicitacaoAdocao:

    def __init__(self, animal, adotante):
        self.__animal = animal
        self.__adotante = adotante
        self.__estado = EstadoPendente()

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, novo_estado):
        self.__estado = novo_estado

    def aprovar(self):
        self.__estado.aprovar(self)
        self.__animal.status = "Adotado"

    def rejeitar(self):
        self.__estado.rejeitar(self)

    def exibir(self):
        return (
            f"{self.__animal.nome} -> "
            f"{self.__adotante.nome} | "
            f"{type(self.__estado).__name__}"
        )
