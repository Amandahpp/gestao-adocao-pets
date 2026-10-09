# Guia do usuário — Português

## Objetivo

O sistema ajuda a organizar adoções de cães e gatos. Os dados ficam na memória enquanto o programa está aberto.

## Como usar

1. Execute `python main.py` na pasta principal.
2. Clique em **Cadastrar Cachorro** ou **Cadastrar Gato**. Preencha os campos. Clique em **Salvar**.
3. Clique em **Cadastrar Adotante**. Informe nome, CPF com 11 dígitos e telefone. Clique em **Salvar**.
4. Clique em **Nova Solicitação**. Escolha o animal e o adotante. Clique em **Enviar solicitação**.
5. Clique em **Gerenciar Solicitações**. Selecione uma linha. Clique em **Aprovar** ou **Rejeitar**.
6. Clique em **Listar Animais** para consultar a situação dos animais.

## Atenção

- O sistema não salva dados em arquivos ou banco de dados.
- Um animal adotado não pode receber nova solicitação.
- Uma solicitação concluída não pode ser alterada.
- O sistema verifica o tamanho do CPF, mas não confirma se o CPF é válido.

Veja [decisões](decisoes.md), [arquitetura](arquitetura.md) e [interface](interface.md).
