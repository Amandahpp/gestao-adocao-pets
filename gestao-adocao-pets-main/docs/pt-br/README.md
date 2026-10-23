# Guia do usuário

## Objetivo

O sistema ajuda a organizar a adoção de cachorros e gatos. Nesta primeira parte do trabalho, o sistema guarda os dados somente na memória. Ao fechar o programa, os dados são apagados.

## Iniciar o programa

1. Abra um terminal na pasta que contém o arquivo `main.py`.
2. Execute o comando `python main.py`.

A janela **Patinhas Felizes | Gestão de Adoções** mostra seis cartões. Para abrir uma função, clique em **Abrir →** no cartão.

## Cadastrar um animal

1. Clique em **Abrir →** no cartão **Cadastrar cachorro** ou **Cadastrar gato**.
2. Preencha **Nome** e **Idade (anos)**.
3. Escolha o **Sexo**: Macho ou Fêmea.
4. Preencha **Raça** (cachorro) ou **Pelagem** (gato).
5. Clique em **Salvar cadastro**.

O sistema mostra uma mensagem de sucesso. A janela fecha. O animal recebe o status "Disponível".

## Cadastrar um adotante

1. Clique em **Abrir →** no cartão **Cadastrar adotante**.
2. Preencha **Nome**, **CPF** e **Telefone**.
3. Clique em **Salvar cadastro**.

O CPF deve ter 11 dígitos. O sistema ignora pontos e traços. Cada CPF pode ser cadastrado uma vez.

## Criar uma solicitação de adoção

1. Clique em **Abrir →** no cartão **Nova solicitação**.
2. Escolha o animal na lista **Animal**.
3. Escolha o adotante na lista **Adotante**.
4. Clique em **Enviar solicitação**.

A lista de animais mostra somente animais disponíveis e sem solicitação pendente. A solicitação nova tem o status "Pendente".

## Aprovar ou rejeitar uma solicitação

1. Clique em **Abrir →** no cartão **Gerenciar solicitações**.
2. Selecione uma linha da tabela.
3. Clique em **Aprovar** ou **Rejeitar**.

Resultado:

- **Aprovar:** a solicitação passa a "Aprovada". O animal passa a "Adotado".
- **Rejeitar:** a solicitação passa a "Rejeitada". O animal continua "Disponível" e volta para a lista de **Nova solicitação**.

Uma solicitação aprovada ou rejeitada não pode mais mudar.

## Consultar os animais

1. Clique em **Abrir →** no cartão **Consultar animais**.
2. Leia a tabela com **Nome**, **Tipo**, **Idade** e **Status**.
3. Clique em **Fechar** para sair.

## Avisos do sistema

| Aviso | O que fazer |
|---|---|
| Cadastre um adotante antes. | Cadastre um adotante. Depois crie a solicitação. |
| Não há animais disponíveis sem solicitação pendente. | Cadastre um animal novo ou conclua a solicitação pendente. |
| O CPF deve ter 11 dígitos. | Corrija o CPF. |
| Já existe um adotante com esse CPF. | Use outro CPF. |
| A idade deve ser um número inteiro não negativo. | Digite um número inteiro, como 0, 1 ou 5. |
| Selecione uma solicitação. | Clique em uma linha da tabela antes de aprovar ou rejeitar. |

## Veja também

- [Arquitetura](arquitetura.md)
- [Decisões de projeto](decisoes.md)
- [Interface gráfica](interface.md)
