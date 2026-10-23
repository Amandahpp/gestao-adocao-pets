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
- **Result:** To add a new animal type, create the class and add one case to the factory. The factory uses a static method and a text value to choose the class. It is a simple factory. It is not the Factory Method pattern of the GoF book.

## D3 — Singleton

- **Decision:** Keep one `Abrigo` (shelter) object while the program runs.
- **Reason:** The system has one shelter. All parts of the code must see the same lists of animals and requests.
- **Where:** `src/models/abrigo.py`, with the method `__new__`.
- **Result:** The object is global state in the process. The tests reset `Abrigo._instancia` before each case. The test `test_singleton` confirms that a second call returns the same object.

## D4 — State

- **Decision:** Show the status of a request with three states: `EstadoPendente`, `EstadoAprovada`, and `EstadoRejeitada`.
- **Reason:** Each state defines the permitted actions. The code does not need a chain of `if` statements in many places.
- **Where:** `src/models/estado_solicitacao.py`, `src/models/estados.py`, and `src/models/solicitacao_adocao.py`.
- **Result:** Only the Pending state accepts approve or reject. When it approves, the state also changes the animal to "Adotado" (Adopted). The Approved and Rejected states raise an error for each action.

## D5 — Tkinter and ttk interface

- **Decision:** Use Tkinter and the `ttk` widgets.
- **Reason:** The library is part of Python. It has the basic components that criterion C3 requires: windows, buttons, fields, lists, and tables.
- **Where:** `src/views/`. The style is in `theme.py`.
- **Result:** The program needs no extra installation on Windows. On Linux, you can need the package `python3-tk`.

## D6 — Data in memory

- **Decision:** Do not use a database in this first part of the project.
- **Reason:** The database is planned for the second part.
- **Where:** The lists are in `Abrigo` and in `Controller`.
- **Result:** The program loses the data when it closes. The second part of the project will add a database.

## D7 — Layered input checks

- **Decision:** Check the data in more than one place. Each place checks what it knows.
- **Where and what:**
  - `Animal` and `Adotante`: name not empty, age a whole number of zero or more, valid sex, and CPF with 11 digits.
  - `Abrigo`: unique identifier, animal registered and available, one pending request for each animal.
  - States: permitted transitions.
  - `Controller`: age text with digits only, breed or coat filled in, and unique CPF.
- **Result:** The models raise `ValueError`. The controller catches the error and shows a warning. The CPF check counts digits only. It does not check the verification digits.
