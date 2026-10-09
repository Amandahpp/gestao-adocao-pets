# System architecture

The project uses a simplified **Model–View–Controller (MVC)** structure.

- **Model:** Defines animals, adopters, shelters, and adoption requests. Applies business rules.
- **View:** Shows Tkinter windows, input fields, and tables. Sends user actions to the controller.
- **Controller:** Receives user actions. Calls the models. Shows messages.

## Adoption request sequence

1. The user selects an available animal and an adopter.
2. The view sends the selections to the controller.
3. The controller creates a request and registers it with the shelter.
4. The shelter rejects a second pending request for the same animal.
5. The controller sends an approval or rejection action to the request.
6. The state object permits or rejects the transition.
7. After approval, the animal status becomes Adopted.

## Limits

The application has no user authentication, database, or external service integration. It is a local academic demonstration.
