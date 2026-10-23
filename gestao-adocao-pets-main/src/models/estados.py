from src.models.estado_solicitacao import EstadoSolicitacao

class EstadoPendente(EstadoSolicitacao):
    nome = "Pendente"
    def aprovar(self, solicitacao):
        if solicitacao.animal.status != "Disponível":
            raise ValueError("O animal já foi adotado.")
        solicitacao.animal.status = "Adotado"
        solicitacao.estado = EstadoAprovada()
    def rejeitar(self, solicitacao):
        solicitacao.estado = EstadoRejeitada()

class EstadoAprovada(EstadoSolicitacao):
    nome = "Aprovada"
    def aprovar(self, solicitacao): raise ValueError("A solicitação já foi aprovada.")
    def rejeitar(self, solicitacao): raise ValueError("Não é possível rejeitar uma solicitação aprovada.")

class EstadoRejeitada(EstadoSolicitacao):
    nome = "Rejeitada"
    def aprovar(self, solicitacao): raise ValueError("Não é possível aprovar uma solicitação rejeitada.")
    def rejeitar(self, solicitacao): raise ValueError("A solicitação já foi rejeitada.")
