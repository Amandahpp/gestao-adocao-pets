# Guia do usuário

## Objetivo

O sistema ajuda a organizar a adoção de cachorros e gatos. O sistema grava os dados em um banco de dados PostgreSQL. Os dados continuam disponíveis depois que você fecha o programa.

## Iniciar o programa

1. Confirme que o PostgreSQL está em execução e que o banco foi criado. Veja o [README principal](../../README.md).
2. Abra um terminal na pasta que contém o arquivo `main.py`.
3. Execute o comando `python main.py`.

O programa conecta ao banco. Depois, ele carrega os animais, os adotantes e as solicitações já gravados. Se o banco estiver indisponível, o programa mostra a mensagem **Banco de dados indisponível** e fecha.

A janela **Patinhas Felizes | Gestão de Adoções** mostra seis cartões. Para abrir uma função, clique em **Abrir →** no cartão.

A janela **Patinhas Felizes | Gestão de Adoções** mostra seis cartões. Para abrir uma função, clique em **Abrir →** no cartão.

## Cadastrar um animal

1. Clique em **Abrir →** no cartão **Cadastrar cachorro** ou **Cadastrar gato**.
2. Preencha **Nome** e **Idade (anos)**.
3. Escolha o **Sexo**: Macho ou Fêmea.
4. Preencha **Raça** (cachorro) ou **Pelagem** (gato).
5. Clique em **Salvar cadastro**.

O sistema grava o animal no banco de dados. Depois, mostra uma mensagem de sucesso. A janela fecha. O animal recebe o status "Disponível".

## Cadastrar um adotante

1. Clique em **Abrir →** no cartão **Cadastrar adotante**.
2. Preencha **Nome**, **CPF** e **Telefone**.
3. Clique em **Salvar cadastro**.

O CPF deve ter 11 dígitos. O sistema ignora pontos e traços. Cada CPF pode ser cadastrado uma vez. O sistema grava o adotante no banco de dados.

## Criar uma solicitação de adoção

1. Clique em **Abrir →** no cartão **Nova solicitação**.
2. Escolha o animal na lista **Animal**.
3. Escolha o adotante na lista **Adotante**.
4. Clique em **Enviar solicitação**.

A lista de animais mostra somente animais disponíveis e sem solicitação pendente. A solicitação nova tem o status "Pendente". O sistema grava a solicitação no banco de dados.

## Aprovar ou rejeitar uma solicitação

1. Clique em **Abrir →** no cartão **Gerenciar solicitações**.
2. Selecione uma linha da tabela.
3. Clique em **Aprovar** ou **Rejeitar**.

Resultado:

- **Aprovar:** a solicitação passa a "Aprovada". O animal passa a "Adotado".
- **Rejeitar:** a solicitação passa a "Rejeitada". O animal continua "Disponível" e volta para a lista de **Nova solicitação**.

O sistema grava a solicitação e o animal juntos. Se a gravação falhar, nenhum dos dois muda.

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
| Banco de dados indisponível | O programa não conseguiu conectar ao banco. Confirme que o PostgreSQL está em execução. Confira o nome do banco e a senha. Abra o programa de novo. |
| Erro no banco de dados | Uma operação falhou no banco. O sistema desfez a operação. Tente de novo. Veja a seção "Problemas comuns" no README principal. |

## Veja também

- [Arquitetura](arquitetura.md)
- [Decisões de projeto](decisoes.md)
- [Interface gráfica](interface.md)
