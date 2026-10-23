import tkinter as tk
from tkinter import ttk, messagebox
from src.views.theme import center_window, form_shell


class GerenciadorSolicitacoesView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Gerenciar solicitações")
        center_window(self, 900, 570)
        card = form_shell(self, "Gerenciar solicitações", "Selecione um pedido para aprovar ou rejeitar.")
        card.rowconfigure(0, weight=1)
        self.tabela = ttk.Treeview(card, columns=("adotante", "animal", "status"), show="headings")
        for coluna, titulo in (("adotante", "Adotante"), ("animal", "Animal"), ("status", "Situação")):
            self.tabela.heading(coluna, text=titulo)
            self.tabela.column(coluna, minwidth=110, width=170, stretch=True)
        self.tabela.grid(row=0, column=0, columnspan=3, sticky="nsew")
        scrollbar = ttk.Scrollbar(card, orient="vertical", command=self.tabela.yview)
        scrollbar.grid(row=0, column=3, sticky="ns")
        self.tabela.configure(yscrollcommand=scrollbar.set)
        botoes = ttk.Frame(card, style="Card.TFrame")
        botoes.grid(row=1, column=0, columnspan=3, sticky="e", pady=(16, 0))
        ttk.Button(botoes, text="Aprovar", style="Accent.TButton", command=lambda: self._alterar("aprovar")).pack(side="left", padx=5)
        ttk.Button(botoes, text="Rejeitar", command=lambda: self._alterar("rejeitar")).pack(side="left", padx=5)
        ttk.Button(botoes, text="Fechar", command=self.destroy).pack(side="left", padx=5)
        self._carregar_dados()

    def _carregar_dados(self):
        self.tabela.delete(*self.tabela.get_children())
        for indice, solicitacao in enumerate(self.controller.abrigo.solicitacoes):
            self.tabela.insert("", "end", iid=str(indice), values=(solicitacao.adotante.nome, solicitacao.animal.nome, solicitacao.status))

    def _alterar(self, acao):
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma solicitação.")
            return
        if self.controller.alterar_solicitacao(int(selecao[0]), acao):
            self._carregar_dados()
