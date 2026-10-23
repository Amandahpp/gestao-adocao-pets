import unittest
from src.models.abrigo import Abrigo
from src.models.animal_factory import AnimalFactory
from src.models.adotante import Adotante
from src.models.solicitacao_adocao import SolicitacaoAdocao

class TesteModelos(unittest.TestCase):
    def setUp(self):
        # Isola o Singleton entre testes, sem alterar o código de produção.
        Abrigo._instancia = None
        self.abrigo = Abrigo("Teste")
        self.animal = AnimalFactory.criar_animal("gato", 1, "Mimi", 2, "Fêmea", "Curta")
        self.adotante = Adotante("Ana", "12345678901", "9999-9999")
        self.abrigo.cadastrar_animal(self.animal)

    def test_factory_cria_tipo_correto(self):
        self.assertEqual(type(self.animal).__name__, "Gato")
        self.assertEqual(type(AnimalFactory.criar_animal("cachorro", 2, "Bob", 1, "Macho", "SRD")).__name__, "Cachorro")

    def test_singleton(self):
        self.assertIs(self.abrigo, Abrigo("Outro nome"))
        self.assertEqual(Abrigo().nome, "Teste")

    def test_aprovar_altera_status(self):
        s = SolicitacaoAdocao(self.animal, self.adotante)
        self.abrigo.cadastrar_solicitacao(s)
        s.aprovar()
        self.assertEqual(s.status, "Aprovada")
        self.assertEqual(self.animal.status, "Adotado")
        with self.assertRaises(ValueError): s.rejeitar()

    def test_rejeitar_nao_adota(self):
        s = SolicitacaoAdocao(self.animal, self.adotante)
        self.abrigo.cadastrar_solicitacao(s)
        s.rejeitar()
        self.assertEqual(s.status, "Rejeitada")
        self.assertEqual(self.animal.status, "Disponível")
        with self.assertRaises(ValueError): s.aprovar()

    def test_nao_aceita_duas_pendentes(self):
        self.abrigo.cadastrar_solicitacao(SolicitacaoAdocao(self.animal, self.adotante))
        with self.assertRaises(ValueError):
            self.abrigo.cadastrar_solicitacao(SolicitacaoAdocao(self.animal, self.adotante))

    def test_nao_aceita_adotado(self):
        self.animal.status = "Adotado"
        with self.assertRaises(ValueError):
            self.abrigo.cadastrar_solicitacao(SolicitacaoAdocao(self.animal, self.adotante))

    def test_idade_invalida(self):
        with self.assertRaises(ValueError):
            AnimalFactory.criar_animal("gato", 3, "Luna", -1, "Fêmea", "Longa")

    def test_cpf_invalido(self):
        with self.assertRaises(ValueError): Adotante("João", "123", "999")

    def test_id_duplicado(self):
        with self.assertRaises(ValueError): self.abrigo.cadastrar_animal(self.animal)

if __name__ == "__main__": unittest.main()
