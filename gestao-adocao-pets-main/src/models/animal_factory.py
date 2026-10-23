from src.models.cachorro import Cachorro
from src.models.gato import Gato

class AnimalFactory:

    @staticmethod
    def criar_animal(tipo, *args):

        if tipo.lower() == "cachorro":
            return Cachorro(*args)

        elif tipo.lower() == "gato":
            return Gato(*args)

        raise ValueError("Tipo inválido")
