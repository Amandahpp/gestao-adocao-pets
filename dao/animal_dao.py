from database.conexao import transacao, executar, ErroBanco, FOREIGN_KEY_VIOLATION
from src.models.animal_factory import AnimalFactory
from src.models.cachorro import Cachorro
from src.models.gato import Gato

_COLUNAS = "id, nome, idade, sexo, status, tipo, raca, pelagem"


def _para_animal(linha):
    id_animal, nome, idade, sexo, status, tipo, raca, pelagem = linha
    detalhe = raca if tipo == "Cachorro" else pelagem
    animal = AnimalFactory.criar_animal(tipo, id_animal, nome, idade, sexo, detalhe)
    animal.status = status
    return animal


class AnimalDAO:
    """Acesso à tabela Animal. Cachorro e gato ficam na mesma tabela;
    a coluna `tipo` indica qual classe criar ao ler."""

    def inserir(self, animal, abrigo_id=None, conn=None):
        """Grava o animal e passa a ele o id gerado pelo banco. Devolve esse id."""
        if isinstance(animal, Cachorro):
            tipo, raca, pelagem = "Cachorro", animal.raca, None
        elif isinstance(animal, Gato):
            tipo, raca, pelagem = "Gato", None, animal.pelagem
        else:
            raise ValueError("Tipo de animal não suportado.")
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur,
                     "INSERT INTO Animal (nome, idade, sexo, status, tipo, raca, pelagem, abrigo_id) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id",
                     (animal.nome, animal.idade, animal.sexo, animal.status,
                      tipo, raca, pelagem, abrigo_id))
            animal.id = cur.fetchone()[0]
            return animal.id

    def buscar_por_id(self, animal_id, conn=None):
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur, f"SELECT {_COLUNAS} FROM Animal WHERE id = %s", (animal_id,))
            linha = cur.fetchone()
            return _para_animal(linha) if linha else None

    def listar(self, abrigo_id=None, conn=None):
        """Lista os animais, do mais antigo cadastro para o mais novo.
        Com `abrigo_id`, devolve só os animais desse abrigo."""
        with transacao(conn) as c, c.cursor() as cur:
            if abrigo_id is None:
                executar(cur, f"SELECT {_COLUNAS} FROM Animal ORDER BY id")
            else:
                executar(cur, f"SELECT {_COLUNAS} FROM Animal WHERE abrigo_id = %s ORDER BY id",
                         (abrigo_id,))
            return [_para_animal(linha) for linha in cur.fetchall()]

    def atualizar_status(self, animal, conn=None):
        """Grava o status atual do animal ('Disponível' ou 'Adotado')."""
        with transacao(conn) as c, c.cursor() as cur:
            executar(cur, "UPDATE Animal SET status = %s WHERE id = %s",
                     (animal.status, animal.id))
            return cur.rowcount > 0

    def remover(self, animal_id, conn=None):
        with transacao(conn) as c, c.cursor() as cur:
            try:
                executar(cur, "DELETE FROM Animal WHERE id = %s", (animal_id,))
            except ErroBanco as erro:
                if erro.codigo == FOREIGN_KEY_VIOLATION:
                    raise ValueError("Não é possível remover: o animal tem solicitações.") from erro
                raise
            return cur.rowcount > 0
