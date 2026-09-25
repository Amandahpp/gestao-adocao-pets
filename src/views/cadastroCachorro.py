import tkinter as tk
from tkinter import ttk

class CadastroCachorroView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.title("Cadastrar Cachorro")
        self.geometry("280x220")

        ttk.Label(self, text="Nome:").pack(pady=(10, 2))
        self.ent_nome = ttk.Entry(self)
        self.ent_nome.pack()

        ttk.Label(self, text="Idade:").pack(pady=(5, 2))
        self.ent_idade = ttk.Entry(self)
        self.ent_idade.pack()

        ttk.Label(self, text="Sexo:").pack(pady=(5, 2))
        self.combo_sexo = ttk.Combobox(self, values=["Macho", "Fêmea"], state="readonly")
        self.combo_sexo.set("Macho")
        self.combo_sexo.pack()

        ttk.Label(self, text="Raça:").pack(pady=(5, 2))
        self.ent_raca = ttk.Entry(self)
        self.ent_raca.pack()

        ttk.Button(self, text="Salvar", command=self._salvar).pack(pady=15)

    def _salvar(self):
        nome = self.ent_nome.get().strip()
        idade = self.ent_idade.get().strip()
        sexo = self.combo_sexo.get()
        raca = self.ent_raca.get().strip()

        if self.controller is not None:
            ok = self.controller.cadastrar_cachorro(nome, idade, sexo, raca)
            if ok:
                self.destroy()
        else:
            self.destroy()
