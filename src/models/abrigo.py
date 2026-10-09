class Abrigo:
    """Singleton: mantém o mesmo abrigo durante a execução."""
    _instancia = None

    def __new__(cls, nome="Patinhas Felizes"):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, nome="Patinhas Felizes"):
        if not hasattr(self, "_inicializado"):
            self._nome = nome
            self._animais = []
            self._solicitacoes = []
            self._inicializado = True

    def cadastrar_animal(self, animal):
        if any(a.id == animal.id for a in self._animais):
            raise ValueError("Já existe um animal com esse identificador.")
        self._animais.append(animal)

    def cadastrar_solicitacao(self, solicitacao):
        if solicitacao.animal not in self._animais:
            raise ValueError("Animal não cadastrado no abrigo.")
        if solicitacao.animal.status != "Disponível":
            raise ValueError("Animal indisponível para adoção.")
        if any(s.animal is solicitacao.animal and s.status == "Pendente" for s in self._solicitacoes):
            raise ValueError("Já existe uma solicitação pendente para esse animal.")
        self._solicitacoes.append(solicitacao)

    @property
    def nome(self): return self._nome

    @property
    def animais(self): return tuple(self._animais)

    @property
    def solicitacoes(self): return tuple(self._solicitacoes)
