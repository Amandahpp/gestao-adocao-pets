# Architecture

The project uses a simplified **Model–View–Controller (MVC)** pattern. The code has three folders.

| Layer | Folder | Function |
|---|---|---|
| Model | `src/models/` | Holds the data and the business rules. |
| View | `src/views/` | Shows the windows and receives the clicks. |
| Controller | `src/controllers/` | Connects the windows to the rules. |

## Classes in each layer

- **Model:** `Animal`, `Cachorro` (dog), `Gato` (cat), `AnimalFactory`, `Adotante` (adopter), `Abrigo` (shelter), `SolicitacaoAdocao` (adoption request), `EstadoSolicitacao`, `EstadoPendente`, `EstadoAprovada`, and `EstadoRejeitada`.
- **View:** `MainView`, `CadastroCachorroView`, `CadastroGatoView`, `CadastroAdotanteView`, `CadastroSolicitacaoView`, `ListagemAnimaisView`, and `GerenciadorSolicitacoesView`. The file `theme.py` defines the visual style.
- **Controller:** the class `Controller`. It creates the shelter, keeps the list of adopters, opens the windows, and calls the models.

## Adoption sequence

1. The user selects an animal and an adopter in `CadastroSolicitacaoView`.
2. The view calls `Controller.cadastrar_solicitacao`.
3. The controller creates a `SolicitacaoAdocao` with the state `EstadoPendente`.
4. The controller asks the shelter to register the request.
5. The shelter checks three rules. The animal is registered. The animal is available. The animal has no other pending request. If a rule fails, the shelter raises an error.
6. The controller shows a success message or a warning.
7. In `GerenciadorSolicitacoesView`, the user selects **Aprovar** (Approve) or **Rejeitar** (Reject). The view calls `Controller.alterar_solicitacao`.
8. The request passes the action to its current state object.
9. The state `EstadoPendente` does the change. When it approves, it changes the animal to "Adotado" (Adopted). The other states raise an error.

## Limits of this version

These points do not stop the application. A later version can improve them.

- The controller shows messages with `messagebox`, a Tkinter component. In strict MVC, the view does this task.
- The views read the lists directly from `controller.abrigo`.
- The rule "animal is available and has no pending request" appears in `Controller` and in `CadastroSolicitacaoView`.
- The list of adopters is in `Controller`. The list of animals is in `Abrigo`.
- The status values are plain text, for example "Disponível" and "Pendente".
- The application has no persistent storage. It keeps the data in memory.
