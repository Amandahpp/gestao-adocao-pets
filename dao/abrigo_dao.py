from database.conexao import transacao, executar


class AbrigoDAO:
    """Acesso à tabela Abrigo. Devolve identificadores, não objetos `Abrigo`,
    porque o `Abrigo` é um Singleton que guarda as listas em memória."""

    def obter_ou_criar(self, nome, conn=None):
        """Devolve o id do abrigo com esse nome. Cria o abrigo se ele não existir."""
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur, "SELECT id FROM Abrigo WHERE nome = %s", (nome,))
            linha = cur.fetchone()
            if linha:
                return linha[0]
            executar(cur, "INSERT INTO Abrigo (nome) VALUES (%s) RETURNING id", (nome,))
            return cur.fetchone()[0]

    def buscar_por_id(self, abrigo_id, conn=None):
        """Devolve o nome do abrigo ou None."""
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur, "SELECT nome FROM Abrigo WHERE id = %s", (abrigo_id,))
            linha = cur.fetchone()
            return linha[0] if linha else None

    def listar(self, conn=None):
        """Devolve uma lista de tuplas (id, nome)."""
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur, "SELECT id, nome FROM Abrigo ORDER BY id")
            return cur.fetchall()

    def atualizar_nome(self, abrigo_id, novo_nome, conn=None):
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur, "UPDATE Abrigo SET nome = %s WHERE id = %s", (novo_nome, abrigo_id))
            return cur.rowcount > 0
