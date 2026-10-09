from abc import ABC, abstractmethod

class EstadoSolicitacao(ABC):
    @property
    @abstractmethod
    def nome(self): pass

    @abstractmethod
    def aprovar(self, solicitacao): pass

    @abstractmethod
    def rejeitar(self, solicitacao): pass
