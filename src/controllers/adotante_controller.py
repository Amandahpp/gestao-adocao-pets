# import feio pq deu erro de novo
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from src.models.adotante import Adotante

class AdotanteController:

    def __init__(self):
        self.adotantes = []

    def cadastrar_adotante(self, nome, cpf, telefone):
        adotante = Adotante(nome, cpf, telefone)

        self.adotantes.append(adotante)

        # teste
        print(adotante.exibir_dados())