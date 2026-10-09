# Graphical user interface — updated design

The application uses Tkinter and ttk. It does not require external UI packages. The file `src/views/theme.py` defines colors, fonts, buttons, entry fields, and table styles.

## Responsive layout

- The main window starts at 1000 × 760 pixels. The user can resize it.
- The main menu shows two card columns in a wide window. It shows one column in a narrow window.
- Grid weights let the cards use the available width.
- Forms and tables expand with their containers.
- Secondary windows open near the center of the screen.

## Components and events

- `Tk` creates the main window. `Toplevel` creates secondary windows.
- `Frame` groups controls. `Label` identifies fields.
- `Entry` accepts text. `Combobox` selects an item.
- `Treeview` displays records. `Scrollbar` scrolls tables.
- `Button` uses `command` to call an action.
- The `<Configure>` event changes the menu layout when the window width changes.

The program uses `pack` and `grid` in separate containers. The views call the Controller to perform operations. This keeps the MVC structure.

### Visual palette
The main menu keeps six responsive cards in two columns on wide screens. The cards use pastel blue, orange, green, pink, yellow-orange, and lilac backgrounds. Each card has a matching action button. Original emoji icons and actions remain unchanged. Other screens use a light theme with blue accents.
