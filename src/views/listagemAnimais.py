import tkinter as tk
from tkinter import ttk
from src.views.theme import center_window, form_shell


class ListagemAnimaisView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.title("Animais cadastrados")
        center_window(self, 850, 560)
        card = form_shell(self, "Animais cadastrados", "Consulte os animais registrados e sua disponibilidade.")
        card.rowconfigure(0, weight=1)
        self.tabela = ttk.Treeview(card, columns=("nome", "tipo", "idade", "status"), show="headings")
        for col, title in (("nome", "Nome"), ("tipo", "Tipo"), ("idade", "Idade"), ("status", "Status")):
            self.tabela.heading(col, text=title)
            self.tabela.column(col, minwidth=75, width=140, stretch=True)
        self.tabela.grid(row=0, column=0, columnspan=2, sticky="nsew")
        scrollbar = ttk.Scrollbar(card, orient="vertical", command=self.tabela.yview)
        scrollbar.grid(row=0, column=2, sticky="ns")
        self.tabela.configure(yscrollcommand=scrollbar.set)
        ttk.Button(card, text="Fechar", command=self.destroy).grid(row=1, column=1, sticky="e", pady=(16, 0))
        self._carregar_dados()

    def _carregar_dados(self):
        if self.controller is None:
            return
        self.tabela.delete(*self.tabela.get_children())
        for animal in self.controller.abrigo.animais:
            self.tabela.insert("", "end", values=(animal.nome, type(animal).__name__, animal.idade, animal.status))
