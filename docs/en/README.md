# User guide — English

## Purpose

The application helps staff manage dog and cat adoptions. The application keeps data in memory while it runs.

## Procedure

1. Open a terminal in the project folder. Run `python main.py`.
2. Select **Cadastrar Cachorro** (Register Dog) or **Cadastrar Gato** (Register Cat). Enter the animal data. Select **Salvar** (Save).
3. Select **Cadastrar Adotante** (Register Adopter). Enter a name, an 11-digit CPF number, and a telephone number. Select **Salvar**.
4. Select **Nova Solicitação** (New Request). Select an animal and an adopter. Select **Enviar solicitação** (Submit Request).
5. Select **Gerenciar Solicitações** (Manage Requests). Select a request. Select **Aprovar** (Approve) or **Rejeitar** (Reject).
6. Select **Listar Animais** (List Animals) to see the animal status.

## Limits

- The application does not save data to a file or a database.
- Do not submit a new request for an adopted animal.
- You cannot change a completed request.
- The application checks CPF length. It does not check CPF verification digits.

Read the [decisions](decisions.md), [architecture](architecture.md), and [interface guide](interface.md).
