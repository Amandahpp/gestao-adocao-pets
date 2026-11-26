from database.conexao import (
    transacao, executar, ErroBanco, UNIQUE_VIOLATION, FOREIGN_KEY_VIOLATION,
)
from src.models.adotante import Adotante


def _para_adotante(linha):
    cpf, nome, telefone = linha
    return Adotante(nome, cpf, telefone or "")


class AdotanteDAO:
    """Acesso à tabela Adotante. O CPF (só dígitos) é a chave primária."""

    def inserir(self, adotante, conn=None):
        with transacao(conn) as c, c.cursor() as cur:
            try:
                executar(cur,
                         "INSERT INTO Adotante (cpf, nome, telefone) VALUES (%s, %s, %s)",
                         (adotante.cpf, adotante.nome, adotante.telefone))
            except ErroBanco as erro:
                if erro.codigo == UNIQUE_VIOLATION:
                    raise ValueError("Já existe um adotante com esse CPF.") from erro
                raise

    def buscar_por_cpf(self, cpf, conn=None):
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur, "SELECT cpf, nome, telefone FROM Adotante WHERE cpf = %s", (cpf,))
            linha = cur.fetchone()
            return _para_adotante(linha) if linha else None

    def listar(self, conn=None):
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur, "SELECT cpf, nome, telefone FROM Adotante ORDER BY nome, cpf")
            return [_para_adotante(linha) for linha in cur.fetchall()]

    def atualizar(self, adotante, conn=None):
        """Atualiza nome e telefone do adotante que tem o mesmo CPF."""
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur,
                     "UPDATE Adotante SET nome = %s, telefone = %s WHERE cpf = %s",
                     (adotante.nome, adotante.telefone, adotante.cpf))
            return cur.rowcount > 0

    def remover(self, cpf, conn=None):
        with transacao(conn) as c, c.cursor() as cur:
            try:
                executar(cur, "DELETE FROM Adotante WHERE cpf = %s", (cpf,))
            except ErroBanco as erro:
                if erro.codigo == FOREIGN_KEY_VIOLATION:
                    raise ValueError("Não é possível remover: o adotante tem solicitações.") from erro
                raise
            return cur.rowcount > 0
