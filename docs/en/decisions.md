# Design decisions

## D1 — MVC architecture

**Decision:** Keep models, controller, and views in separate folders. **Reason:** Reduce dependencies between business rules and windows. **Implementation:** `src/models/`, `src/controllers/controller.py`, and `src/views/`.

## D2 — Factory

**Decision:** Use `AnimalFactory.criar_animal` to create dogs and cats. **Reason:** Keep object creation in one component. **Implementation:** `src/models/animal_factory.py`.

## D3 — Singleton

**Decision:** Use one `Abrigo` object in one Python process. **Reason:** Share animal and request lists. **Implementation:** `src/models/abrigo.py`. **Limit:** The object keeps shared state. Tests must reset this state.

## D4 — State

**Decision:** Use three request states: Pending, Approved, and Rejected. **Reason:** Control permitted transitions. **Implementation:** `src/models/estado_solicitacao.py`, `estados.py`, and `solicitacao_adocao.py`. Approval also sets the animal status to Adopted.

## D5 — Tkinter interface

**Decision:** Use Tkinter and `ttk` widgets. **Reason:** Show the basic user interface components, events, and layouts.

## D6 — In-memory data

**Decision:** Do not add database storage in this version. **Result:** The application loses data when it closes.

## D7 — Input checks

**Decision:** Check inputs in the model and show errors through the controller. CPF checks use the number of digits only. Animal age must be a nonnegative integer.
