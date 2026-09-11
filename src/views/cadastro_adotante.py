import tkinter as tk
from tkinter import ttk

# import feio pq deu erro
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from src.controllers.adotante_controller import AdotanteController

# criacao da view para a tela de cadastro de adotante
class CadastroAdotanteView(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, padding="15")

        self.controller = controller

        self.pack(fill="both", expand=True)

        # titulo principal "Cadastrar Adotante"
        label_titulo = ttk.Label(
            self,
            text="Cadastrar Adotante",
            font=("Helvetica", 14, "bold")
        )

        label_titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0,15)
        )

        # campo "Nome"
        label_nome = ttk.Label(
            self,
            text="Nome:"
        )

        label_nome.grid(
            row=1,
            column=0,
            sticky="w",
            pady=4
        )

        self.entry_nome = ttk.Entry(self)

        self.entry_nome.grid(
            row=1,
            column=1,
            sticky="ew",
            pady=4
        )

        # campo "CPF"
        label_cpf = ttk.Label(
            self,
            text="CPF:"
        )

        label_cpf.grid(
            row=2,
            column=0,
            sticky="w",
            pady=4
        )

        self.entry_cpf = ttk.Entry(self)

        self.entry_cpf.grid(
            row=2,
            column=1,
            sticky="ew",
            pady=4
        )

        # campo "Telefone"
        label_telefone = ttk.Label(
            self,
            text="Telefone:"
        )

        label_telefone.grid(
            row=3,
            column=0,
            sticky="w",
            pady=4
        )

        self.entry_telefone = ttk.Entry(self)

        self.entry_telefone.grid(
            row=3,
            column=1,
            sticky="ew",
            pady=4
        )

        # botao "Cadastrar"
        botao_cadastrar = ttk.Button(
            self,
            text="Cadastrar",
            command=self.cadastrar
        )

        botao_cadastrar.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(15,4)
        )

    # pega os dados da View para enviar ao Controller
    def cadastrar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        telefone = self.entry_telefone.get()

        self.controller.cadastrar_adotante(
            nome,
            cpf,
            telefone
        )





# teste

if __name__ == "__main__":
    root = tk.Tk()

    root.title("Cadastro de Adotante")
    root.geometry("400x300")

    controller = AdotanteController()

    app = CadastroAdotanteView(root, controller)

    root.mainloop()