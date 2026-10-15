# Graphical user interface

The interface uses **Tkinter** and the **ttk** widgets from the Python standard library. The file `src/views/theme.py` defines the colors, the fonts, and the style of buttons, fields, and tables.

## Windows

- The main window starts at 1000 × 760 pixels. The minimum size is 480 × 580 pixels.
- The main window shows six cards. Each card has an **Abrir →** (Open) button.
- Each function opens a secondary window (`Toplevel`). The code centers this window on the screen.

| Card | Window | Main components |
|---|---|---|
| Cadastrar cachorro (Register dog) | `CadastroCachorroView` | Text fields, selection list, button |
| Cadastrar gato (Register cat) | `CadastroGatoView` | Text fields, selection list, button |
| Consultar animais (View animals) | `ListagemAnimaisView` | Table, scroll bar, button |
| Cadastrar adotante (Register adopter) | `CadastroAdotanteView` | Text fields, button |
| Nova solicitação (New request) | `CadastroSolicitacaoView` | Two selection lists, button |
| Gerenciar solicitações (Manage requests) | `GerenciadorSolicitacoesView` | Table, scroll bar, three buttons |

## Components

| Tkinter component | Use |
|---|---|
| `Tk` | Main window. |
| `Toplevel` | Secondary windows. |
| `Frame` | Groups the other components. |
| `Label` | Titles, text, and field names. |
| `Entry` | Text field. |
| `Combobox` | Selection list, for example the sex and the animal choice. |
| `Treeview` | Table of animals and requests. |
| `Scrollbar` | Scroll bar for the tables. |
| `Button` | Buttons that start an action. |
| `messagebox` | Warning and success dialogs. |

## Events

- Each button uses the parameter `command` to call a method of the controller or the view.
- The event `<Configure>` of the main window changes the card layout when the window size changes.
- The request table uses `selection()` to find the row that the user selected.

## Screen layout

- The main screen uses two columns when the window is 750 pixels wide or more. Below this width, it uses one column.
- The code uses `grid` and `pack` in different containers. Tkinter does not permit both in the same container.
- Forms and tables expand with the window.

## Visual style

The `ttk` theme `clam` is the base. The file `theme.py` defines a palette with a light background and blue accents. The six cards on the main screen have different colors: blue, orange, green, pink, yellow-orange, and lilac.
