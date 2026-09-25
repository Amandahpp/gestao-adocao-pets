import sys
import os

# Garante que a raiz do projeto esteja no sys.path, independente
# de onde o VSCode define o diretório de trabalho ao dar "Run".
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from src.controllers.controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Adoção Patinhas Felizes")
    root.geometry("400x350")

    app = Controller(root)

    root.mainloop()
