import tkinter as tk
from tkinter import ttk

class MainView(ttk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent, padding="15")
        self.controller = controller
        self.pack(fill="both", expand=True)

        #Título principal
        label_titulo = ttk.Label(
            self,
            text="Sistema de Adoção Patinhas Felizes",
            font=("Helvetica", 14, "bold")
        )
        label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        #Chamada para criar os botões
        self._criar_botoes()

    def _criar_botoes(self) -> None:
        menu_items = [
            ("Cadastrar Cachorro", getattr(self.controller, "abrir_cad_cachorro", None)),
            ("Cadastrar Gato", getattr(self.controller, "abrir_cad_gato", None)),
            ("Listar Animais", getattr(self.controller, "abrir_listagem_animais", None)),
            ("Cadastrar Adotante", getattr(self.controller, "abrir_cad_adotante", None)),
            ("Nova Solicitação", getattr(self.controller, "abrir_cad_solicitacao", None)),
            ("Gerenciar Solicitações", getattr(self.controller, "abrir_gerenciador_solicitacoes", None)),
        ]

        for i, (texto, comando) in enumerate(menu_items):
            btn = ttk.Button(self, text=texto, command=comando)
            btn.grid(row=i + 1, column=0, sticky="ew", pady=4)
