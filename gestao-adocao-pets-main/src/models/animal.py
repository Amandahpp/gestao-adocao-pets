from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, id_animal, nome, idade, sexo):
        if not str(nome).strip(): raise ValueError("Informe o nome do animal.")
        if type(idade) is not int or idade < 0: raise ValueError("A idade deve ser um inteiro não negativo.")
        if sexo not in ("Macho", "Fêmea"): raise ValueError("Selecione um sexo válido.")
        self._id = id_animal
        self._nome = str(nome).strip()
        self._idade = idade
        self._sexo = sexo
        self._status = "Disponível"

    @property
    def id(self): return self._id
    @property
    def nome(self): return self._nome
    @property
    def idade(self): return self._idade
    @property
    def sexo(self): return self._sexo
    @property
    def status(self): return self._status
    @status.setter
    def status(self, novo_status):
        if novo_status not in ("Disponível", "Adotado"):
            raise ValueError("Status inválido.")
        self._status = novo_status

    @abstractmethod
    def exibir_dados(self): pass
