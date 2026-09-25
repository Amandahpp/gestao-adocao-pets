import tkinter as tk
from tkinter import ttk


class ListagemAnimaisView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller

        self.title("Animais Cadastrados")
        self.geometry("420x260")

        self._build_interface()
        self._carregar_dados()

    def _build_interface(self):
        self.tabela = ttk.Treeview(
            self,
            columns=("nome", "tipo", "idade", "status"),
            show="headings",
            height=8,
        )
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("tipo", text="Tipo")
        self.tabela.heading("idade", text="Idade")
        self.tabela.heading("status", text="Status")
        self.tabela.pack(pady=10, padx=10, fill="both", expand=True)

        ttk.Button(self, text="Fechar", command=self.destroy).pack(pady=(0, 10))

    def _carregar_dados(self):
        if self.controller is None:
            return

        for animal in self.controller.abrigo.animais:
            tipo = type(animal).__name__
            self.tabela.insert(
                "", "end", values=(animal.nome, tipo, animal.idade, animal.status)
            )
