from src.models.estados import EstadoPendente

class SolicitacaoAdocao:
    def __init__(self, animal, adotante):
        self._animal = animal
        self._adotante = adotante
        self._estado = EstadoPendente()

    @property
    def animal(self): return self._animal
    @property
    def adotante(self): return self._adotante
    @property
    def estado(self): return self._estado
    @estado.setter
    def estado(self, valor): self._estado = valor
    @property
    def status(self): return self._estado.nome

    def aprovar(self): self._estado.aprovar(self)
    def rejeitar(self): self._estado.rejeitar(self)
    def exibir(self):
        return f"{self.animal.nome} -> {self.adotante.nome} | {self.status}"
