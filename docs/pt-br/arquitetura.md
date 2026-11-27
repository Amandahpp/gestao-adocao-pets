# Arquitetura

O projeto usa o padrão **MVC simplificado**, com uma camada de acesso ao banco de dados. O código está dividido em quatro partes.

| Camada | Pasta | Função |
|---|---|---|
| Model | `src/models/` | Guarda os dados e as regras de negócio. |
| View | `src/views/` | Mostra as janelas e recebe os cliques. |
| Controller | `src/controllers/` | Liga as janelas às regras e ao banco. |
| DAO | `dao/` | Lê e grava as tabelas do PostgreSQL. Há um DAO para cada tabela. |

A pasta `database/` guarda o script das tabelas (`banco.sql`), os dados de exemplo (`insercao.sql`) e o módulo de conexão (`conexao.py`).

## Classes de cada camada

- **Model:** `Animal`, `Cachorro`, `Gato`, `AnimalFactory`, `Adotante`, `Abrigo`, `SolicitacaoAdocao`, `EstadoSolicitacao`, `EstadoPendente`, `EstadoAprovada` e `EstadoRejeitada`.
- **View:** `MainView`, `CadastroCachorroView`, `CadastroGatoView`, `CadastroAdotanteView`, `CadastroSolicitacaoView`, `ListagemAnimaisView` e `GerenciadorSolicitacoesView`. O arquivo `theme.py` define o estilo visual.
- **Controller:** a classe `Controller`. Ela cria o `Abrigo`, guarda a lista de adotantes, abre as janelas, chama os modelos e chama os DAOs.
- **DAO:** `AbrigoDAO`, `AdotanteDAO`, `AnimalDAO` e `SolicitacaoAdocaoDAO`. Eles usam as funções `transacao` e `executar` do módulo `database/conexao.py`.

## Dados em memória e no banco

Os dados ficam gravados no PostgreSQL. O programa também mantém uma cópia em memória. As janelas e as regras de negócio trabalham com essa cópia.

- Na abertura, o `Controller` lê o banco. Ele carrega os animais, os adotantes e as solicitações para as listas em memória.
- A cada operação, o `Controller` grava no banco. Se a gravação falha, o controller desfaz a mudança em memória e mostra uma mensagem de erro.
- Os identificadores dos animais e das solicitações vêm do banco.

## Modelo de dados

| Tabela | Colunas principais | Regras no banco |
|---|---|---|
| `Adotante` | `cpf` (chave primária), `nome`, `telefone` | O CPF é único. |
| `Abrigo` | `id`, `nome` | O nome é único. |
| `Animal` | `id`, `nome`, `idade`, `sexo`, `status`, `tipo`, `raca`, `pelagem`, `abrigo_id` | A idade é maior ou igual a zero. O sexo, o status e o tipo aceitam só valores fixos. Cachorro exige raça. Gato exige pelagem. |
| `SolicitacaoAdocao` | `id`, `animal_id`, `adotante_cpf`, `estado`, `status` | O estado é Pendente, Aprovada ou Rejeitada. Cada animal pode ter só uma solicitação pendente. |

Cachorros e gatos ficam na mesma tabela `Animal`. A coluna `tipo` indica qual classe criar ao ler.

## Fluxo de uma adoção

1. A pessoa escolhe um animal e um adotante em `CadastroSolicitacaoView`.
2. A view chama `Controller.cadastrar_solicitacao`.
3. O controller cria uma `SolicitacaoAdocao` com o estado `EstadoPendente`.
4. O controller pede ao `Abrigo` que registre a solicitação.
5. O `Abrigo` confere três regras. O animal está cadastrado. O animal está disponível. O animal não tem outra solicitação pendente. Se uma regra falha, o `Abrigo` gera um erro.
6. O controller pede ao `SolicitacaoAdocaoDAO` que grave a solicitação. Se a gravação falha, o controller tira a solicitação da memória.
7. O controller mostra uma mensagem de sucesso ou de aviso.
8. Em `GerenciadorSolicitacoesView`, a pessoa escolhe **Aprovar** ou **Rejeitar**. A view chama `Controller.alterar_solicitacao`.
9. A solicitação passa a ação para o objeto de estado atual.
10. O estado `EstadoPendente` executa a mudança em memória. Ao aprovar, ele muda o animal para "Adotado". Os outros estados geram um erro.
11. O controller abre uma transação. Ele grava a solicitação e o animal juntos. Se a gravação falha, o controller volta o estado da solicitação e o status do animal ao valor anterior.

## Limites desta etapa

Estes pontos não impedem o funcionamento. Podem ser melhorados em uma próxima etapa.

- O controller mostra mensagens com `messagebox`, que é um componente do Tkinter. No MVC estrito, essa tarefa é da view.
- As views leem as listas diretamente de `controller.abrigo`.
- A regra "animal disponível e sem solicitação pendente" aparece no `Controller` e em `CadastroSolicitacaoView`.
- A lista de adotantes fica no `Controller`. A lista de animais fica no `Abrigo`.
- O `Controller` conhece o módulo `database/conexao.py`. Ele abre a transação que reúne dois DAOs.
- A cópia em memória é carregada uma vez, na abertura. Se outra pessoa alterar o banco com o programa aberto, a tela não atualiza.
- Os status são textos soltos, como "Disponível" e "Pendente".
