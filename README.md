# Patinhas Felizes — Sistema de Gestão de Adoção

Aplicativo acadêmico em Python com interface Tkinter. Permite cadastrar cães, gatos e adotantes; consultar animais; criar solicitações; e aprovar ou rejeitar solicitações.

## Executar

Requisitos: Python 3.10+ com Tkinter disponível. Não há dependências externas.

1. Abra esta pasta no VS Code ou em um terminal.
2. Execute `python main.py` (no Windows, também pode usar `py main.py`).
3. Cadastre um animal e um adotante antes de registrar uma solicitação.

## Regras principais

- A idade do animal deve ser um inteiro maior ou igual a zero.
- O CPF deve conter 11 dígitos (o formato é verificado; os dígitos verificadores não são validados).
- Não são aceitos CPFs duplicados durante a execução.
- Só pode haver uma solicitação pendente por animal.
- A aprovação altera o status do animal para **Adotado**.
- Solicitações aprovadas ou rejeitadas não podem mudar de estado.
- Os dados ficam **somente na memória**. São perdidos ao fechar o programa.

## Testes

Execute `python -m unittest discover -s tests -v` na raiz do projeto.

## Estrutura e documentação

- `src/models/`: regras de negócio, classes de domínio, Factory, Singleton e State.
- `src/controllers/`: coordenação das ações da interface (MVC).
- `src/views/`: janelas, formulários, eventos e layouts Tkinter.
- `docs/pt-br/` e `docs/en/`: documentação em português e inglês.
- `docs/diagramas/`: diagramas UML em PlantUML (`.puml`).
- `tests/`: testes automatizados das regras de negócio.

Consulte [o índice da documentação](docs/README.md).

---

# English — Pet Adoption Management

This academic Python application uses Tkinter. It registers pets and adopters and manages adoption requests. Run `python main.py` from the project root. Run `python -m unittest discover -s tests -v` to check the business rules. Data stays in memory and is lost when the program closes. See [English documentation](docs/en/README.md).

## Interface visual

O tema visual está em `src/views/theme.py`. A tela inicial é responsiva: duas colunas em janelas largas e uma coluna em janelas estreitas. Todas as janelas secundárias são centralizadas. Não há dependências externas para o tema.
