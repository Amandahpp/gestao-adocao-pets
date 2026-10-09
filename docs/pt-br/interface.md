# Interface gráfica — versão visual atualizada

A aplicação utiliza Tkinter e ttk, sem dependências externas. O arquivo `src/views/theme.py` centraliza a paleta de cores, tipografia e estilos de botões, entradas e tabelas.

## Organização responsiva

- A janela principal inicia com 1000 × 760 pixels e pode ser redimensionada.
- O menu utiliza `grid`, com cartões organizados em duas colunas em janelas largas e uma coluna em janelas estreitas.
- As colunas possuem peso de expansão, para que os cartões ocupem a largura disponível.
- Formulários e tabelas usam contêineres com expansão horizontal e vertical.
- Janelas secundárias são centralizadas na tela.

## Componentes e eventos

- `Tk` cria a janela principal; `Toplevel` cria as janelas secundárias.
- `Frame` organiza o conteúdo; `Label` identifica ações e campos.
- `Entry` recebe texto; `Combobox` permite seleção entre opções.
- `Treeview` mostra animais e solicitações; `Scrollbar` permite rolar tabelas.
- `Button` executa operações por meio de `command`.
- O evento `<Configure>` ajusta o número de colunas do menu à largura disponível.

Os gerenciadores `pack` e `grid` são utilizados em contêineres diferentes, conforme as regras do Tkinter. A interface encaminha as ações ao Controller, mantendo a arquitetura MVC.

### Paleta visual
O menu mantém seis cartões responsivos em duas colunas em telas largas, com fundos pastéis azul, laranja, verde, rosa, amarelo-alaranjado e lilás. Cada cartão usa botão na mesma família de cor. Os emojis e os comandos originais foram preservados. O restante das telas usa um tema claro com detalhes em azul.
