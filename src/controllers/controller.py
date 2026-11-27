from tkinter import messagebox
from database.conexao import transacao, ErroBanco
from dao.abrigo_dao import AbrigoDAO
from dao.adotante_dao import AdotanteDAO
from dao.animal_dao import AnimalDAO
from dao.solicitacaoAdocao_dao import SolicitacaoAdocaoDAO
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

NOME_ABRIGO = "Patinhas Felizes"


class Controller:
    """Coordena as ações da interface e as regras do domínio (MVC).

    Os dados ficam gravados no PostgreSQL (via DAOs). As listas em memória
    (`abrigo.animais`, `abrigo.solicitacoes`, `adotantes`) são um espelho do banco,
    carregado na abertura e atualizado a cada operação bem-sucedida.
    """

    def __init__(self, root):
        self.root = root
        self.abrigo_dao = AbrigoDAO()
        self.adotante_dao = AdotanteDAO()
        self.animal_dao = AnimalDAO()
        self.solicitacao_dao = SolicitacaoAdocaoDAO()
        self.abrigo = Abrigo(NOME_ABRIGO)
        self.adotantes = []
        try:
            self._carregar_do_banco()
        except ErroBanco as erro:
            messagebox.showerror(
                "Banco de dados indisponível",
                f"{erro}\n\nVerifique se o PostgreSQL está rodando, se o banco foi criado "
                "(database/banco.sql) e se as variáveis DB_HOST, DB_PORT, DB_NAME, "
                "DB_USER e DB_PASSWORD estão corretas.")
            raise SystemExit(1)
        self.main_view = MainView(root, self)

    # ---------- carga inicial ----------
    def _carregar_do_banco(self):
        self.abrigo_id = self.abrigo_dao.obter_ou_criar(NOME_ABRIGO)
        animais = self.animal_dao.listar(self.abrigo_id)
        self.adotantes = self.adotante_dao.listar()
        solicitacoes = self.solicitacao_dao.listar(
            {a.id: a for a in animais}, {a.cpf: a for a in self.adotantes})
        for animal in animais:
            if animal not in self.abrigo.animais:
                self.abrigo.cadastrar_animal(animal)
        # Já foram validadas quando gravadas (inclui aprovadas/rejeitadas), então não revalida.
        for solicitacao in solicitacoes:
            self.abrigo.restaurar_solicitacao(solicitacao)

    def _erro_banco(self, erro):
        messagebox.showerror("Erro no banco de dados", str(erro))

    # ---------- telas ----------
    def abrir_cad_cachorro(self): CadastroCachorroView(self.root, self)
    def abrir_cad_gato(self): CadastroGatoView(self.root, self)
    def abrir_listagem_animais(self): ListagemAnimaisView(self.root, self)
    def abrir_cad_adotante(self): CadastroAdotanteView(self.root, self)

    # ---------- animais ----------
    def _cadastrar_animal(self, tipo, nome, idade, sexo, detalhe):
        try:
            if not str(idade).strip().isdigit():
                raise ValueError("A idade deve ser um número inteiro não negativo.")
            if not str(detalhe).strip():
                raise ValueError("Preencha todos os campos do animal.")
            # id=None: quem gera o id é o banco (o DAO preenche `animal.id` ao inserir).
            animal = AnimalFactory.criar_animal(tipo, None, nome, int(idade), sexo, detalhe)
            self.animal_dao.inserir(animal, self.abrigo_id)
            self.abrigo.cadastrar_animal(animal)
        except ValueError as erro:
            messagebox.showwarning("Dados inválidos", str(erro))
            return False
        except ErroBanco as erro:
            self._erro_banco(erro)
            return False
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()} '{animal.nome}' cadastrado!")
        return True

    def cadastrar_cachorro(self, nome, idade, sexo, raca):
        return self._cadastrar_animal("cachorro", nome, idade, sexo, raca)

    def cadastrar_gato(self, nome, idade, sexo, pelagem):
        return self._cadastrar_animal("gato", nome, idade, sexo, pelagem)

    # ---------- adotantes ----------
    def cadastrar_adotante(self, nome, cpf, telefone):
        try:
            adotante = Adotante(nome, cpf, telefone)
            if any(a.cpf == adotante.cpf for a in self.adotantes):
                raise ValueError("Já existe um adotante com esse CPF.")
            self.adotante_dao.inserir(adotante)
            self.adotantes.append(adotante)
        except ValueError as erro:
            messagebox.showwarning("Dados inválidos", str(erro))
            return False
        except ErroBanco as erro:
            self._erro_banco(erro)
            return False
        messagebox.showinfo("Sucesso", f"Adotante '{adotante.nome}' cadastrado!")
        return True

    # ---------- solicitações ----------
    def abrir_cad_solicitacao(self):
        if not any(a.status == "Disponível" and not any(s.animal is a and s.status == "Pendente" for s in self.abrigo.solicitacoes) for a in self.abrigo.animais):
            messagebox.showwarning("Atenção", "Não há animais disponíveis sem solicitação pendente.")
            return
        if not self.adotantes:
            messagebox.showwarning("Atenção", "Cadastre um adotante antes.")
            return
        CadastroSolicitacaoView(self.root, self)

    def cadastrar_solicitacao(self, indice_animal, indice_adotante):
        solicitacao = None
        try:
            animal = self.abrigo.animais[indice_animal]
            adotante = self.adotantes[indice_adotante]
            solicitacao = SolicitacaoAdocao(animal, adotante)
            self.abrigo.cadastrar_solicitacao(solicitacao)  # valida as regras e adiciona em memória
            try:
                self.solicitacao_dao.inserir(solicitacao)
            except Exception:
                self.abrigo.remover_solicitacao(solicitacao)  # desfaz a memória se o banco falhar
                raise
        except (IndexError, ValueError) as erro:
            messagebox.showwarning("Atenção", str(erro))
            return False
        except ErroBanco as erro:
            self._erro_banco(erro)
            return False
        messagebox.showinfo("Sucesso", "Solicitação registrada!")
        return True

    def alterar_solicitacao(self, indice, acao):
        solicitacao = None
        estado_anterior = status_animal_anterior = None
        try:
            solicitacao = self.abrigo.solicitacoes[indice]
            animal = solicitacao.animal
            estado_anterior, status_animal_anterior = solicitacao.estado, animal.status
            if acao == "aprovar": solicitacao.aprovar()
            elif acao == "rejeitar": solicitacao.rejeitar()
            else: raise ValueError("Ação desconhecida.")
            try:
                # Solicitação e animal são gravados juntos: ou os dois, ou nenhum.
                with transacao() as conn:
                    self.solicitacao_dao.atualizar_estado(solicitacao, conn)
                    self.animal_dao.atualizar_status(animal, conn)
            except Exception:
                solicitacao.estado = estado_anterior  # desfaz a memória se o banco falhar
                animal.status = status_animal_anterior
                raise
        except (IndexError, ValueError) as erro:
            messagebox.showwarning("Atenção", str(erro))
            return False
        except ErroBanco as erro:
            self._erro_banco(erro)
            return False
        messagebox.showinfo("Sucesso", "Solicitação atualizada!")
        return True

    def abrir_gerenciador_solicitacoes(self):
        if not self.abrigo.solicitacoes:
            messagebox.showinfo("Informação", "Não há solicitações cadastradas.")
            return
        GerenciadorSolicitacoesView(self.root, self)
