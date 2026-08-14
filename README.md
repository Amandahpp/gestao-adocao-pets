# Gestão de Adoção de Pets

Sistema gráfico integrado à banco de dados que tem como intuito aproximar animais em centros de adoção e pessoas que desejam adotar.

Foram utilizados os seguintes padrões de projeto para auxiliar no desenvolvimento:
-

# Funcionalidades
- Cadastro de animais: características, idade, dados de saúde
- Cadastro de pessoas interessadas a adotar: preferências, tipo de residência, contato
- Listagem de animais e adotantes
- Gerenciamento de solicitações: abertura, aprovação, rejeição

# Instalação
O programa não precisa de instalação, bastando que os arquivos estejam disponíveis localmente em uma máquina com interpretador python.

dependências:
- python
- git

```
git clone https://github.com/Amandahpp/gestao-adocao-pets.git
cd gestao-adocao-pets
python -m src.main
```

# Integrantes do projeto

- Amanda Andreis Hoppe
- Ana Paula de Oliveira Andreis
- Elise C. de Lara
- Maria Eduarda de Chaves

# Classes do Sistema

## Animal

Classe abstrata que representa um animal genérico no sistema. Possui atributos comuns a todos os animais, como id, nome, idade, sexo e status.

## Cachorro

Classe que herda de Animal e representa um cachorro. Possui o atributo específico raça e implementa o método exibir_dados.

## Gato

Classe que herda de Animal e representa um gato. Possui o atributo específico pelagem e implementa o método exibir_dados.

## Adotante

Representa uma pessoa interessada em adotar um animal. Armazena nome, CPF e telefone.

## SolicitacaoAdocao

Representa o pedido de adoção de um animal por um adotante. Utiliza o padrão State para controlar o estado da solicitação.

## EstadoSolicitacao

Classe abstrata que define os métodos que todos os estados da solicitação devem implementar: aprovar e rejeitar.

## EstadoPendente, EstadoAprovada e EstadoRejeitada

Classes concretas que representam os possíveis estados de uma solicitação de adoção.

## AnimalFactory

Classe responsável por aplicar o Factory Pattern, centralizando a criação de objetos do tipo Cachorro e Gato.

## Abrigo

Classe responsável por gerenciar os animais e as solicitações do sistema. Implementa o Singleton Pattern para garantir que exista apenas uma instância do abrigo durante a execução.
