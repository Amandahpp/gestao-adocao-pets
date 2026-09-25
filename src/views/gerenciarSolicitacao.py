import tkinter as tk
from tkinter import ttk, messagebox


class GerenciadorSolicitacoesView(tk.Toplevel):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller

        self.title("Gerenciar Solicitações")
        self.geometry("450x260")

        self.tabela = ttk.Treeview(
            self, columns=("adotante", "animal", "status"), show="headings", height=6
        )
        self.tabela.heading("adotante", text="Adotante")
        self.tabela.heading("animal", text="Animal")
        self.tabela.heading("status", text="Status")
        self.tabela.pack(pady=10, padx=10, fill="both", expand=True)

        frame_btn = ttk.Frame(self)
        frame_btn.pack(pady=5)
        ttk.Button(frame_btn, text="Aprovar", command=self._aprovar).pack(side="left", padx=5)
        ttk.Button(frame_btn, text="Reprovar", command=self._reprovar).pack(side="left", padx=5)
        ttk.Button(frame_btn, text="Fechar", command=self.destroy).pack(side="left", padx=5)

        self._carregar_dados()

    def _carregar_dados(self):
        self.tabela.delete(*self.tabela.get_children())

        if self.controller is None:
            return

        for indice, solicitacao in enumerate(self.controller.abrigo.solicitacoes):
            texto = solicitacao.exibir()
            animal_nome, resto = texto.split(" -> ", 1)
            adotante_nome, estado = resto.split(" | ", 1)
            self.tabela.insert(
                "", "end", iid=str(indice), values=(adotante_nome, animal_nome, estado)
            )

    def _solicitacao_selecionada(self):
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma solicitação na tabela.")
            return None
        indice = int(selecao[0])
        return self.controller.abrigo.solicitacoes[indice]

    def _aprovar(self):
        solicitacao = self._solicitacao_selecionada()
        if solicitacao is None:
            return
        solicitacao.aprovar()
        self._carregar_dados()

    def _reprovar(self):
        solicitacao = self._solicitacao_selecionada()
        if solicitacao is None:
            return
        solicitacao.rejeitar()
        self._carregar_dados()
