import tkinter as tk
from tkinter import ttk


class CadastroSolicitacaoView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller

        self.title("Nova Solicitação")
        self.geometry("300x200")

        self._animais_labels = []
        self._adotantes_labels = []

        ttk.Label(self, text="Animal:").pack(pady=(10, 2))
        self.combo_animal = ttk.Combobox(self, values=[], state="readonly")
        self.combo_animal.pack()

        ttk.Label(self, text="Adotante:").pack(pady=(5, 2))
        self.combo_adotante = ttk.Combobox(self, values=[], state="readonly")
        self.combo_adotante.pack()

        ttk.Button(self, text="Enviar", command=self._enviar).pack(pady=15)

        self._carregar_dados()

    def _carregar_dados(self):
        if self.controller is None:
            return

        self._animais_labels = [
            f"{a.nome} ({type(a).__name__})" for a in self.controller.abrigo.animais
        ]
        self._adotantes_labels = [a.nome for a in self.controller.adotantes]

        self.combo_animal["values"] = self._animais_labels
        self.combo_adotante["values"] = self._adotantes_labels

        if self._animais_labels:
            self.combo_animal.current(0)
        if self._adotantes_labels:
            self.combo_adotante.current(0)

    def _enviar(self):
        indice_animal = self.combo_animal.current()
        indice_adotante = self.combo_adotante.current()

        if indice_animal < 0 or indice_adotante < 0:
            return

        if self.controller is not None:
            self.controller.cadastrar_solicitacao(indice_animal, indice_adotante)

        self.destroy()
