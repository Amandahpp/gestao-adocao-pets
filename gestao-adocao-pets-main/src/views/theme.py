"""Tema visual único da aplicação (Tkinter/ttk, sem dependências externas)."""
import tkinter as tk
from tkinter import ttk

BG = "#F8FAFD"
WHITE = "#FFFFFF"
INK = "#253B55"
MUTED = "#66778D"
GREEN = "#287BC4"
GREEN_DARK = "#205F99"
PALE = "#E7F1FC"
BORDER = "#DCE5EF"


# Tons pastéis dos seis cartões da tela inicial.
CARD_PALETTE = (
    ("#E3F1FF", "#287BC4"),  # cachorro: azul
    ("#FFF0E3", "#E97927"),  # gato: laranja
    ("#E5F3E8", "#39875D"),  # animais: verde
    ("#FFE8F0", "#D95782"),  # adotante: rosa
    ("#FFF1D9", "#DB8A27"),  # nova solicitação: amarelo-alaranjado
    ("#EEE7FA", "#8060B8"),  # gerenciar: lilás
)


def apply_theme(root):
    root.configure(bg=BG)
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TFrame", background=BG)
    style.configure("Card.TFrame", background=WHITE)
    for index, (surface, accent) in enumerate(CARD_PALETTE):
        style.configure(f"Pet{index}.TFrame", background=surface)
        style.configure(f"Pet{index}.TLabel", background=surface, foreground=INK)
        style.configure(f"Pet{index}Muted.TLabel", background=surface, foreground=MUTED)
        style.configure(f"Pet{index}.TButton", background=accent, foreground=WHITE,
                        font=("Segoe UI", 10, "bold"), padding=(16, 10), borderwidth=0)
        style.map(f"Pet{index}.TButton", foreground=[("active", WHITE)],
                  background=[("active", accent)])
    style.configure("TLabel", background=BG, foreground=INK, font=("Segoe UI", 11))
    style.configure("Card.TLabel", background=WHITE, foreground=INK, font=("Segoe UI", 11))
    style.configure("Muted.TLabel", background=BG, foreground=MUTED, font=("Segoe UI", 10))
    style.configure("CardMuted.TLabel", background=WHITE, foreground=MUTED, font=("Segoe UI", 10))
    style.configure("Title.TLabel", background=BG, foreground=INK, font=("Segoe UI", 24, "bold"))
    style.configure("Section.TLabel", background=BG, foreground=INK, font=("Segoe UI", 17, "bold"))
    style.configure("CardTitle.TLabel", background=WHITE, foreground=INK, font=("Segoe UI", 13, "bold"))
    style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=(16, 10), background=PALE, foreground=GREEN_DARK, borderwidth=0)
    style.map("TButton", background=[("active", "#D4E8FA"), ("disabled", "#EAEFEC")])
    style.configure("Accent.TButton", background=GREEN, foreground=WHITE)
    style.map("Accent.TButton", background=[("active", GREEN_DARK)], foreground=[("active", WHITE)])
    style.configure("TEntry", padding=8, fieldbackground=WHITE, bordercolor=BORDER)
    style.configure("TCombobox", padding=8, fieldbackground=WHITE)
    style.configure("Treeview", font=("Segoe UI", 10), rowheight=34, background=WHITE, fieldbackground=WHITE, foreground=INK, borderwidth=0)
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), padding=9, background=PALE, foreground=INK)
    style.map("Treeview", background=[("selected", GREEN)], foreground=[("selected", WHITE)])


def center_window(window, width=650, height=450):
    window.update_idletasks()
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    width = min(width, max(380, screen_w - 80))
    height = min(height, max(280, screen_h - 110))
    window.geometry(f"{width}x{height}+{max(0, (screen_w-width)//2)}+{max(0, (screen_h-height)//2)}")
    window.minsize(min(width, 420), min(height, 320))
    window.configure(bg=BG)


def form_shell(window, heading, description):
    """Cabeçalho e painel de formulário que se expande e permanece centralizado."""
    outer = ttk.Frame(window, padding=28)
    outer.pack(fill="both", expand=True)
    outer.columnconfigure(0, weight=1)
    outer.rowconfigure(2, weight=1)
    ttk.Label(outer, text=heading, style="Section.TLabel").grid(row=0, column=0, sticky="w")
    ttk.Label(outer, text=description, style="Muted.TLabel", wraplength=530).grid(row=1, column=0, sticky="w", pady=(5, 18))
    card = ttk.Frame(outer, style="Card.TFrame", padding=24)
    card.grid(row=2, column=0, sticky="nsew")
    card.columnconfigure(1, weight=1)
    return card


def form_field(card, row, label, widget):
    ttk.Label(card, text=label, style="Card.TLabel").grid(row=row, column=0, sticky="w", padx=(0, 16), pady=9)
    widget.grid(row=row, column=1, sticky="ew", pady=9)
    return widget
