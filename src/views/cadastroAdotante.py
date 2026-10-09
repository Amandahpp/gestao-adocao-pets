from tkinter import ttk
import tkinter as tk
from src.views.theme import center_window, form_shell, form_field


class CadastroAdotanteView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.title("Cadastrar adotante")
        center_window(self, 620, 460)
        card = form_shell(self, "Cadastrar adotante", "Informe os dados de contato da pessoa.")
        self.ent_nome = ttk.Entry(card)
        form_field(card, 0, "Nome", self.ent_nome)
        self.ent_cpf = ttk.Entry(card)
        form_field(card, 1, "CPF", self.ent_cpf)
        self.ent_telefone = ttk.Entry(card)
        form_field(card, 2, "Telefone", self.ent_telefone)
        ttk.Button(card, text="Salvar cadastro", style="Accent.TButton", command=self._salvar).grid(row=3, column=1, sticky="e", pady=(20, 0))
        self.ent_nome.focus_set()

    def _salvar(self):
        if self.controller is None:
            return
        if self.controller.cadastrar_adotante(self.ent_nome.get().strip(), self.ent_cpf.get().strip(), self.ent_telefone.get().strip()):
            self.destroy()
