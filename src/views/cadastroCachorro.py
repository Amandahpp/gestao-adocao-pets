import tkinter as tk
from tkinter import ttk

class CadastroCachorroView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
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

        ttk.Button(self, text="Salvar", command=self.destroy).pack(pady=15)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = CadastroCachorroView(root)
    root.mainloop()