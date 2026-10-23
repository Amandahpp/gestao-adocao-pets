"""Painel inicial responsivo: cartões em 1 ou 2 colunas conforme a largura."""
from tkinter import ttk
from src.views.theme import CARD_PALETTE


class MainView(ttk.Frame):
    ACTIONS = (
        ("🐶", "Cadastrar cachorro", "abrir_cad_cachorro"),
        ("🐱", "Cadastrar gato", "abrir_cad_gato"),
        ("🐾", "Consultar animais", "abrir_listagem_animais"),
        ("👤", "Cadastrar adotante", "abrir_cad_adotante"),
        ("💚", "Nova solicitação", "abrir_cad_solicitacao"),
        ("📋", "Gerenciar solicitações", "abrir_gerenciador_solicitacoes"),
    )

    def __init__(self, parent, controller):
        super().__init__(parent, padding=(28, 25))
        self.controller = controller
        self.pack(fill="both", expand=True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        header = ttk.Frame(self)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 24))
        ttk.Label(header, text="🐾  Patinhas Felizes", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="Gestão de adoções  •  Escolha uma ação para começar", style="Muted.TLabel").pack(anchor="w", pady=(6, 0))
        self.grid_area = ttk.Frame(self)
        self.grid_area.grid(row=1, column=0, sticky="nsew")
        self.grid_area.rowconfigure(0, weight=1)
        self.grid_area.columnconfigure(0, weight=1)
        self.cards = []
        for index, (emoji, title, action) in enumerate(self.ACTIONS):
            card = ttk.Frame(self.grid_area, style=f"Pet{index}.TFrame", padding=22)
            ttk.Label(card, text=emoji, style=f"Pet{index}.TLabel", font=("Segoe UI Emoji", 23)).pack(anchor="w")
            ttk.Label(card, text=title, style=f"Pet{index}.TLabel", font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=(10, 5))
            ttk.Button(card, text="Abrir  →", style=f"Pet{index}.TButton", command=getattr(controller, action)).pack(anchor="w", pady=(18, 0))
            self.cards.append(card)
        self._columns = None
        self.bind("<Configure>", self._on_resize)
        self._layout_cards(2)

    def _on_resize(self, event):
        if event.widget is self:
            self._layout_cards(2 if event.width >= 750 else 1)

    def _layout_cards(self, columns):
        if columns == self._columns:
            return
        self._columns = columns
        for card in self.cards:
            card.grid_forget()
        for column in range(2):
            self.grid_area.columnconfigure(column, weight=1 if column < columns else 0, uniform="cards" if column < columns else "")
        for row in range(6):
            self.grid_area.rowconfigure(row, weight=0)
        for i, card in enumerate(self.cards):
            card.grid(row=i // columns, column=i % columns, sticky="nsew", padx=8, pady=8)
