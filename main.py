import tkinter as tk
from src.controllers.controller import Controller
from src.views.theme import apply_theme


def main():
    root = tk.Tk()
    root.title("Patinhas Felizes | Gestão de Adoções")
    root.geometry("1000x760")
    root.minsize(480, 580)
    apply_theme(root)
    Controller(root)
    root.mainloop()


if __name__ == "__main__":
    main()
