import tkinter as tk
from tkinter import ttk


class CadastroAdotanteView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller

        self.title("Cadastrar Adotante")
        self.geometry("300x220")
        self.resizable(False, False)

        self._build_interface()

    def _build_interface(self):
        frame = ttk.Frame(self, padding="15")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w", pady=4)
        self.ent_nome = ttk.Entry(frame)
        self.ent_nome.grid(row=0, column=1, sticky="ew", pady=4)

        ttk.Label(frame, text="CPF:").grid(row=1, column=0, sticky="w", pady=4)
        self.ent_cpf = ttk.Entry(frame)
        self.ent_cpf.grid(row=1, column=1, sticky="ew", pady=4)

        ttk.Label(frame, text="Telefone:").grid(row=2, column=0, sticky="w", pady=4)
        self.ent_telefone = ttk.Entry(frame)
        self.ent_telefone.grid(row=2, column=1, sticky="ew", pady=4)

        frame.columnconfigure(1, weight=1)

        ttk.Button(frame, text="Salvar", command=self._salvar).grid(
            row=3, column=0, columnspan=2, pady=(15, 0)
        )

    def _salvar(self):
        nome = self.ent_nome.get().strip()
        cpf = self.ent_cpf.get().strip()
        telefone = self.ent_telefone.get().strip()

        if self.controller is not None:
            ok = self.controller.cadastrar_adotante(nome, cpf, telefone)
            if ok:
                self.destroy()
        else:
            self.destroy()
