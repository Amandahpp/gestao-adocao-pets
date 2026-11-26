
import os
from contextlib import contextmanager

try:
    import psycopg2
except ImportError:  # o programa ainda abre sem o driver, só que sem banco
    psycopg2 = None

UNIQUE_VIOLATION = "23505"
FOREIGN_KEY_VIOLATION = "23503"


class ErroBanco(Exception):
    """Falha ao falar com o banco. `codigo` guarda o código SQLSTATE, se houver."""

    def __init__(self, mensagem, codigo=None):
        super().__init__(mensagem)
        self.codigo = codigo


def conectar():
    """Abre uma nova conexão. Quem chamar precisa fechá-la (use `transacao`)."""
    if psycopg2 is None:
        raise ErroBanco("O driver psycopg2 não está instalado. Rode: pip install -r requirements.txt")
    opcoes = {}
    schema = os.getenv("DB_SCHEMA")
    if schema:
        opcoes["options"] = f"-c search_path={schema}"
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "patinhas"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
            connect_timeout=5,
            **opcoes,
        )
    except psycopg2.Error as erro:
        raise ErroBanco(f"Não foi possível conectar ao banco: {str(erro).strip()}",
                        getattr(erro, "pgcode", None)) from erro


@contextmanager
def transacao(conn=None):
    """Executa um bloco em uma transação.

    Sem `conn`, abre uma conexão, confirma (commit) no fim e desfaz (rollback) se der erro.
    Com `conn`, só reaproveita a conexão: quem a abriu decide o commit e o rollback.
    Isso permite que vários DAOs participem da mesma transação.
    """
    if conn is not None:
        yield conn
        return
    conn = conectar()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def executar(cursor, sql, parametros=None):
    """Executa um comando SQL e converte erros do driver em `ErroBanco`."""
    try:
        cursor.execute(sql, parametros)
    except psycopg2.Error as erro:
        raise ErroBanco(str(erro).strip(), getattr(erro, "pgcode", None)) from erro
