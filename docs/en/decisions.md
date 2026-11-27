# Design decisions

Each decision has four parts: what the team decided, the reason, where it is in the code, and the result.

## D1 — MVC architecture

- **Decision:** Split the code into `models`, `views`, and `controllers`.
- **Reason:** Keep the business rules separate from the windows. The team can then test the rules without the interface.
- **Where:** `src/models/`, `src/views/`, and `src/controllers/controller.py`.
- **Result:** The tests in `tests/test_models.py` run without Tkinter. The MVC is simplified. [architecture.md](architecture.md) describes the limits.

## D2 — Factory (simple factory)

- **Decision:** Create dogs and cats with `AnimalFactory.criar_animal`.
- **Reason:** The controller does not need to know the classes `Cachorro` and `Gato`. It sends only the type.
- **Where:** `src/models/animal_factory.py`.
- **Result:** To add a new animal type, create the class and add one case to the factory. The factory uses a static method and a text value to choose the class. It is a simple factory. It is not the Factory Method pattern of the GoF book. `AnimalDAO` also uses the factory. When it reads a row from the database, it sends the column `tipo` to the factory to create the correct object.

## D3 — Singleton

- **Decision:** Keep one `Abrigo` (shelter) object while the program runs.
- **Reason:** The system has one shelter. All parts of the code must see the same lists of animals and requests.
- **Where:** `src/models/abrigo.py`, with the method `__new__`.
- **Result:** The object is global state in the process. The tests reset `Abrigo._instancia` before each case. The test `test_singleton` confirms that a second call returns the same object.

## D4 — State

- **Decision:** Show the status of a request with three states: `EstadoPendente`, `EstadoAprovada`, and `EstadoRejeitada`.
- **Reason:** Each state defines the permitted actions. The code does not need a chain of `if` statements in many places.
- **Where:** `src/models/estado_solicitacao.py`, `src/models/estados.py`, and `src/models/solicitacao_adocao.py`.
- **Result:** Only the Pending state accepts approve or reject. When it approves, the state also changes the animal to "Adotado" (Adopted). The Approved and Rejected states raise an error for each action. The database saves only the name of the state. The function `estado_por_nome`, in `estados.py`, converts this name into the state object when the program reads it.

## D5 — Tkinter and ttk interface

- **Decision:** Use Tkinter and the `ttk` widgets.
- **Reason:** The library is part of Python. It has the basic components that criterion C3 requires: windows, buttons, fields, lists, and tables.
- **Where:** `src/views/`. The style is in `theme.py`.
- **Result:** The program needs no extra installation on Windows. On Linux, you can need the package `python3-tk`.

## D6 — PostgreSQL database

- **Decision:** Save the data in a PostgreSQL database, with the driver `psycopg2`.
- **Reason:** PostgreSQL has the features that the system uses: `CHECK` constraints, foreign keys, and a partial unique index. The index guarantees one pending request for each animal.
- **Where:** `database/banco.sql` (tables), `database/conexao.py` (connection and transactions), and the folder `dao/`.
- **Result:** The data stays available after the program closes. The program does not start without the database. The connection uses the variables `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, and `DB_PASSWORD`.

## D7 — Layered input checks

- **Decision:** Check the data in more than one place. Each place checks what it knows.
- **Where and what:**
  - `Animal` and `Adotante`: name not empty, age a whole number of zero or more, valid sex, and CPF with 11 digits.
  - `Abrigo`: unique identifier, animal registered and available, one pending request for each animal.
  - States: permitted transitions.
  - `Controller`: age text with digits only, breed or coat filled in, and unique CPF.
  - Database: `CHECK` and `UNIQUE` constraints and foreign keys, in `banco.sql`.
- **Result:** The models raise `ValueError`. The controller catches the error and shows a warning. The database is the last barrier. It refuses invalid data even if another program writes to it. The CPF check counts digits only. It does not check the verification digits.

## D8 — DAO (Data Access Object)

- **Decision:** Create one DAO for each table: `AbrigoDAO`, `AdotanteDAO`, `AnimalDAO`, and `SolicitacaoAdocaoDAO`.
- **Reason:** Keep the SQL in one place, outside the models and the controller. A change in the database does not force a change in the business rules. The tests of the models also run without a database.
- **Where:** The folder `dao/`.
- **Result:** The model classes have no SQL. The DAOs return domain objects, for example `Cachorro` and `Adotante`. `AbrigoDAO` returns identifiers only, because `Abrigo` is a Singleton that keeps the lists in memory. `SolicitacaoAdocaoDAO` receives the animals and adopters that are already loaded. The request then points to the same `Animal` object that is in `Abrigo`.

## D9 — Transaction for approve and reject

- **Decision:** Save the request and the animal in the same transaction.
- **Reason:** Avoid conflicting data, for example an "Aprovada" (Approved) request with an animal that is still "Disponível" (Available).
- **Where:** `database/conexao.py` (function `transacao`) and `Controller.alterar_solicitacao`.
- **Result:** If one of the saves fails, the database cancels both. The controller also sets the memory back to the old value. The tests `test_aprovar_grava_solicitacao_e_animal_na_mesma_transacao` and `test_erro_dentro_da_transacao_desfaz_tudo` cover this case. The `Controller` knows the module `database/conexao.py` to open the transaction.

## D10 — Copy in memory

- **Decision:** Keep the lists of animals, requests, and adopters in memory. The controller loads them at startup and updates them after each successful operation.
- **Reason:** The windows and the business rules already worked with objects in memory in the first part. The system also compares animals by identity, that is, by the same object. A request must therefore point to the same `Animal` that is in `Abrigo`. Keeping the copy avoided a rewrite of these parts.
- **Where:** `Controller._carregar_do_banco`, `Abrigo.restaurar_solicitacao`, and `Abrigo.remover_solicitacao`.
- **Result:** The windows do not read the database at each click. If another person changes the database while the program is open, the screen does not update. The method `restaurar_solicitacao` puts requests that come from the database back in memory without the registration checks, because they can be Approved or Rejected.

## D11 — Identifiers created by the database

- **Decision:** Let the database create the `id` of animals and requests. The object starts with an empty `id`. After the save, the DAO puts the `id` in the object.
- **Reason:** Avoid that the program and the database create different identifiers.
- **Where:** Columns `GENERATED ALWAYS AS IDENTITY` in `banco.sql` and the methods `inserir` of the DAOs.
- **Result:** The program does not need to count identifiers. The object has an `id` only after the save. The adopter uses the CPF, digits only, as the primary key.
