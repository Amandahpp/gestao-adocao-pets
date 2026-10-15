# Decisões de projeto

Cada decisão tem quatro partes: o que foi decidido, o motivo, onde está no código e a consequência.

## D1 — Arquitetura MVC

- **Decisão:** separar o código em `models`, `views` e `controllers`.
- **Motivo:** manter as regras de negócio separadas das janelas. Assim, as regras podem ser testadas sem abrir a interface.
- **Onde:** `src/models/`, `src/views/` e `src/controllers/controller.py`.
- **Consequência:** os testes em `tests/test_models.py` rodam sem Tkinter. Em compensação, o MVC é simplificado. O limite está descrito em [arquitetura.md](arquitetura.md).

## D2 — Factory (fábrica simples)

- **Decisão:** criar cachorros e gatos por meio de `AnimalFactory.criar_animal`.
- **Motivo:** o controller não precisa conhecer as classes `Cachorro` e `Gato`. Ele só informa o tipo.
- **Onde:** `src/models/animal_factory.py`.
- **Consequência:** para incluir um novo tipo de animal, basta criar a classe e acrescentar um caso na fábrica. A fábrica usa um método estático e um texto para escolher a classe. Por isso ela é uma fábrica simples, e não o padrão Factory Method do livro GoF.

## D3 — Singleton

- **Decisão:** manter uma única instância de `Abrigo` durante a execução.
- **Motivo:** o sistema tem um só abrigo. Todas as partes do código precisam ver as mesmas listas de animais e de solicitações.
- **Onde:** `src/models/abrigo.py`, com o método `__new__`.
- **Consequência:** a instância é estado global do processo. Os testes reiniciam `Abrigo._instancia` antes de cada caso. O teste `test_singleton` confirma que uma segunda chamada devolve o mesmo objeto.

## D4 — State

- **Decisão:** representar a situação da solicitação com três estados: `EstadoPendente`, `EstadoAprovada` e `EstadoRejeitada`.
- **Motivo:** cada estado define quais ações são permitidas. Assim, o código evita uma cadeia de `if` espalhada pelo sistema.
- **Onde:** `src/models/estado_solicitacao.py`, `src/models/estados.py` e `src/models/solicitacao_adocao.py`.
- **Consequência:** só o estado Pendente aceita aprovar ou rejeitar. Ao aprovar, o estado também muda o animal para "Adotado". Os estados Aprovada e Rejeitada geram um erro para qualquer ação.

## D5 — Interface com Tkinter e ttk

- **Decisão:** usar Tkinter e os componentes `ttk`.
- **Motivo:** a biblioteca vem com o Python. Ela oferece os componentes básicos pedidos no critério C3: janelas, botões, campos, listas e tabelas.
- **Onde:** `src/views/`. O estilo fica em `theme.py`.
- **Consequência:** o programa não precisa de instalação extra no Windows. No Linux, pode ser necessário instalar o pacote `python3-tk`.

## D6 — Dados em memória

- **Decisão:** não usar banco de dados nesta primeira parte do trabalho.
- **Motivo:** o banco está previsto para a segunda parte.
- **Onde:** as listas ficam em `Abrigo` e em `Controller`.
- **Consequência:** os dados somem quando o programa fecha. A segunda parte do trabalho vai incluir o banco de dados.

## D7 — Validação em camadas

- **Decisão:** validar os dados em mais de um lugar. Cada lugar cuida do que conhece.
- **Onde e o que:**
  - `Animal` e `Adotante`: nome não vazio, idade inteira maior ou igual a zero, sexo válido e CPF com 11 dígitos.
  - `Abrigo`: identificador único, animal cadastrado e disponível, uma solicitação pendente por animal.
  - Estados: transições permitidas.
  - `Controller`: texto da idade com só dígitos, raça ou pelagem preenchida e CPF único.
- **Consequência:** os modelos geram `ValueError`. O controller captura o erro e mostra um aviso. O sistema confere só a quantidade de dígitos do CPF. Ele não valida os dígitos verificadores.
