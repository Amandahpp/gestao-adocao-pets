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
    """Coordena as ações da interface e as regras do domínio (MVC)."""
    def __init__(self, root):
        self.root = root
        self.abrigo = Abrigo("Patinhas Felizes")
        self.adotantes = []
        self._proximo_id = max((a.id for a in self.abrigo.animais), default=0) + 1
        self.main_view = MainView(root, self)

    def _gerar_id(self):
        resultado = self._proximo_id
        self._proximo_id += 1
        return resultado

    def abrir_cad_cachorro(self): CadastroCachorroView(self.root, self)
    def abrir_cad_gato(self): CadastroGatoView(self.root, self)
    def abrir_listagem_animais(self): ListagemAnimaisView(self.root, self)
    def abrir_cad_adotante(self): CadastroAdotanteView(self.root, self)

    def _cadastrar_animal(self, tipo, nome, idade, sexo, detalhe):
        try:
            if not str(idade).strip().isdigit():
                raise ValueError("A idade deve ser um número inteiro não negativo.")
            if not str(detalhe).strip():
                raise ValueError("Preencha todos os campos do animal.")
            animal = AnimalFactory.criar_animal(tipo, self._proximo_id, nome, int(idade), sexo, detalhe)
            self.abrigo.cadastrar_animal(animal)
            self._gerar_id()
        except ValueError as erro:
            messagebox.showwarning("Dados inválidos", str(erro))
            return False
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()} '{animal.nome}' cadastrado!")
        return True

    def cadastrar_cachorro(self, nome, idade, sexo, raca):
        return self._cadastrar_animal("cachorro", nome, idade, sexo, raca)

    def cadastrar_gato(self, nome, idade, sexo, pelagem):
        return self._cadastrar_animal("gato", nome, idade, sexo, pelagem)

    def cadastrar_adotante(self, nome, cpf, telefone):
        try:
            adotante = Adotante(nome, cpf, telefone)
            if any(a.cpf == adotante.cpf for a in self.adotantes):
                raise ValueError("Já existe um adotante com esse CPF.")
            self.adotantes.append(adotante)
        except ValueError as erro:
            messagebox.showwarning("Dados inválidos", str(erro))
            return False
        messagebox.showinfo("Sucesso", f"Adotante '{adotante.nome}' cadastrado!")
        return True

    def abrir_cad_solicitacao(self):
        if not any(a.status == "Disponível" and not any(s.animal is a and s.status == "Pendente" for s in self.abrigo.solicitacoes) for a in self.abrigo.animais):
            messagebox.showwarning("Atenção", "Não há animais disponíveis sem solicitação pendente.")
            return
        if not self.adotantes:
            messagebox.showwarning("Atenção", "Cadastre um adotante antes.")
            return
        CadastroSolicitacaoView(self.root, self)

    def cadastrar_solicitacao(self, indice_animal, indice_adotante):
        try:
            animal = self.abrigo.animais[indice_animal]
            adotante = self.adotantes[indice_adotante]
            self.abrigo.cadastrar_solicitacao(SolicitacaoAdocao(animal, adotante))
        except (IndexError, ValueError) as erro:
            messagebox.showwarning("Atenção", str(erro))
            return False
        messagebox.showinfo("Sucesso", "Solicitação registrada!")
        return True

    def alterar_solicitacao(self, indice, acao):
        try:
            solicitacao = self.abrigo.solicitacoes[indice]
            if acao == "aprovar": solicitacao.aprovar()
            elif acao == "rejeitar": solicitacao.rejeitar()
            else: raise ValueError("Ação desconhecida.")
        except (IndexError, ValueError) as erro:
            messagebox.showwarning("Atenção", str(erro))
            return False
        messagebox.showinfo("Sucesso", "Solicitação atualizada!")
        return True

    def abrir_gerenciador_solicitacoes(self):
        if not self.abrigo.solicitacoes:
            messagebox.showinfo("Informação", "Não há solicitações cadastradas.")
            return
        GerenciadorSolicitacoesView(self.root, self)
