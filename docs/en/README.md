# User guide

## Purpose

The application helps staff manage dog and cat adoptions. In this first part of the project, the application keeps data in memory only. The application deletes the data when you close it.

The screen labels are in Portuguese. This guide gives the English meaning in parentheses.

## Start the application

1. Open a terminal in the folder that contains the file `main.py`.
2. Run the command `python main.py`.

The window **Patinhas Felizes | Gestão de Adoções** shows six cards. To open a function, select **Abrir →** (Open) on the card.

## Register an animal

1. Select **Abrir →** on the card **Cadastrar cachorro** (Register dog) or **Cadastrar gato** (Register cat).
2. Enter **Nome** (Name) and **Idade (anos)** (Age in years).
3. Select **Sexo** (Sex): Macho (Male) or Fêmea (Female).
4. Enter **Raça** (Breed) for a dog. Enter **Pelagem** (Coat) for a cat.
5. Select **Salvar cadastro** (Save record).

The application shows a success message. The window closes. The animal gets the status "Disponível" (Available).

## Register an adopter

1. Select **Abrir →** on the card **Cadastrar adotante** (Register adopter).
2. Enter **Nome** (Name), **CPF**, and **Telefone** (Telephone).
3. Select **Salvar cadastro** (Save record).

The CPF must have 11 digits. The application ignores dots and hyphens. You can register each CPF one time.

## Create an adoption request

1. Select **Abrir →** on the card **Nova solicitação** (New request).
2. Select an animal in the list **Animal**.
3. Select an adopter in the list **Adotante** (Adopter).
4. Select **Enviar solicitação** (Submit request).

The animal list shows only animals that are available and have no pending request. The new request has the status "Pendente" (Pending).

## Approve or reject a request

1. Select **Abrir →** on the card **Gerenciar solicitações** (Manage requests).
2. Select a row in the table.
3. Select **Aprovar** (Approve) or **Rejeitar** (Reject).

Result:

- **Approve:** The request status changes to "Aprovada" (Approved). The animal status changes to "Adotado" (Adopted).
- **Reject:** The request status changes to "Rejeitada" (Rejected). The animal stays "Disponível" (Available). The animal shows again in the list of **Nova solicitação**.

You cannot change an approved request or a rejected request.

## See the animals

1. Select **Abrir →** on the card **Consultar animais** (View animals).
2. Read the table with **Nome** (Name), **Tipo** (Type), **Idade** (Age), and **Status**.
3. Select **Fechar** (Close) to leave.

## Application messages

| Message | Action |
|---|---|
| Cadastre um adotante antes. (Register an adopter first.) | Register an adopter. Then create the request. |
| Não há animais disponíveis sem solicitação pendente. (No available animal without a pending request.) | Register a new animal or complete the pending request. |
| O CPF deve ter 11 dígitos. (The CPF must have 11 digits.) | Correct the CPF. |
| Já existe um adotante com esse CPF. (An adopter with this CPF already exists.) | Use a different CPF. |
| A idade deve ser um número inteiro não negativo. (The age must be a whole number, zero or more.) | Enter a whole number, for example 0, 1, or 5. |
| Selecione uma solicitação. (Select a request.) | Select a row in the table before you approve or reject. |

## See also

- [Architecture](architecture.md)
- [Design decisions](decisions.md)
- [User interface](interface.md)
