import tkinter as tk
from tkinter import ttk

class GerenciadorSolicitacoesView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gerenciar Solicitações")
        self.geometry("400x220")

        self.tabela = ttk.Treeview(self, columns=("adotante", "animal", "status"), show="headings", height=5)
        self.tabela.heading("adotante", text="Adotante")
        self.tabela.heading("animal", text="Animal")
        self.tabela.heading("status", text="Status")

        self.tabela.insert("", "end", values=("Ana Silva", "Rex", "Pendente"))
        self.tabela.insert("", "end", values=("Carlos Souza", "Mingau", "Pendente"))

        self.tabela.pack(pady=10, padx=10, fill="both", expand=True)

        frame_btn = ttk.Frame(self)
        frame_btn.pack(pady=5)
        ttk.Button(frame_btn, text="Aprovar", command=self.destroy).pack(side="left", padx=5)
        ttk.Button(frame_btn, text="Reprovar", command=self.destroy).pack(side="left", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = GerenciadorSolicitacoesView(root)
    root.mainloop()