from abrigo import Abrigo
from adotante import Adotante
from animal_factory import AnimalFactory
from solicitacao_adocao import SolicitacaoAdocao

abrigo = Abrigo("Patinhas Felizes")
adotantes = []

id_animal = 1

while True:

    print("\n===== SISTEMA DE ADOÇÃO =====")
    print("1 - Cadastrar Cachorro")
    print("2 - Cadastrar Gato")
    print("3 - Listar Animais")
    print("4 - Cadastrar Adotante")
    print("5 - Solicitar Adoção")
    print("6 - Aprovar Solicitação")
    print("7 - Rejeitar Solicitação")
    print("8 - Listar Solicitações")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        raca = input("Raça: ")

        animal = AnimalFactory.criar_animal(
            "cachorro",
            id_animal,
            nome,
            idade,
            sexo,
            raca
        )

        abrigo.cadastrar_animal(animal)
        id_animal += 1

    elif opcao == "2":

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        pelagem = input("Pelagem: ")

        animal = AnimalFactory.criar_animal(
            "gato",
            id_animal,
            nome,
            idade,
            sexo,
            pelagem
        )

        abrigo.cadastrar_animal(animal)
        id_animal += 1

    elif opcao == "3":
        abrigo.listar_animais()

    elif opcao == "4":

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")

        adotantes.append(
            Adotante(nome, cpf, telefone)
        )

    elif opcao == "5":

        abrigo.listar_animais()

        indice_animal = int(
            input("Animal: ")
        )

        for i, adotante in enumerate(adotantes):
            print(i, "-", adotante.nome)

        indice_adotante = int(
            input("Adotante: ")
        )

        solicitacao = SolicitacaoAdocao(
            abrigo.animais[indice_animal],
            adotantes[indice_adotante]
        )

        abrigo.cadastrar_solicitacao(
            solicitacao
        )

    elif opcao == "6":

        abrigo.listar_solicitacoes()

        indice = int(input("Solicitação: "))

        abrigo.solicitacoes[indice].aprovar()

    elif opcao == "7":

        abrigo.listar_solicitacoes()

        indice = int(input("Solicitação: "))

        abrigo.solicitacoes[indice].rejeitar()

    elif opcao == "8":

        abrigo.listar_solicitacoes()

    elif opcao == "0":
        break