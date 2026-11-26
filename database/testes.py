"""Testes de integração dos DAOs. Precisam de um PostgreSQL acessível.

Como executar (na pasta que contém main.py):

    python -m unittest database.testes -v

Os testes criam um schema temporário (`teste_<pid>`), rodam `banco.sql` dentro dele
e apagam o schema no final. As tabelas reais do banco não são tocadas.
Se o banco não estiver acessível, os testes são pulados.
"""
import os
import unittest
from pathlib import Path

from database import conexao
from database.conexao import ErroBanco, conectar, transacao
from dao.abrigo_dao import AbrigoDAO
from dao.adotante_dao import AdotanteDAO
from dao.animal_dao import AnimalDAO
from dao.solicitacaoAdocao_dao import SolicitacaoAdocaoDAO
from src.models.adotante import Adotante
from src.models.animal_factory import AnimalFactory
from src.models.solicitacao_adocao import SolicitacaoAdocao

SCRIPT = Path(__file__).with_name("banco.sql")
SCHEMA = f"teste_{os.getpid()}"
_schema_anterior = None


def setUpModule():
    global _schema_anterior
    _schema_anterior = os.environ.pop("DB_SCHEMA", None)
    try:
        conn = conectar()
    except ErroBanco as erro:
        raise unittest.SkipTest(f"Banco indisponível: {erro}")
    try:
        with conn.cursor() as cur:
            cur.execute(f"CREATE SCHEMA {SCHEMA}")
        conn.commit()
    finally:
        conn.close()
    os.environ["DB_SCHEMA"] = SCHEMA
    with transacao() as conn, conn.cursor() as cur:
        cur.execute(SCRIPT.read_text(encoding="utf-8"))


def tearDownModule():
    os.environ.pop("DB_SCHEMA", None)
    if _schema_anterior is not None:
        os.environ["DB_SCHEMA"] = _schema_anterior
    try:
        with transacao() as conn, conn.cursor() as cur:
            cur.execute(f"DROP SCHEMA IF EXISTS {SCHEMA} CASCADE")
    except ErroBanco:
        pass


class BaseDAO(unittest.TestCase):
    def setUp(self):
        with transacao() as conn, conn.cursor() as cur:
            cur.execute("TRUNCATE SolicitacaoAdocao, Animal, Abrigo, Adotante RESTART IDENTITY CASCADE")
        self.abrigo_dao = AbrigoDAO()
        self.adotante_dao = AdotanteDAO()
        self.animal_dao = AnimalDAO()
        self.solicitacao_dao = SolicitacaoAdocaoDAO()
        self.abrigo_id = self.abrigo_dao.obter_ou_criar("Patinhas Felizes")

    def novo_gato(self, nome="Mimi"):
        gato = AnimalFactory.criar_animal("gato", None, nome, 2, "Fêmea", "Curta")
        self.animal_dao.inserir(gato, self.abrigo_id)
        return gato

    def novo_adotante(self, cpf="12345678901"):
        adotante = Adotante("Ana", cpf, "9999-9999")
        self.adotante_dao.inserir(adotante)
        return adotante


class TesteAbrigoDAO(BaseDAO):
    def test_obter_ou_criar_e_idempotente(self):
        self.assertEqual(self.abrigo_dao.obter_ou_criar("Patinhas Felizes"), self.abrigo_id)
        self.assertEqual(len(self.abrigo_dao.listar()), 1)

    def test_buscar_e_atualizar_nome(self):
        self.assertEqual(self.abrigo_dao.buscar_por_id(self.abrigo_id), "Patinhas Felizes")
        self.assertTrue(self.abrigo_dao.atualizar_nome(self.abrigo_id, "Novo Nome"))
        self.assertEqual(self.abrigo_dao.buscar_por_id(self.abrigo_id), "Novo Nome")
        self.assertIsNone(self.abrigo_dao.buscar_por_id(9999))


class TesteAdotanteDAO(BaseDAO):
    def test_inserir_e_buscar(self):
        self.novo_adotante()
        lido = self.adotante_dao.buscar_por_cpf("12345678901")
        self.assertEqual((lido.nome, lido.cpf, lido.telefone), ("Ana", "12345678901", "9999-9999"))
        self.assertIsNone(self.adotante_dao.buscar_por_cpf("00000000000"))

    def test_cpf_duplicado(self):
        self.novo_adotante()
        with self.assertRaisesRegex(ValueError, "mesmo CPF|esse CPF"):
            self.adotante_dao.inserir(Adotante("Outra", "123.456.789-01", "1"))

    def test_telefone_vazio_nao_vira_texto_none(self):
        self.adotante_dao.inserir(Adotante("Bia", "11122233344", ""))
        self.assertEqual(self.adotante_dao.buscar_por_cpf("11122233344").telefone, "")

    def test_listar_atualizar_remover(self):
        self.novo_adotante("12345678901")
        self.novo_adotante("98765432100")
        self.assertEqual(len(self.adotante_dao.listar()), 2)
        self.assertTrue(self.adotante_dao.atualizar(Adotante("Ana Maria", "12345678901", "1111")))
        self.assertEqual(self.adotante_dao.buscar_por_cpf("12345678901").nome, "Ana Maria")
        self.assertTrue(self.adotante_dao.remover("98765432100"))
        self.assertFalse(self.adotante_dao.remover("98765432100"))

    def test_nao_remove_adotante_com_solicitacao(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        self.solicitacao_dao.inserir(SolicitacaoAdocao(gato, adotante))
        with self.assertRaises(ValueError):
            self.adotante_dao.remover(adotante.cpf)


class TesteAnimalDAO(BaseDAO):
    def test_inserir_define_id_e_le_de_volta_com_o_tipo_certo(self):
        gato = self.novo_gato()
        cao = AnimalFactory.criar_animal("cachorro", None, "Bob", 3, "Macho", "SRD")
        self.animal_dao.inserir(cao, self.abrigo_id)
        self.assertEqual((gato.id, cao.id), (1, 2))
        lido_gato = self.animal_dao.buscar_por_id(gato.id)
        lido_cao = self.animal_dao.buscar_por_id(cao.id)
        self.assertEqual(type(lido_gato).__name__, "Gato")
        self.assertEqual(lido_gato.pelagem, "Curta")
        self.assertEqual(type(lido_cao).__name__, "Cachorro")
        self.assertEqual(lido_cao.raca, "SRD")
        self.assertEqual((lido_cao.nome, lido_cao.idade, lido_cao.sexo, lido_cao.status),
                         ("Bob", 3, "Macho", "Disponível"))

    def test_listar_por_abrigo(self):
        self.novo_gato("A")
        self.novo_gato("B")
        outro = AnimalFactory.criar_animal("gato", None, "C", 1, "Macho", "Longa")
        self.animal_dao.inserir(outro, self.abrigo_dao.obter_ou_criar("Outro abrigo"))
        self.assertEqual([a.nome for a in self.animal_dao.listar(self.abrigo_id)], ["A", "B"])
        self.assertEqual(len(self.animal_dao.listar()), 3)

    def test_atualizar_status(self):
        gato = self.novo_gato()
        gato.status = "Adotado"
        self.assertTrue(self.animal_dao.atualizar_status(gato))
        self.assertEqual(self.animal_dao.buscar_por_id(gato.id).status, "Adotado")

    def test_remover_e_bloqueio_por_solicitacao(self):
        livre, usado, adotante = self.novo_gato("Livre"), self.novo_gato("Usado"), self.novo_adotante()
        self.solicitacao_dao.inserir(SolicitacaoAdocao(usado, adotante))
        self.assertTrue(self.animal_dao.remover(livre.id))
        with self.assertRaises(ValueError):
            self.animal_dao.remover(usado.id)


class TesteSolicitacaoAdocaoDAO(BaseDAO):
    def test_inserir_e_listar_preservando_identidade_dos_objetos(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        s = SolicitacaoAdocao(gato, adotante)
        self.solicitacao_dao.inserir(s)
        self.assertEqual(s.id, 1)
        animais = {a.id: a for a in self.animal_dao.listar(self.abrigo_id)}
        adotantes = {a.cpf: a for a in self.adotante_dao.listar()}
        (lida,) = self.solicitacao_dao.listar(animais, adotantes)
        self.assertIs(lida.animal, animais[gato.id])
        self.assertIs(lida.adotante, adotantes[adotante.cpf])
        self.assertEqual(lida.status, "Pendente")

    def test_listar_sem_argumentos_carrega_tudo(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        self.solicitacao_dao.inserir(SolicitacaoAdocao(gato, adotante))
        (lida,) = self.solicitacao_dao.listar()
        self.assertEqual((lida.animal.nome, lida.adotante.nome), ("Mimi", "Ana"))

    def test_nao_aceita_duas_pendentes_para_o_mesmo_animal(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        self.solicitacao_dao.inserir(SolicitacaoAdocao(gato, adotante))
        with self.assertRaisesRegex(ValueError, "pendente"):
            self.solicitacao_dao.inserir(SolicitacaoAdocao(gato, adotante))

    def test_apos_rejeitar_pode_haver_nova_pendente(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        primeira = SolicitacaoAdocao(gato, adotante)
        self.solicitacao_dao.inserir(primeira)
        primeira.rejeitar()
        self.solicitacao_dao.atualizar_estado(primeira)
        self.solicitacao_dao.inserir(SolicitacaoAdocao(gato, adotante))
        self.assertEqual([s.status for s in self.solicitacao_dao.listar()], ["Rejeitada", "Pendente"])

    def test_aprovar_grava_solicitacao_e_animal_na_mesma_transacao(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        s = SolicitacaoAdocao(gato, adotante)
        self.solicitacao_dao.inserir(s)
        s.aprovar()
        with transacao() as conn:
            self.solicitacao_dao.atualizar_estado(s, conn)
            self.animal_dao.atualizar_status(gato, conn)
        (lida,) = self.solicitacao_dao.listar()
        self.assertEqual((lida.status, lida.animal.status), ("Aprovada", "Adotado"))
        with self.assertRaises(ValueError):
            lida.rejeitar()

    def test_erro_dentro_da_transacao_desfaz_tudo(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        s = SolicitacaoAdocao(gato, adotante)
        self.solicitacao_dao.inserir(s)
        s.aprovar()
        with self.assertRaises(RuntimeError):
            with transacao() as conn:
                self.solicitacao_dao.atualizar_estado(s, conn)
                self.animal_dao.atualizar_status(gato, conn)
                raise RuntimeError("falha simulada")
        (lida,) = self.solicitacao_dao.listar()
        self.assertEqual((lida.status, lida.animal.status), ("Pendente", "Disponível"))

    def test_atualizar_estado_exige_solicitacao_gravada(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        with self.assertRaises(ValueError):
            self.solicitacao_dao.atualizar_estado(SolicitacaoAdocao(gato, adotante))

    def test_buscar_por_id(self):
        gato, adotante = self.novo_gato(), self.novo_adotante()
        s = SolicitacaoAdocao(gato, adotante)
        self.solicitacao_dao.inserir(s)
        self.assertEqual(self.solicitacao_dao.buscar_por_id(s.id).adotante.cpf, adotante.cpf)
        self.assertIsNone(self.solicitacao_dao.buscar_por_id(999))


class TesteConexao(unittest.TestCase):
    def test_conexao_invalida_vira_erro_banco(self):
        anterior = os.environ.get("DB_PORT")
        os.environ["DB_PORT"] = "1"
        try:
            with self.assertRaises(ErroBanco):
                conexao.conectar()
        finally:
            if anterior is None:
                os.environ.pop("DB_PORT", None)
            else:
                os.environ["DB_PORT"] = anterior


if __name__ == "__main__":
    unittest.main()
