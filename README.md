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

* [X] Faz a requisição para o servidor do sistema e retorna um dataframe.
* [X] Trabalhar os dados deixando no formato e colunas desejadas.
* [X] ordenar e renomear as colunas e enviar todos os itens de acordo com a tabela criada.
* [ ] Criar as funções que busca as ordens pelo código.
* [ ] Criar as funções que busca as ordens pelo estado da ordem.
* [ ] Criar a página html com o layout necessário.
* [ ] linkar a página html com o script que traz as informações do servidor.
