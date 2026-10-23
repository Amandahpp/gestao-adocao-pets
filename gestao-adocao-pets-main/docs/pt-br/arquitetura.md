# Arquitetura

O projeto usa o padrão **MVC simplificado**. O código está dividido em três pastas.

| Camada | Pasta | Função |
|---|---|---|
| Model | `src/models/` | Guarda os dados e as regras de negócio. |
| View | `src/views/` | Mostra as janelas e recebe os cliques. |
| Controller | `src/controllers/` | Liga as janelas às regras. |

## Classes de cada camada

- **Model:** `Animal`, `Cachorro`, `Gato`, `AnimalFactory`, `Adotante`, `Abrigo`, `SolicitacaoAdocao`, `EstadoSolicitacao`, `EstadoPendente`, `EstadoAprovada` e `EstadoRejeitada`.
- **View:** `MainView`, `CadastroCachorroView`, `CadastroGatoView`, `CadastroAdotanteView`, `CadastroSolicitacaoView`, `ListagemAnimaisView` e `GerenciadorSolicitacoesView`. O arquivo `theme.py` define o estilo visual.
- **Controller:** a classe `Controller`. Ela cria o `Abrigo`, guarda a lista de adotantes, abre as janelas e chama os modelos.

## Fluxo de uma adoção

1. A pessoa escolhe um animal e um adotante em `CadastroSolicitacaoView`.
2. A view chama `Controller.cadastrar_solicitacao`.
3. O controller cria uma `SolicitacaoAdocao` com o estado `EstadoPendente`.
4. O controller pede ao `Abrigo` que registre a solicitação.
5. O `Abrigo` confere três regras. O animal está cadastrado. O animal está disponível. O animal não tem outra solicitação pendente. Se uma regra falha, o `Abrigo` gera um erro.
6. O controller mostra uma mensagem de sucesso ou de aviso.
7. Em `GerenciadorSolicitacoesView`, a pessoa escolhe **Aprovar** ou **Rejeitar**. A view chama `Controller.alterar_solicitacao`.
8. A solicitação passa a ação para o objeto de estado atual.
9. O estado `EstadoPendente` executa a mudança. Ao aprovar, ele muda o animal para "Adotado". Os outros estados geram um erro.

## Limites desta etapa

Estes pontos não impedem o funcionamento. Podem ser melhorados em uma próxima etapa.

- O controller mostra mensagens com `messagebox`, que é um componente do Tkinter. No MVC estrito, essa tarefa é da view.
- As views leem as listas diretamente de `controller.abrigo`.
- A regra "animal disponível e sem solicitação pendente" aparece no `Controller` e em `CadastroSolicitacaoView`.
- A lista de adotantes fica no `Controller`. A lista de animais fica no `Abrigo`.
- Os status são textos soltos, como "Disponível" e "Pendente".
- Não há persistência. Os dados ficam na memória.
