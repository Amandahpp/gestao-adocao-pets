# Decisões de projeto

## D1 — Arquitetura MVC

**Decisão:** separar modelos, controlador e interfaces. **Motivo:** reduzir dependências entre regras e janelas. **Aplicação:** `src/models/`, `src/controllers/controller.py` e `src/views/`. O controlador recebe eventos da interface e chama os modelos.

## D2 — Factory

**Decisão:** usar `AnimalFactory.criar_animal`. **Motivo:** centralizar a criação de cães e gatos. **Aplicação:** `src/models/animal_factory.py`. O controlador informa o tipo de animal. A Factory escolhe `Cachorro` ou `Gato`.

## D3 — Singleton

**Decisão:** manter uma instância de `Abrigo`. **Motivo:** compartilhar a lista de animais e solicitações durante a execução. **Aplicação:** `src/models/abrigo.py`, com `__new__`. **Limite:** o Singleton mantém estado global no processo. Por isso, os testes isolam o estado entre casos.

## D4 — State

**Decisão:** representar as solicitações com estados `Pendente`, `Aprovada` e `Rejeitada`. **Motivo:** definir quais ações são permitidas em cada situação. **Aplicação:** `src/models/estado_solicitacao.py`, `estados.py` e `solicitacao_adocao.py`. A aprovação de uma solicitação pendente também altera o animal para `Adotado`.

## D5 — Interface Tkinter

**Decisão:** usar Tkinter e `ttk`. **Motivo:** utilizar componentes básicos da biblioteca padrão. **Aplicação:** janelas, rótulos, campos, caixas de seleção, tabelas e botões com eventos.

## D6 — Dados em memória

**Decisão:** não implementar persistência nesta entrega. **Consequência:** os cadastros desaparecem quando o programa fecha. O projeto não deve ser apresentado como sistema com banco de dados.

## D7 — Validação

**Decisão:** validar campos no modelo e comunicar erros pelo controlador. O CPF tem verificação de tamanho, mas não de dígitos verificadores. A idade aceita zero e números inteiros positivos.
