# Questões 

##Respostas Questões Iniciais:

Qual o objetivo do comando cache em Spark? 

Armazenar informações na memória RAM ao invés de em disco, assim o acesso a informação pode ser feito em velocidades bem diferentes (disco  ˜10-3    RAM ˜10-9  segundos ),  o que torna o comando cache atrativo e potencializador do sucesso do spark framework.
O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?

Por que o o Spark Framework permite processamento em memória sem a necessidade prévia de acesso ao disco, que é o modo de operação do MapReduce.

Qual é a função do SparkContext ?

Tem a função de representação/instância da conexão com o cluster, com ele é possível realizar a configuração e a partir dela realizar em broadcast as ações e transformações no RDD.



Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

RDD é o cubo de informações (construído por diversos objetos) gerado a partir de um processo de ETL, com ele pode-se realizar outras transformações, o que gera outros RDDs, ou até mesmo ações e assim extrair informações resumidas.



GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê? 

Porque o groupByKey cria  uma lista para cada Key durante o processo, ou seja, um novo objeto, o que demanda mais operações e por sua vez mais tempo, além do consumo de memória.



Explique o que o código abaixo faz:

Linha 1 - Carrega o RDD

Linha 2.1 Retorna um RDD, onde cada palavra de cada linha se torna um item, no caso de estiver separada por um espaço.

Linha 2.2 - Retorna um RDD, onde cada palavra é agrupada por chave, e cada chave é a letra que está na segunda posição da palavra.

Linha 2.3 - Retorna um RDD, onde há um agrupamento por chave, ou seja, todas as palavras que contém a mesma chave agora estão no mesmo grupo.

Linha 3  - O RDD é persistido. 


##Questões Práticas -  Também estão do diretorio de resultados finais.

('erros dia', [(u'01/Aug', 243), (u'01/Jul', 316), (u'02/Jul', 291), (u'03/Aug', 304), (u'03/Jul', 474), (u'04/Aug', 346), (u'04/Jul', 359), (u'05/Aug', 236), (u'05/Jul', 497), (u'06/Aug', 373), (u'06/Jul', 640), (u'07/Aug', 537), (u'07/Jul', 570), (u'08/Aug', 391), (u'08/Jul', 302), (u'09/Aug', 279), (u'09/Jul', 348), (u'10/Aug', 315), (u'10/Jul', 398), (u'11/Aug', 263), (u'11/Jul', 471), (u'12/Aug', 196), (u'12/Jul', 471), (u'13/Aug', 216), (u'13/Jul', 532), (u'14/Aug', 287), (u'14/Jul', 413), (u'15/Aug', 327), (u'15/Jul', 254), (u'16/Aug', 259), (u'16/Jul', 257), (u'17/Aug', 271), (u'17/Jul', 406), (u'18/Aug', 256), (u'18/Jul', 465), (u'19/Aug', 209), (u'19/Jul', 639), (u'20/Aug', 312), (u'20/Jul', 428), (u'21/Aug', 305), (u'21/Jul', 334), (u'22/Aug', 288), (u'22/Jul', 192), (u'23/Aug', 345), (u'23/Jul', 233), (u'24/Aug', 420), (u'24/Jul', 328), (u'25/Aug', 415), (u'25/Jul', 461), (u'26/Aug', 366), (u'26/Jul', 336), (u'27/Aug', 370), (u'27/Jul', 336), (u'28/Aug', 410), (u'28/Jul', 94), (u'29/Aug', 420), (u'30/Aug', 571), (u'31/Aug', 526)])
('Total Retornos 404', 20901)
('total bytes', 65524314915)
('Host Unicos', 137978)
('top 5  404', [(251, u'hoohoo.ncsa.uiuc.edu'), (157, u'piweba3y.prodigy.com'), (132, u'jbiagioni.npt.nuwc.navy.mil'), (114, u'piweba1y.prodigy.com'), (91, u'www-d4.proxy.aol.com')])



