# neoway

Desafio Técnico - Pessoa Desenvolvedora de

Software (Governança de Dados)

Primeiramente, gostaríamos de agradecer o seu interesse e disponibilidade em avaliar nossa
oportunidade. Nessa etapa do processo seletivo queremos que você coloque a “mão na massa” e
mostre para a gente um pouco do seu repertório técnico.
Objetivo
Nosso desafio tem como objetivo dar oportunidade para que você nos apresente com mais
profundidade sua experiência em criar soluções para os desafios e problemas do dia a dia.
O desafio foi dividido em duas partes e para entregá-lo, você deve realizar o upload em um
repositório público no Github e nos encaminhar o link do projeto via e-mail:
a) Desenvolvimento de um ETL utilizando as tecnologias Python ou Go para desenvolvimento e
PostgreSQL ou MySQL para SGBD.
b) Criação de um dashboard utilizando o PowerBI.

Agendaremos uma data para que você possa nos apresentar as duas partes do desafio e
possamos tirar dúvidas e aprender juntos.

Parte 1 - Desenvolvimento do ETL
Você deve realizar a extração dos dados fornecidos pela API pública RandomUser, realizar
algumas transformações nos dados e apresentá-los em um Dashboard criado no PowerBI.
Essa API tem a finalidade de testar aplicações gerando dados aleatórios de usuários,
retornando diversos campos interessantes, como Nome, Naturalidade e Data de nascimento.

Orientações
Extração/Extract
- Você deve extrair uma amostra aleatória de 5.000 (5 mil) registros com Naturalidade BR.
Acesse a documentação para entender como realizar esse filtro
- Não é necessário extrair os dados de todos os campos da API, somente os campos abaixo
são interessantes para nós:
gender, name.first, name.last, dob.date, email, phone, cell, nat, location.street.name,
location.street.number, location.city, location.postcode, location.country,
location.coordinates.latitude, location.coordinates.longitude, registered.date.

Transformação/Transform
- Além das orientações abaixo, você deve padronizar e higienizar os dados da forma que
julgar mais interessante. Na apresentação do desafio esperamos que justifique as decisões
tomadas nessa etapa de transformação.
Orientações
● Você não deve utilizar o campo “age” da api. Gostaríamos que criasse uma nova coluna
calculando a idade do usuário;
● Deve ser criado o campo "enderecoCompleto" unindo todas as partículas de endereço com
exceção das coordenadas;
● Deve ser criado um campo de metadado de classificação dos usuários, conforme a regra
abaixo:
○ Crianças - usuários menores de 12 anos;
○ Adolescentes - usuários de até 18 anos;
○ Maiores de idade - usuários maiores de 18 anos.
● Deve ser criado um campo de metadado de “Finalidade de Uso”, conforme a regra abaixo:
○ Produtos de Marketing - Somente maiores de Idade;
○ Produtos de Riscos - Maiores de Idade e Adolescentes.
● Deve ser criado um campo de metadado de origem (URL da consulta na API).
● Deve ser criado um campo de metadado de data de processamento (a ser estampada no
momento de LOAD no banco de dados).

Carregamento/Load
- Você deve armazenar os dados em uma base de dados em SQL, utilizando PostgreSQL ou
MySQL.
- Você deve modelar a base de dados de forma que os dados sejam organizados como
Entidades de Relacionamento aplicando regras de normalização.
- Você deve seguir as boas práticas de utilização de tipos de dados, nomes de tabelas e
colunas.

Parte 2 - Criação do painel no PowerBI
Agora que você já armazenou os 5.000 registros aleatórios, extraídos da API RandomUser, você
deve dar a visibilidade desses dados. Para isso, gostaríamos que criasse um painel no PowerBI com
as seguintes visões:

Aba 1
● Visualização dos registros extraídos, com todos os campos aparentes em um componente
de tabela.
● Criação de ao menos 2 filtros: “Finalidade de Uso”, “Classificação de Usuários”. Se entender
que algum outro campo pode ser útil para ser realizado em um filtro, pode ficar à vontade
para criá-lo.

Aba 2
Pedimos para que você classifique os usuários de acordo com sua idade. Isso é necessário
pois você deve dar a visibilidade da quantidade de usuários menores de idade para que a área
responsável possa realizar a deleção desses dados. Por isso, nessa segunda aba exercite sua
criatividade para dar uma visibilidade dos usuários menores de idades, quantidade de usuários por
finalidade de uso, e outras coisas legais que você julga interessante apresentar.

Extra
Se identificar outras visões ou ações para governar os dados, fique à vontade para
descrevê-las ou criar outras abas no painel construído no PowerBI.

Bom desenvolvimento e boa sorte!
Data Excellence - Neoway
