from tkinter import ttk
import tkinter as tk
from src.views.theme import center_window, form_shell, form_field


class CadastroCachorroView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.title("Cadastrar cachorro")
        center_window(self, 620, 460)
        card = form_shell(self, "Cadastrar cachorro", "Preencha os dados do cachorro.")
        self.ent_nome = ttk.Entry(card)
        form_field(card, 0, "Nome", self.ent_nome)
        self.ent_idade = ttk.Entry(card)
        form_field(card, 1, "Idade (anos)", self.ent_idade)
        self.combo_sexo = ttk.Combobox(card, values=["Macho", "Fêmea"], state="readonly")
        self.combo_sexo.current(0)
        form_field(card, 2, "Sexo", self.combo_sexo)
        self.ent_raca = ttk.Entry(card)
        form_field(card, 3, "Raça", self.ent_raca)
        ttk.Button(card, text="Salvar cadastro", style="Accent.TButton", command=self._salvar).grid(row=4, column=1, sticky="e", pady=(20, 0))
        self.ent_nome.focus_set()

    def _salvar(self):
        if self.controller is None:
            return
        if self.controller.cadastrar_cachorro(self.ent_nome.get().strip(), self.ent_idade.get().strip(), self.combo_sexo.get(), self.ent_raca.get().strip()):
            self.destroy()
