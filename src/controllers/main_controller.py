import tkinter as tk

from src.controllers.adotante_controller import AdotanteController
from src.views.cadastro_adotante import CadastroAdotanteView

class MainController:

    def __init__(self, root):
        self.root = root
        self.adotante_controller = AdotanteController()

    def abrir_cad_adotante(self):
        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Adotante")
        janela.geometry("400x300")

        CadastroAdotanteView(
            janela,
            self.adotante_controller
        )