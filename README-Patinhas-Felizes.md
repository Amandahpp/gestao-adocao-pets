# 🐾 Patinhas Felizes — Sistema de Gestão de Adoção de Animais

Aplicação desktop acadêmica desenvolvida em **Python** com **Tkinter** para apoiar a gestão de animais disponíveis para adoção, o cadastro de pessoas interessadas e o acompanhamento de solicitações de adoção.

O projeto demonstra conceitos de Programação Orientada a Objetos (POO), organização em camadas inspirada no padrão **MVC**, e padrões de projeto como **Factory**, **Singleton** e **State**.

> **Importante:** esta versão mantém os dados apenas em memória. Ao fechar o programa, os cadastros e solicitações são perdidos. O sistema não utiliza banco de dados.

## 📑 Sumário

- [Objetivos](#-objetivos)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias e conceitos](#-tecnologias-e-conceitos)
- [Requisitos](#-requisitos)
- [Como obter e executar](#-como-obter-e-executar)
- [Como utilizar](#-como-utilizar)
- [Regras de negócio](#-regras-de-negócio)
- [Arquitetura do projeto](#-arquitetura-do-projeto)
- [Padrões de projeto](#-padrões-de-projeto)
- [Testes automatizados](#-testes-automatizados)
- [Diagramas e documentação complementar](#-diagramas-e-documentação-complementar)
- [Limitações conhecidas](#-limitações-conhecidas)
- [Possíveis melhorias futuras](#-possíveis-melhorias-futuras)
- [Idioma](#-idioma)

## 🎯 Objetivos

- Organizar o cadastro de cães e gatos disponíveis para adoção.
- Registrar os dados básicos dos adotantes.
- Criar solicitações de adoção relacionando um animal a um adotante.
- Permitir aprovar ou rejeitar solicitações.
- Atualizar a disponibilidade do animal quando uma adoção é aprovada.
- Aplicar conceitos de orientação a objetos, separação de responsabilidades e padrões de projeto.

## ✨ Funcionalidades

### Cadastro de animais

- Cadastro de **cachorros**, com nome, idade, sexo e raça.
- Cadastro de **gatos**, com nome, idade, sexo e pelagem.
- Geração automática de identificador para cada animal durante a execução.
- Consulta dos animais cadastrados, com tipo, idade e situação.

### Cadastro de adotantes

- Registro de nome, CPF e telefone.
- Verificação de que o CPF informado contém 11 dígitos numéricos.
- Impedimento de CPF duplicado durante a execução atual.

### Solicitações de adoção

- Criação de uma solicitação para um animal disponível e um adotante cadastrado.
- Exibição das solicitações e de seus estados.
- Aprovação ou rejeição de uma solicitação pendente.
- Ao aprovar uma solicitação, o animal passa para o estado **Adotado**.
- Ao rejeitar, o animal permanece **Disponível**.

### Interface gráfica

A tela inicial apresenta cartões de acesso às principais operações. O layout reorganiza os cartões em duas colunas em janelas mais largas e em uma coluna em janelas estreitas. Formulários e tabelas são exibidos em janelas secundárias.

## 🧰 Tecnologias e conceitos

- **Python 3.10 ou superior** — linguagem de programação.
- **Tkinter / ttk** — biblioteca padrão do Python utilizada na interface gráfica.
- **unittest** — biblioteca padrão utilizada nos testes automatizados.
- **Programação Orientada a Objetos** — classes, herança, encapsulamento, propriedades e abstração.
- **MVC (Model–View–Controller)** — separação entre dados/regras, interface e coordenação das ações.
- **Factory Method (fábrica simples)** — criação de objetos `Cachorro` ou `Gato` conforme o tipo informado.
- **Singleton** — mantém uma única instância de `Abrigo` durante a execução.
- **State** — representa os estados de uma solicitação e define quais transições são permitidas.
- **UML / PlantUML** — documentação visual por diagramas `.puml`.

Não são necessárias bibliotecas externas para executar a aplicação, desde que a instalação do Python tenha o Tkinter disponível.

## 💻 Requisitos

- Python **3.10+**.
- Tkinter instalado e funcional.
- Windows, macOS ou Linux com ambiente gráfico disponível.
- Terminal ou editor de código, como o Visual Studio Code (opcional).

Para verificar a versão do Python:

```bash
python --version
```

No Windows, também pode ser utilizado:

```powershell
py --version
```

Para verificar se o Tkinter está disponível:

```bash
python -m tkinter
```

Se o comando abrir uma pequena janela de demonstração, o Tkinter está disponível.

## ▶️ Como obter e executar

### 1. Baixe ou clone o projeto

Se o projeto estiver em um repositório Git, execute:

```bash
git clone <URL_DO_REPOSITORIO>
cd gestao-adocao-pets-main
```

Se você recebeu o projeto em um arquivo ZIP, extraia-o e abra a pasta `gestao-adocao-pets-main` no terminal ou editor.

### 2. (Opcional) Crie um ambiente virtual

O projeto não exige pacotes externos, mas um ambiente virtual pode ajudar a manter o ambiente de desenvolvimento organizado.

Windows:

```powershell
py -m venv .venv
.venv\Scripts\activate
```

macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Inicie a aplicação

Execute o comando a partir da pasta raiz do projeto, onde está o arquivo `main.py`.

Windows:

```powershell
py main.py
```

Ou, se o comando `python` estiver configurado:

```bash
python main.py
```

macOS ou Linux:

```bash
python3 main.py
```

A janela **Patinhas Felizes | Gestão de Adoções** deverá ser aberta.

## 🐶 Como utilizar

Uma sequência básica para experimentar o sistema é:

1. **Cadastre um cachorro ou gato.** Preencha nome, idade, sexo e o campo específico da espécie (raça ou pelagem).
2. **Cadastre um adotante.** Informe nome, CPF com 11 dígitos e telefone.
3. **Consulte os animais.** Confira os animais registrados e se estão disponíveis ou adotados.
4. **Crie uma solicitação.** Selecione um animal disponível sem outra solicitação pendente e escolha um adotante já cadastrado.
5. **Gerencie a solicitação.** Na tela de gerenciamento, selecione uma solicitação e escolha **Aprovar** ou **Rejeitar**.
6. **Confira o resultado.** Uma solicitação aprovada passa a ter o estado `Aprovada` e o animal relacionado passa a `Adotado`. Uma solicitação rejeitada passa a `Rejeitada`, e o animal continua disponível.

O menu inicial contém as opções **Cadastrar cachorro**, **Cadastrar gato**, **Consultar animais**, **Cadastrar adotante**, **Nova solicitação** e **Gerenciar solicitações**.

## 📏 Regras de negócio

- O nome do animal não pode ficar vazio.
- A idade deve ser um número inteiro maior ou igual a zero.
- O sexo deve ser `Macho` ou `Fêmea`.
- O campo específico do animal (raça ou pelagem) deve ser preenchido pela interface.
- O nome do adotante não pode ficar vazio.
- O CPF deve conter 11 dígitos. **A validação atual não verifica os dígitos verificadores do CPF**; verifica apenas a quantidade de números.
- Não é permitido cadastrar dois adotantes com o mesmo CPF durante a execução atual.
- Cada animal recebe um identificador, e o abrigo não aceita identificadores duplicados.
- Só é possível solicitar a adoção de um animal cadastrado e disponível.
- Não pode existir mais de uma solicitação **pendente** para o mesmo animal.
- A aprovação só pode ocorrer enquanto a solicitação estiver pendente e o animal estiver disponível.
- Aprovar uma solicitação altera o status do animal para `Adotado`.
- Rejeitar uma solicitação não altera a disponibilidade do animal.
- Uma solicitação aprovada não pode ser rejeitada; uma solicitação rejeitada não pode ser aprovada.
- Os dados permanecem disponíveis apenas enquanto o programa está aberto.

## 🗂️ Arquitetura do projeto

```text
gestao-adocao-pets-main/
├── main.py                         # Ponto de entrada da aplicação
├── README.md                       # Documentação principal
├── criteriosAvaliacao.md            # Critérios de avaliação
├── docs/
│   ├── README.md                   # Índice da documentação
│   ├── criterios-avaliacao.md      # Critérios de avaliação detalhados
│   ├── pt-br/                      # Documentação em português
│   ├── en/                         # Documentation in English
│   └── diagramas/                  # Diagramas UML em PlantUML
├── src/
│   ├── controllers/                # Coordenação entre interface e regras
│   ├── models/                     # Entidades e regras de negócio
│   └── views/                      # Interface gráfica Tkinter
└── tests/
    └── test_models.py              # Testes automatizados dos modelos
```

### Responsabilidade dos principais módulos

| Caminho | Responsabilidade |
|---|---|
| `main.py` | Cria a janela principal, aplica o tema e inicia o controlador. |
| `src/models/animal.py` | Define a classe abstrata `Animal` e valida os dados comuns. |
| `src/models/cachorro.py` | Implementa a entidade `Cachorro`, derivada de `Animal`. |
| `src/models/gato.py` | Implementa a entidade `Gato`, derivada de `Animal`. |
| `src/models/adotante.py` | Representa o adotante e valida nome e formato do CPF. |
| `src/models/abrigo.py` | Mantém a coleção de animais e solicitações e aplica regras do abrigo. |
| `src/models/animal_factory.py` | Cria o tipo correto de animal a partir do tipo solicitado. |
| `src/models/solicitacao_adocao.py` | Representa uma solicitação, seus participantes e seu estado. |
| `src/models/estado_solicitacao.py` | Define a interface dos estados de solicitação. |
| `src/models/estados.py` | Implementa os estados pendente, aprovada e rejeitada. |
| `src/controllers/controller.py` | Coordena as operações acionadas pela interface e trata mensagens de validação. |
| `src/views/main_menu.py` | Apresenta o menu inicial e os atalhos para as funcionalidades. |
| `src/views/cadastroCachorro.py` | Formulário de cadastro de cachorro. |
| `src/views/cadastroGato.py` | Formulário de cadastro de gato. |
| `src/views/cadastroAdotante.py` | Formulário de cadastro de adotante. |
| `src/views/cadastroSolicitacao.py` | Formulário de criação de solicitação de adoção. |
| `src/views/listagemAnimais.py` | Tabela de consulta de animais cadastrados. |
| `src/views/gerenciarSolicitacao.py` | Tabela e ações para aprovar ou rejeitar solicitações. |
| `src/views/theme.py` | Estilos, cores, organização visual e centralização das janelas. |
| `tests/test_models.py` | Testes das regras de negócio e dos padrões implementados. |

## 🧩 Padrões de projeto

### Factory — `AnimalFactory`

Centraliza a criação de animais. Recebe o tipo (`cachorro` ou `gato`) e os dados necessários, retornando uma instância da classe correspondente. Isso evita espalhar a lógica de escolha da classe pelo código que solicita o cadastro.

### Singleton — `Abrigo`

A classe `Abrigo` reutiliza a mesma instância durante a execução do programa, mantendo uma coleção central de animais e solicitações. Esse comportamento é reiniciado quando o processo termina, pois não há persistência em arquivo ou banco de dados.

### State — estados da solicitação

A solicitação delega as operações de aprovação e rejeição ao objeto que representa seu estado atual:

- `EstadoPendente`: permite aprovar ou rejeitar.
- `EstadoAprovada`: impede novas mudanças de estado e impede rejeição.
- `EstadoRejeitada`: impede novas mudanças de estado e impede aprovação.

Esse padrão concentra as regras de transição em classes específicas, em vez de depender de várias condições espalhadas pelo sistema.

### MVC — separação de responsabilidades

- **Model:** entidades e regras de negócio, localizadas principalmente em `src/models/`.
- **View:** janelas, formulários, tabelas e componentes visuais em `src/views/`.
- **Controller:** recebe ações da interface, chama as regras do domínio e apresenta mensagens em `src/controllers/`.

## 🧪 Testes automatizados

Os testes utilizam o módulo `unittest`, que já faz parte da biblioteca padrão do Python. Na raiz do projeto, execute:

```bash
python -m unittest discover -s tests -v
```

No Windows, também pode ser utilizado:

```powershell
py -m unittest discover -s tests -v
```

A suíte verifica, entre outros pontos:

- criação de cachorro e gato pela fábrica;
- reutilização da instância Singleton do abrigo;
- aprovação e rejeição de solicitações;
- mudança de situação do animal após aprovação;
- bloqueio de duas solicitações pendentes para o mesmo animal;
- impedimento de solicitação para animal já adotado;
- validação de idade e formato do CPF;
- impedimento de identificadores duplicados.

O resultado esperado é que os testes sejam concluídos sem falhas. Caso algum teste falhe, confira a mensagem apresentada no terminal para identificar a regra que precisa ser investigada.

## 📐 Diagramas e documentação complementar

A pasta `docs/` reúne material de apoio ao entendimento e à avaliação do projeto:

- `docs/README.md` — índice da documentação.
- `docs/pt-br/README.md` — visão geral em português.
- `docs/pt-br/arquitetura.md` — arquitetura da aplicação.
- `docs/pt-br/decisoes.md` — decisões e justificativas de projeto.
- `docs/pt-br/interface.md` — documentação da interface.
- `docs/en/` — documentação equivalente em inglês.
- `docs/diagramas/casos-de-uso.puml` — diagrama de casos de uso.
- `docs/diagramas/classes.puml` — diagrama de classes.
- `docs/diagramas/componentes-mvc.puml` — diagrama dos componentes MVC.
- `docs/diagramas/sequencia-adocao.puml` — sequência do fluxo de adoção.

Os arquivos `.puml` podem ser visualizados com uma ferramenta compatível com PlantUML. Consulte também `criteriosAvaliacao.md` e `docs/criterios-avaliacao.md` para os critérios de avaliação do trabalho.

## ⚠️ Limitações conhecidas

- **Sem persistência:** os dados são mantidos em memória e desaparecem ao encerrar o programa.
- **CPF:** a validação confere a quantidade de dígitos, mas não verifica os dígitos verificadores.
- **Sem autenticação:** não há perfis de usuário, login ou permissões.
- **Uso local:** a aplicação é uma interface desktop, não um site ou serviço web multiusuário.
- **Interface gráfica:** é necessário executar o programa em um ambiente com suporte a janelas Tkinter.

## 🚀 Possíveis melhorias futuras

- Persistir cadastros e solicitações em SQLite ou outro banco de dados.
- Implementar validação completa dos dígitos verificadores do CPF.
- Adicionar edição e remoção de cadastros com regras de integridade.
- Permitir filtros e pesquisa na listagem de animais.
- Registrar datas de criação e decisão das solicitações.
- Incluir fotos, descrição, porte e outras características dos animais.
- Criar relatórios de adoções e de animais disponíveis.
- Adicionar autenticação e níveis de acesso, caso o sistema passe a ser utilizado por várias pessoas.
- Ampliar a cobertura de testes para interface e fluxos completos.

## 🌐 Idioma

A interface e a documentação principal estão em português. O diretório `docs/en/` contém documentação complementar em inglês.

---

**Projeto acadêmico — Patinhas Felizes: Sistema de Gestão de Adoção de Animais.**
