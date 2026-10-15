# Patinhas Felizes

Sistema de gestão de adoção de animais. Trabalho da disciplina de Linguagem de Programação Orientada a Objetos (LPOO).

**Integrantes:** Amanda Andreis Hoppe, Ana Paula de Oliveira Andreis, Maria Eduarda de Chaves
                

## O que o sistema faz

O sistema cadastra cachorros, gatos e adotantes. O operador cria uma solicitação de adoção para um animal. O operador aprova ou rejeita a solicitação. Quando ele aprova, o animal passa a ter o status "Adotado".

Nesta primeira parte do trabalho, o sistema guarda os dados somente na memória. Ao fechar o programa, os dados são apagados. A segunda parte do trabalho vai incluir um banco de dados.

## Como executar

Requisito: Python 3.10 ou superior. O Tkinter faz parte da instalação padrão do Python no Windows. No Linux, pode ser necessário instalar o pacote `python3-tk`.

1. Baixe ou clone este repositório.
2. Abra um terminal na pasta que contém o arquivo `main.py`.
3. Execute o comando:

```
python main.py
```

Para executar os testes automáticos:

```
python -m unittest tests.test_models
```

## Como usar

1. Cadastre um cachorro ou um gato.
2. Cadastre um adotante. O CPF deve ter 11 dígitos. O sistema conta só os dígitos e ignora pontos e traços.
3. Abra **Nova solicitação**. Escolha um animal e um adotante.
4. Abra **Gerenciar solicitações**. Selecione uma solicitação. Clique em **Aprovar** ou **Rejeitar**.
5. Abra **Consultar animais** para ver o status de cada animal.

## Regras do sistema

- O nome do animal e o nome do adotante não podem ficar vazios.
- A idade do animal é um número inteiro maior ou igual a zero.
- O sexo do animal é "Macho" ou "Fêmea".
- Raça (cachorro) e pelagem (gato) não podem ficar vazias.
- Não pode haver dois adotantes com o mesmo CPF.
- Só é possível solicitar um animal cadastrado e disponível.
- Cada animal pode ter apenas uma solicitação pendente.
- Uma solicitação aprovada ou rejeitada não pode mais mudar.
- Rejeitar uma solicitação não altera o status do animal.

## Conceitos de POO neste projeto

| Conceito | Onde está |
|---|---|
| Abstração | `Animal` é uma classe abstrata com o método abstrato `exibir_dados()`. |
| Herança | `Cachorro` e `Gato` herdam de `Animal`. |
| Polimorfismo | Os três estados da solicitação respondem de forma diferente à mesma chamada `aprovar()`. `Cachorro` e `Gato` implementam `exibir_dados()` cada um à sua maneira. |
| Encapsulamento | Os atributos são privados. O acesso é feito por propriedades (`@property`). Os construtores validam os dados. |
| Associação | `Abrigo` guarda animais e solicitações. `SolicitacaoAdocao` liga um animal a um adotante. |

## Padrões de projeto

| Padrão | Classe | Função |
|---|---|---|
| Singleton | `Abrigo` | Existe um único abrigo durante a execução. |
| Factory (fábrica simples) | `AnimalFactory` | Cria `Cachorro` ou `Gato` conforme o tipo pedido. |
| State | `EstadoSolicitacao` e suas subclasses | Define o que cada estado da solicitação permite. |

A arquitetura é MVC simplificada: `models/` guarda as regras, `views/` guarda as janelas e `controllers/` liga as duas partes. Os motivos de cada escolha estão em [docs/pt-br/decisoes.md](docs/pt-br/decisoes.md).

## Estrutura de pastas

```
.
├── main.py                  Ponto de entrada
├── criteriosAvaliacao.md    Critérios do professor
├── docs/                    Documentação e diagramas UML
├── src/
│   ├── models/              Entidades e regras de negócio
│   ├── views/               Janelas Tkinter
│   └── controllers/         Controller principal
└── tests/
    └── test_models.py       Testes automáticos dos modelos
```

## Documentação

Veja a pasta [docs](docs/README.md). Ela contém os textos em português e em inglês e os diagramas UML.

## Limitações desta etapa

- Os dados não são salvos. Eles somem quando o programa fecha. O banco de dados está previsto para a segunda parte.
- O sistema confere só a quantidade de dígitos do CPF. Ele não valida os dígitos verificadores.
- O sistema não valida o telefone.
