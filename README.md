# Requisição de ordens por request no sistema DataSul

* Este projeto tem como objetivo, fazer a requisição http para o servidor do sistema DataSul e retornar algumas informações sobre as ordens de produção.

* Isso dará agilidade no processo de pesquisas de ordens, sem a necessidade de todos terem que acessaro sistema ou ter conhecimento.

* O frontEnd será desenvolvido em html, com isso não necessitará de nada nem de nenhum conhecimento de programação para utilizar o programa.

## **Inciando**

 Para usar o programa, inicialmente o programa terá para o usuário a opção de buscar informações no sistema por:

* Por faixa de ordem ou ordem, o programa fará a requisição colocando como parâmetro as ordens de produção.

* Por código, digitando o código desejado, o programa retornará todas as ordens abertas do código informado.

* Estado da ordem, por exemplo se a pessoa quiser o estado "liberada", retornará todas as ordens nesse estado.

* Múltiplos filtros poderão ser usados também.

## **Melhorias**

* O programa está limitado ao modelo de requisição para o ERP DataSul.

* A janela que é feita a requisição é a de *apontamento de ordens* do DataSul

## **Desenvolvimento**

### 1º Commit

* [X] Faz a requisição para o servidor do sistema e retorna um dataframe.
* [X] Trabalhar os dados deixando no formato e colunas desejadas.
* [X] ordenar e renomear as colunas e enviar todos os itens de acordo com a tabela criada.

### 2º Commit

* [X] Criar as funções que busca as ordens pelo código.
* [X] Criar as funções que busca as ordens pelo estado da ordem.
* [X] Criar a página html com o layout necessário.
* [X] linkar a página html com o script que traz as informações do servidor.
* [X] implementar o timestamp automático com datas limites de 1 ano. **(2022-09-05)**
* [X] Adicionar a requisição dos pedidos.
* [X] Fazer a requisição dos itens dos pedidos.
* [X] Unir as tabelas e gerar um arquivo relatório

### 3º Commit

* [X] Implementar a função de trazer os itens de pedidos específicos **(2022-09-30)**
* [X] Adicionar itens na tabela *pedidos* **(2022-10-03)**
* [X] Criar função para faixa de data, padrão deixa a faixa no mês e pode determinar a data inicial. **(2022-10-07)**
* [X] Criar a opção de enviar para o banco vários pedidos (problemas com a coluna *tipo*) **Descrição(01)*
* [ ] Limitar buscar como padrão apenas pedidos diferentes de ***Atendido total***

### 4º Commit

* [ ] Separar apenas os itens fabricados para insert no banco.
* [ ] Melhorar código para deixar as funções mais claras e autoexplicativas.
* [ ] Desenvolver o funcionamento do programa em outros computadores.
* [ ] Criar função para esolher a pasta para criação dos arquivos dos relatórios.
* [ ] inserir múltiplos itens no banco com *'tipo' diferentes*.
* [ ] Analisar a existência do pedido antes de fazer o insert (evitar duplicados)

## **Testes**

* Testes iniciais já realizados antes do primeiro commit
* Testes da geração do relatório **(2022-09-28)**
* Foi testado todas as funções implementadas até o momento: **(2022-10-03)**
    1. A geração dos pedidos (é requisitado todos os pedidos e eliminados os *atendido total*)
    2. Buscar apenas os itens do pedido selecionado (ainda não é possível buscar vários pedidos por causa da coluna *tipo*)
    3. Função de selecionar apenas as colunas necessárias para o fazer o insert no banco e preparado e enviado os dados para tabela *pedidos*
* Implementado e testado a configuração de pedidos por data **(2022-11-03)**
* **Descrição(01)** - O programa funciona com vários pedidos, mas apenas quando o tipo é igual para todos, atribuir melhorias nesse recurso futuramente.
