from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, id_animal, nome, idade, sexo):
        self.__id = id_animal
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__status = "Disponivel"

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def sexo(self):
        return self.__sexo
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status):
        self.__status = novo_status

    @abstractmethod
    def exibir_dados(self):
        pass