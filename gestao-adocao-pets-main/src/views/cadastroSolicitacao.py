import tkinter as tk
from tkinter import ttk
from src.views.theme import center_window, form_shell, form_field


class CadastroSolicitacaoView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Nova solicitação")
        center_window(self, 690, 390)
        self.animais = [a for a in controller.abrigo.animais if a.status == "Disponível" and not any(s.animal is a and s.status == "Pendente" for s in controller.abrigo.solicitacoes)]
        self.adotantes = list(controller.adotantes)
        card = form_shell(self, "Nova solicitação", "Escolha um animal disponível e um adotante cadastrado.")
        self.combo_animal = ttk.Combobox(card, state="readonly", values=[f"#{a.id} - {a.nome} ({type(a).__name__})" for a in self.animais])
        form_field(card, 0, "Animal", self.combo_animal)
        self.combo_adotante = ttk.Combobox(card, state="readonly", values=[f"{a.nome} ({a.cpf})" for a in self.adotantes])
        form_field(card, 1, "Adotante", self.combo_adotante)
        if self.animais:
            self.combo_animal.current(0)
        if self.adotantes:
            self.combo_adotante.current(0)
        ttk.Button(card, text="Enviar solicitação", style="Accent.TButton", command=self._enviar).grid(row=2, column=1, sticky="e", pady=(22, 0))

    def _enviar(self):
        ia, id_ = self.combo_animal.current(), self.combo_adotante.current()
        if ia < 0 or id_ < 0:
            return
        indice_animal = self.controller.abrigo.animais.index(self.animais[ia])
        indice_adotante = self.controller.adotantes.index(self.adotantes[id_])
        if self.controller.cadastrar_solicitacao(indice_animal, indice_adotante):
            self.destroy()
