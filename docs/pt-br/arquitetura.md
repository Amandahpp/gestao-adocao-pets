# Arquitetura do sistema

O projeto utiliza uma organização **MVC simplificada**.

- **Model:** contém `Animal`, `Cachorro`, `Gato`, `Adotante`, `Abrigo` e `SolicitacaoAdocao`. Aplica as regras de negócio.
- **View:** contém janelas Tkinter. Mostra campos e tabelas. Encaminha eventos para o controlador.
- **Controller:** recebe ações da interface. Valida o fluxo, chama os modelos e apresenta mensagens.

## Fluxo de adoção

1. A pessoa seleciona um animal disponível e um adotante.
2. A interface envia os índices ao controlador.
3. O controlador cria `SolicitacaoAdocao` e pede ao abrigo que registre a solicitação.
4. O abrigo impede solicitações duplicadas pendentes para o mesmo animal.
5. O controlador recebe o pedido de aprovação ou rejeição.
6. O objeto de estado executa a transição permitida.
7. Se houver aprovação, o animal passa para `Adotado`.

## Limites

O programa não possui autenticação, banco de dados ou integração com serviços externos. O uso previsto é uma demonstração acadêmica local.
