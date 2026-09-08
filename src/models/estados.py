from estado_solicitacao import EstadoSolicitacao

class EstadoAprovada(EstadoSolicitacao):

    def aprovar(self, solicitacao):
        print("Solicitação já aprovada.")

    def rejeitar(self, solicitacao):
        print("Não pode rejeitar uma solicitação aprovada.")

class EstadoRejeitada(EstadoSolicitacao):

    def aprovar(self, solicitacao):
        print("Não pode aprovar uma solicitação rejeitada.")

    def rejeitar(self, solicitacao):
        print("Solicitação já rejeitada.")

class EstadoPendente(EstadoSolicitacao):

    def aprovar(self, solicitacao):
        solicitacao.estado = EstadoAprovada()

    def rejeitar(self, solicitacao):
        solicitacao.estado = EstadoRejeitada()