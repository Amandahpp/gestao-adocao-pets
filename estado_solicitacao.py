from abc import ABC, abstractmethod

class EstadoSolicitacao(ABC):

    @abstractmethod
    def aprovar(self, solicitacao):
        pass

    @abstractmethod
    def rejeitar(self, solicitacao):
        pass