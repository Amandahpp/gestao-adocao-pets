import tkinter as tk
from tkinter import ttk

class CadastroGatoView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller

        self.title("Cadastrar Gato")
        self.geometry("300x240")
        self.resizable(False, False)

        self._build_interface()

    def _build_interface(self):
        frame = ttk.Frame(self, padding="15")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w", pady=4)
        self.ent_nome = ttk.Entry(frame)
        self.ent_nome.grid(row=0, column=1, sticky="ew", pady=4)

        ttk.Label(frame, text="Idade:").grid(row=1, column=0, sticky="w", pady=4)
        self.ent_idade = ttk.Entry(frame)
        self.ent_idade.grid(row=1, column=1, sticky="ew", pady=4)

        ttk.Label(frame, text="Sexo:").grid(row=2, column=0, sticky="w", pady=4)
        self.combo_sexo = ttk.Combobox(frame, values=["Macho", "Fêmea"], state="readonly")
        self.combo_sexo.set("Macho")
        self.combo_sexo.grid(row=2, column=1, sticky="ew", pady=4)

        ttk.Label(frame, text="Pelagem:").grid(row=3, column=0, sticky="w", pady=4)
        self.ent_pelagem = ttk.Entry(frame)
        self.ent_pelagem.grid(row=3, column=1, sticky="ew", pady=4)

        frame.columnconfigure(1, weight=1)

        ttk.Button(frame, text="Salvar", command=self._salvar).grid(row=4, column=0, columnspan=2, pady=(15, 0))

    def _salvar(self):
        nome = self.ent_nome.get().strip()
        idade = self.ent_idade.get().strip()
        sexo = self.combo_sexo.get()
        pelagem = self.ent_pelagem.get().strip()

        if self.controller is not None:
            ok = self.controller.cadastrar_gato(nome, idade, sexo, pelagem)
            if ok:
                self.destroy()
        else:
            self.destroy()
