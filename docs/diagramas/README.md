# Diagramas UML

Os diagramas estão em formato PlantUML (`.puml`). Cada arquivo `.puml` gera uma imagem `.png` com o mesmo nome.

| Arquivo | O que mostra |
|---|---|
| `casos-de-uso` | As ações do operador no sistema. |
| `classes` | As classes do domínio e suas relações. |
| `componentes-mvc` | As três camadas do MVC e as dependências entre elas. |
| `sequencia-adocao` | O registro e a aprovação de uma solicitação. |
| `atividades-cadastro` | O fluxo de cadastro de um animal. |
| `atividades-adocao` | O processo completo de adoção. |

## Como gerar as imagens

1. No VS Code, instale a extensão **PlantUML**.
2. Abra um arquivo `.puml`.
3. Pressione `Alt + D` para ver o diagrama.
4. Exporte para PNG pelo menu da extensão.

Outra opção: cole o texto do arquivo em um servidor PlantUML on-line.

## Observação

O `classes` mostra só as classes do domínio. O `Controller` aparece no `componentes-mvc`.
