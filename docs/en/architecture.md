# Architecture

The project uses a simplified **Model–View–Controller (MVC)** pattern, with a database access layer. The code has four parts.

| Layer | Folder | Function |
|---|---|---|
| Model | `src/models/` | Holds the data and the business rules. |
| View | `src/views/` | Shows the windows and receives the clicks. |
| Controller | `src/controllers/` | Connects the windows to the rules and to the database. |
| DAO | `dao/` | Reads and writes the PostgreSQL tables. There is one DAO for each table. |

The folder `database/` holds the table script (`banco.sql`), the sample data (`insercao.sql`), and the connection module (`conexao.py`).

## Classes in each layer

- **Model:** `Animal`, `Cachorro` (dog), `Gato` (cat), `AnimalFactory`, `Adotante` (adopter), `Abrigo` (shelter), `SolicitacaoAdocao` (adoption request), `EstadoSolicitacao`, `EstadoPendente`, `EstadoAprovada`, and `EstadoRejeitada`.
- **View:** `MainView`, `CadastroCachorroView`, `CadastroGatoView`, `CadastroAdotanteView`, `CadastroSolicitacaoView`, `ListagemAnimaisView`, and `GerenciadorSolicitacoesView`. The file `theme.py` defines the visual style.
- **Controller:** the class `Controller`. It creates the shelter, keeps the list of adopters, opens the windows, calls the models, and calls the DAOs.
- **DAO:** `AbrigoDAO`, `AdotanteDAO`, `AnimalDAO`, and `SolicitacaoAdocaoDAO`. They use the functions `transacao` and `executar` from the module `database/conexao.py`.

## Data in memory and in the database

The data is saved in PostgreSQL. The program also keeps a copy in memory. The windows and the business rules work with this copy.

- At startup, the `Controller` reads the database. It loads the animals, the adopters, and the requests into the lists in memory.
- For each operation, the `Controller` saves to the database. If the save fails, the controller reverses the change in memory and shows an error message.
- The database creates the identifiers of animals and requests.

## Data model

| Table | Main columns | Rules in the database |
|---|---|---|
| `Adotante` | `cpf` (primary key), `nome`, `telefone` | The CPF is unique. |
| `Abrigo` | `id`, `nome` | The name is unique. |
| `Animal` | `id`, `nome`, `idade`, `sexo`, `status`, `tipo`, `raca`, `pelagem`, `abrigo_id` | The age is zero or more. Sex, status, and type accept fixed values only. A dog needs a breed. A cat needs a coat. |
| `SolicitacaoAdocao` | `id`, `animal_id`, `adotante_cpf`, `estado`, `status` | The state is Pendente, Aprovada, or Rejeitada. Each animal can have only one pending request. |

Dogs and cats are in the same table, `Animal`. The column `tipo` shows which class to create when the program reads a row.

## Adoption sequence

1. The user selects an animal and an adopter in `CadastroSolicitacaoView`.
2. The view calls `Controller.cadastrar_solicitacao`.
3. The controller creates a `SolicitacaoAdocao` with the state `EstadoPendente`.
4. The controller asks the shelter to register the request.
5. The shelter checks three rules. The animal is registered. The animal is available. The animal has no other pending request. If a rule fails, the shelter raises an error.
6. The controller asks `SolicitacaoAdocaoDAO` to save the request. If the save fails, the controller removes the request from memory.
7. The controller shows a success message or a warning.
8. In `GerenciadorSolicitacoesView`, the user selects **Aprovar** (Approve) or **Rejeitar** (Reject). The view calls `Controller.alterar_solicitacao`.
9. The request passes the action to its current state object.
10. The state `EstadoPendente` does the change in memory. When it approves, it changes the animal to "Adotado" (Adopted). The other states raise an error.
11. The controller opens a transaction. It saves the request and the animal together. If the save fails, the controller sets the request state and the animal status back to the old values.

## Limits of this version

These points do not stop the application. A later version can improve them.

- The controller shows messages with `messagebox`, a Tkinter component. In strict MVC, the view does this task.
- The views read the lists directly from `controller.abrigo`.
- The rule "animal is available and has no pending request" appears in `Controller` and in `CadastroSolicitacaoView`.
- The list of adopters is in `Controller`. The list of animals is in `Abrigo`.
- The `Controller` knows the module `database/conexao.py`. It opens the transaction that joins two DAOs.
- The program loads the copy in memory one time, at startup. If another person changes the database while the program is open, the screen does not update.
- The status values are plain text, for example "Disponível" and "Pendente".
