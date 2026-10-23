# Interface gráfica

A interface usa **Tkinter** e os componentes **ttk**, da biblioteca padrão do Python. O arquivo `src/views/theme.py` define as cores, as fontes e o estilo de botões, campos e tabelas.

## Janelas

- A janela principal usa o tamanho inicial de 1000 × 760 pixels. O tamanho mínimo é 480 × 580 pixels.
- A janela principal mostra seis cartões. Cada cartão tem um botão **Abrir →**.
- Cada função abre uma janela secundária (`Toplevel`). O código centraliza essa janela na tela.

| Cartão | Janela aberta | Componentes principais |
|---|---|---|
| Cadastrar cachorro | `CadastroCachorroView` | Campos de texto, lista de seleção, botão |
| Cadastrar gato | `CadastroGatoView` | Campos de texto, lista de seleção, botão |
| Consultar animais | `ListagemAnimaisView` | Tabela, barra de rolagem, botão |
| Cadastrar adotante | `CadastroAdotanteView` | Campos de texto, botão |
| Nova solicitação | `CadastroSolicitacaoView` | Duas listas de seleção, botão |
| Gerenciar solicitações | `GerenciadorSolicitacoesView` | Tabela, barra de rolagem, três botões |

## Componentes usados

| Componente Tkinter | Uso |
|---|---|
| `Tk` | Janela principal. |
| `Toplevel` | Janelas secundárias. |
| `Frame` | Agrupa os outros componentes. |
| `Label` | Títulos, textos e nomes dos campos. |
| `Entry` | Campo de texto. |
| `Combobox` | Lista de seleção, como o sexo e a escolha do animal. |
| `Treeview` | Tabela de animais e de solicitações. |
| `Scrollbar` | Barra de rolagem das tabelas. |
| `Button` | Botões que executam uma ação. |
| `messagebox` | Caixas de aviso e de sucesso. |

## Eventos

- Cada botão usa o parâmetro `command` para chamar um método do controller ou da view.
- O evento `<Configure>` da janela principal reorganiza os cartões quando a janela muda de tamanho.
- A tabela de solicitações usa `selection()` para saber qual linha a pessoa escolheu.

## Organização da tela

- A tela principal usa duas colunas quando a largura da janela é de 750 pixels ou mais. Abaixo disso, usa uma coluna.
- O código usa `grid` e `pack` em contêineres diferentes. O Tkinter não permite os dois no mesmo contêiner.
- Formulários e tabelas se expandem junto com a janela.

## Estilo visual

O tema `clam` do `ttk` é a base. O arquivo `theme.py` define uma paleta com fundo claro e destaques em azul. Os seis cartões da tela principal têm cores diferentes: azul, laranja, verde, rosa, amarelo-alaranjado e lilás.
