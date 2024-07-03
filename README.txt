Do que se trata o desafio da DropSmart:

Aqui na Dropsmart nós trabalhamos como afiliados da Shopify. Basicamente, toda vez que um aluno nosso ou de um parceiro cria uma e-commerce nessa plataforma e paga pelo 1º mês de trial e o 1º mês cheio, recebemos uma comissão.
Há 3 eventos rastreáveis nessa conversão:
* Free Trial API: Conta criada
* Paid Trial API: 1º mês de trial pago
* Online Conversion API: 1º mês cheio pago

Vou te passar um arquivo .csv abaixo.

Seu objetivo é criar um relatório por canal (definidos pelas colunas de SubIDs).
Esse relatório deve conter faturamento atual, previsão de faturamento pelos eventos de free trial e paid trial já rastreados e qualquer outro dado que você considerar relevante adicionar.


O primeiro passo do nosso projeto foi tratar os dados utilizando o próprio excel, transformando as linhas em colunas e assim tratando os dados para sua leitura ser realizada com sucesso pelo python.

Após isso, salvamos o arquivo em formato excel para facilitar a leitura pelo python, e iniciamos a nossa construção do relatório.

Primeiramente importamos a biblioteca pandas, matplotlib e calendar para dar andamento na construção do relatório.

Decidi criar várias visualizações para mostrar no relatório as diversas nuancias que os dados me mostravam, e também para atender ao que foi solicitado no desafio proposto (Relatório por canal, que continha faturamento atual e previsão de faturamento via free trial e paid trial)

Assim, criei todos os relatórios e também calculei no excel a taxa de conversão média dos primeiros seis meses dos paid trials e free trials que se converteram em vendas (Online Conversion e POS Pro Sale) de 2024 (0.2559), para multiplicar com todos os free trials e paid trials de junho e assim obter a previsão de faturamento para o mês de julho.

Você encontrará neste repositório dois arquivos .py, um é a base escolhida para construir a base dos cálculos do projeto e chegar as visualizações prévias desejadas, e o segundo é o relatório final, contendo todos os gráficos consolidados em um arquivo só e utilizando subplots para uma tela final com todos os gráficos.

*Informação importante* Para conseguir rodar o relatório com sucesso na máquina, abra o repositório como pasta, não os arquivos .py individualmente.

Também inclui um PDF para visualização do relatório antecipadamente.

Qualquer dúvida ou sugestão para melhoria por favor entre em contato!

luizarthurwinter@gmail.com