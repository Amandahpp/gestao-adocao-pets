from database.conexao import transacao, executar, ErroBanco, UNIQUE_VIOLATION
from dao.adotante_dao import AdotanteDAO
from dao.animal_dao import AnimalDAO
from src.models.estados import estado_por_nome
from src.models.solicitacao_adocao import SolicitacaoAdocao


class SolicitacaoAdocaoDAO:
    """Acesso à tabela SolicitacaoAdocao.

    Uma solicitação liga um animal a um adotante. Para ler, o DAO precisa dos
    objetos já carregados. Assim a solicitação aponta para o MESMO objeto `Animal`
    que está em `Abrigo` (o sistema compara animais por identidade).
    """

    def inserir(self, solicitacao, conn=None):
        """Grava a solicitação e passa a ela o id gerado. O animal e o adotante
        precisam estar gravados antes. Devolve o id."""
        with transacao(conn) as c, c.cursor() as cur:
            try:
                executar(cur,
                         "INSERT INTO SolicitacaoAdocao (animal_id, adotante_cpf, estado, status) "
                         "VALUES (%s, %s, %s, %s) RETURNING id",
                         (solicitacao.animal.id, solicitacao.adotante.cpf,
                          solicitacao.estado.nome, solicitacao.status))
            except ErroBanco as erro:
                if erro.codigo == UNIQUE_VIOLATION:
                    raise ValueError("Já existe uma solicitação pendente para esse animal.") from erro
                raise
            solicitacao.id = cur.fetchone()[0]
            return solicitacao.id

    def atualizar_estado(self, solicitacao, conn=None):
        """Grava o estado atual da solicitação (Pendente, Aprovada ou Rejeitada)."""
        if solicitacao.id is None:
            raise ValueError("A solicitação ainda não foi gravada no banco.")
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur,
                     "UPDATE SolicitacaoAdocao SET estado = %s, status = %s WHERE id = %s",
                     (solicitacao.estado.nome, solicitacao.status, solicitacao.id))
            return cur.rowcount > 0

    def listar(self, animais_por_id=None, adotantes_por_cpf=None, conn=None):
        """Lista as solicitações em ordem de id.

        `animais_por_id` e `adotantes_por_cpf` são dicionários com os objetos já carregados.
        Se faltarem, o DAO carrega todos do banco. Só entram solicitações cujo animal
        esteja em `animais_por_id`.
        """
        with transacao(conn) as c:
            if animais_por_id is None:
                animais_por_id = {a.id: a for a in AnimalDAO().listar(conn=c)}
            if adotantes_por_cpf is None:
                adotantes_por_cpf = {a.cpf: a for a in AdotanteDAO().listar(conn=c)}
            if not animais_por_id:
                return []
            with c.cursor() as cur:
                executar(cur,
                         "SELECT id, animal_id, adotante_cpf, estado FROM SolicitacaoAdocao "
                         "WHERE animal_id = ANY(%s) ORDER BY id",
                         (list(animais_por_id),))
                linhas = cur.fetchall()
            return [self._montar(linha, animais_por_id, adotantes_por_cpf) for linha in linhas]

    def buscar_por_id(self, solicitacao_id, animais_por_id=None, adotantes_por_cpf=None, conn=None):
        with transacao(conn) as c:
            todas = self.listar(animais_por_id, adotantes_por_cpf, conn=c)
            return next((s for s in todas if s.id == solicitacao_id), None)

    @staticmethod
    def _montar(linha, animais_por_id, adotantes_por_cpf):
        id_solicitacao, animal_id, cpf, nome_estado = linha
        solicitacao = SolicitacaoAdocao(animais_por_id[animal_id], adotantes_por_cpf[cpf])
        solicitacao.estado = estado_por_nome(nome_estado)
        solicitacao.id = id_solicitacao
        return solicitacao
