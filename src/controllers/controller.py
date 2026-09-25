from tkinter import messagebox

from src.models.abrigo import Abrigo
from src.models.animal_factory import AnimalFactory
from src.models.adotante import Adotante
from src.models.solicitacao_adocao import SolicitacaoAdocao

from src.views.main_menu import MainView
from src.views.cadastroCachorro import CadastroCachorroView
from src.views.cadastroGato import CadastroGatoView
from src.views.cadastroAdotante import CadastroAdotanteView
from src.views.cadastroSolicitacao import CadastroSolicitacaoView
from src.views.listagemAnimais import ListagemAnimaisView
from src.views.gerenciarSolicitacao import GerenciadorSolicitacoesView


class Controller:
    """Liga as telas (views) do tkinter com as classes de negócio (model)."""

    def __init__(self, root):
        self.root = root
        self.abrigo = Abrigo("Patinhas Felizes")
        self.adotantes = []
        self._proximo_id = 1

        self.main_view = MainView(root, self)

    def _gerar_id(self):
        novo_id = self._proximo_id
        self._proximo_id += 1
        return novo_id

    # ---------------- Animais ----------------
    def abrir_cad_cachorro(self):
        CadastroCachorroView(self.root, self)

    def abrir_cad_gato(self):
        CadastroGatoView(self.root, self)

    def cadastrar_cachorro(self, nome, idade, sexo, raca):
        if not nome or not idade:
            messagebox.showwarning("Atenção", "Preencha nome e idade.")
            return False
        try:
            idade = int(idade)
        except ValueError:
            messagebox.showwarning("Atenção", "Idade deve ser um número.")
            return False

        animal = AnimalFactory.criar_animal(
            "cachorro", self._gerar_id(), nome, idade, sexo, raca
        )
        self.abrigo.cadastrar_animal(animal)
        messagebox.showinfo("Sucesso", f"Cachorro '{nome}' cadastrado!")
        return True

    def cadastrar_gato(self, nome, idade, sexo, pelagem):
        if not nome or not idade:
            messagebox.showwarning("Atenção", "Preencha nome e idade.")
            return False
        try:
            idade = int(idade)
        except ValueError:
            messagebox.showwarning("Atenção", "Idade deve ser um número.")
            return False

        animal = AnimalFactory.criar_animal(
            "gato", self._gerar_id(), nome, idade, sexo, pelagem
        )
        self.abrigo.cadastrar_animal(animal)
        messagebox.showinfo("Sucesso", f"Gato '{nome}' cadastrado!")
        return True

    def abrir_listagem_animais(self):
        ListagemAnimaisView(self.root, self)

    # ---------------- Adotantes ----------------
    def abrir_cad_adotante(self):
        CadastroAdotanteView(self.root, self)

    def cadastrar_adotante(self, nome, cpf, telefone):
        if not nome or not cpf:
            messagebox.showwarning("Atenção", "Preencha nome e CPF.")
            return False

        adotante = Adotante(nome, cpf, telefone)
        self.adotantes.append(adotante)
        messagebox.showinfo("Sucesso", f"Adotante '{nome}' cadastrado!")
        return True

    # ---------------- Solicitações ----------------
    def abrir_cad_solicitacao(self):
        if not self.abrigo.animais:
            messagebox.showwarning("Atenção", "Cadastre um animal antes.")
            return
        if not self.adotantes:
            messagebox.showwarning("Atenção", "Cadastre um adotante antes.")
            return
        CadastroSolicitacaoView(self.root, self)

    def cadastrar_solicitacao(self, indice_animal, indice_adotante):
        animal = self.abrigo.animais[indice_animal]
        adotante = self.adotantes[indice_adotante]
        solicitacao = SolicitacaoAdocao(animal, adotante)
        self.abrigo.cadastrar_solicitacao(solicitacao)
        messagebox.showinfo("Sucesso", "Solicitação registrada!")

    def abrir_gerenciador_solicitacoes(self):
        if not self.abrigo.solicitacoes:
            messagebox.showinfo("Info", "Não há solicitações cadastradas.")
            return
        GerenciadorSolicitacoesView(self.root, self)
