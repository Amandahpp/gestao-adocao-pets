class Adotante:
    def __init__(self, nome, cpf, telefone):
        if not str(nome).strip(): raise ValueError("Informe o nome do adotante.")
        numeros = ''.join(c for c in str(cpf) if c.isdigit())
        if len(numeros) != 11: raise ValueError("O CPF deve ter 11 dígitos.")
        self._nome = str(nome).strip()
        self._cpf = numeros
        self._telefone = str(telefone).strip()

    @property
    def nome(self): return self._nome
    @property
    def cpf(self): return self._cpf
    @property
    def telefone(self): return self._telefone

    def exibir_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf} | Telefone: {self.telefone}"
