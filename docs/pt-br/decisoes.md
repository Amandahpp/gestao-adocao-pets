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
- **Consequência:** para incluir um novo tipo de animal, basta criar a classe e acrescentar um caso na fábrica. A fábrica usa um método estático e um texto para escolher a classe. Por isso ela é uma fábrica simples, e não o padrão Factory Method do livro GoF. O `AnimalDAO` também usa a fábrica. Ao ler uma linha do banco, ele passa a coluna `tipo` para a fábrica criar o objeto certo.

## D3 — Singleton

- **Decisão:** manter uma única instância de `Abrigo` durante a execução.
- **Motivo:** o sistema tem um só abrigo. Todas as partes do código precisam ver as mesmas listas de animais e de solicitações.
- **Onde:** `src/models/abrigo.py`, com o método `__new__`.
- **Consequência:** a instância é estado global do processo. Os testes reiniciam `Abrigo._instancia` antes de cada caso. O teste `test_singleton` confirma que uma segunda chamada devolve o mesmo objeto. 

## D4 — State

- **Decisão:** representar a situação da solicitação com três estados: `EstadoPendente`, `EstadoAprovada` e `EstadoRejeitada`.
- **Motivo:** cada estado define quais ações são permitidas. Assim, o código evita uma cadeia de `if` espalhada pelo sistema.
- **Onde:** `src/models/estado_solicitacao.py`, `src/models/estados.py` e `src/models/solicitacao_adocao.py`.
- **Consequência:** só o estado Pendente aceita aprovar ou rejeitar. Ao aprovar, o estado também muda o animal para "Adotado". Os estados Aprovada e Rejeitada geram um erro para qualquer ação. O banco guarda só o nome do estado. A função `estado_por_nome`, em `estados.py`, converte esse nome no objeto de estado ao ler.

## D5 — Interface com Tkinter e ttk

- **Decisão:** usar Tkinter e os componentes `ttk`.
- **Motivo:** a biblioteca vem com o Python. Ela oferece os componentes básicos pedidos no critério C3: janelas, botões, campos, listas e tabelas.
- **Onde:** `src/views/`. O estilo fica em `theme.py`.
- **Consequência:** o programa não precisa de instalação extra no Windows. No Linux, pode ser necessário instalar o pacote `python3-tk`.

## D6 — Banco de dados PostgreSQL

- **Decisão:** gravar os dados em um banco PostgreSQL, com o driver `psycopg2`.
- **Motivo:** o PostgreSQL tem os recursos que o sistema usa: restrições `CHECK`, chaves estrangeiras e um índice único parcial. Esse índice garante uma solicitação pendente por animal.
- **Onde:** `database/banco.sql` (tabelas), `database/conexao.py` (conexão e transações) e a pasta `dao/`.
- **Consequência:** os dados continuam disponíveis depois que o programa fecha. O programa não abre sem o banco. A conexão usa as variáveis `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` e `DB_PASSWORD`.

## D7 — Validação em camadas

- **Decisão:** validar os dados em mais de um lugar. Cada lugar cuida do que conhece.
- **Onde e o que:**
  - `Animal` e `Adotante`: nome não vazio, idade inteira maior ou igual a zero, sexo válido e CPF com 11 dígitos.
  - `Abrigo`: identificador único, animal cadastrado e disponível, uma solicitação pendente por animal.
  - Estados: transições permitidas.
  - `Controller`: texto da idade com só dígitos, raça ou pelagem preenchida e CPF único.
  - Banco de dados: restrições `CHECK`, `UNIQUE` e chaves estrangeiras, em `banco.sql`.
- **Consequência:** os modelos geram `ValueError`. O controller captura o erro e mostra um aviso. O banco é a última barreira. Ele recusa dados inválidos mesmo que outro programa grave nele. O sistema confere só a quantidade de dígitos do CPF. Ele não valida os dígitos verificadores.

## D8 — DAO (Data Access Object)

- **Decisão:** criar um DAO para cada tabela: `AbrigoDAO`, `AdotanteDAO`, `AnimalDAO` e `SolicitacaoAdocaoDAO`.
- **Motivo:** manter o SQL em um só lugar, fora dos modelos e do controller. Assim, uma mudança no banco não obriga a mudar as regras de negócio. Os testes dos modelos também rodam sem banco.
- **Onde:** pasta `dao/`.
- **Consequência:** as classes de modelo não têm SQL. Os DAOs devolvem objetos do domínio, como `Cachorro` e `Adotante`. O `AbrigoDAO` devolve só identificadores, porque o `Abrigo` é um Singleton que guarda as listas em memória. O `SolicitacaoAdocaoDAO` recebe os animais e os adotantes já carregados. Assim, a solicitação aponta para o mesmo objeto `Animal` que está no `Abrigo`.

## D9 — Transação ao aprovar ou rejeitar

- **Decisão:** gravar a solicitação e o animal na mesma transação.
- **Motivo:** evitar dados em conflito, como uma solicitação "Aprovada" com o animal ainda "Disponível".
- **Onde:** `database/conexao.py` (função `transacao`) e `Controller.alterar_solicitacao`.
- **Consequência:** se uma das gravações falha, o banco desfaz as duas. O controller também volta a memória ao valor anterior. Os testes `test_aprovar_grava_solicitacao_e_animal_na_mesma_transacao` e `test_erro_dentro_da_transacao_desfaz_tudo` cobrem esse caso. O `Controller` conhece o módulo `database/conexao.py` para abrir a transação.

## D10 — Cópia em memória

- **Decisão:** manter as listas de animais, solicitações e adotantes em memória. O controller as carrega na abertura e as atualiza a cada operação bem-sucedida.
- **Motivo:** as janelas e as regras de negócio já trabalhavam com objetos em memória na primeira parte. O sistema também compara animais por identidade, ou seja, pelo mesmo objeto. Por isso a solicitação precisa apontar para o mesmo `Animal` que está no `Abrigo`. Manter a cópia evitou reescrever essas partes.
- **Onde:** `Controller._carregar_do_banco`, `Abrigo.restaurar_solicitacao` e `Abrigo.remover_solicitacao`.
- **Consequência:** as janelas não leem o banco a cada clique. Se outra pessoa alterar o banco com o programa aberto, a tela não atualiza. O método `restaurar_solicitacao` recoloca solicitações lidas do banco sem conferir as regras de cadastro, porque elas podem estar Aprovadas ou Rejeitadas.

## D11 — Identificadores criados pelo banco

- **Decisão:** deixar o banco criar o `id` de animais e solicitações. O objeto nasce com `id` vazio. Depois da gravação, o DAO coloca o `id` no objeto.
- **Motivo:** evitar que o programa e o banco criem identificadores diferentes.
- **Onde:** colunas `GENERATED ALWAYS AS IDENTITY` em `banco.sql` e os métodos `inserir` dos DAOs.
- **Consequência:** o programa não precisa contar os identificadores. O objeto só tem `id` depois de gravado. O adotante usa o CPF, só com dígitos, como chave primária.
