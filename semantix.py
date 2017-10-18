

from pyspark import SparkContext, SparkConf


'''
Setup inicial
'''

conf = SparkConf().setMaster('local').setAppName('semantix')

sc = SparkContext(conf=conf)

resultados = {}

'''
carrega as bases de dados

'''
#rawData1 = sc.textFile("access_log_Aug95")

rawData2 = sc.textFile("access_log_Jul95,access_log_Aug95")

#data1 = rawData1.map(lambda x: x.split(" "))#.collect #retorn list

data2 = rawData2.map(lambda x: x.split(" ")).filter(lambda x:len(x) > 2)#.collect #retorn list


'''
numero de hosts unicos
'''
exe1 = data2.map(lambda x:x[0]).distinct().count()

resultados['Host Unicos'] = exe1

print 'Resultado 1:', exe1

'''
total de retornos 404

'''

exe2 = data2.filter(lambda x:x[-2] =='404' ).count()

resultados['Total Retornos 404'] = exe2

print 'Resultado 2',exe2

'''
As 5 urls que contem mais retornos 404

'''


dataPair1 = data2.map(lambda x: (x[0],x[-2])).filter(lambda keyValue: keyValue[1]=='404')

dict = dataPair1.countByKey()

dict = sc.parallelize([dict])

dict = dict.flatMap(lambda x: x.items())

exe3 = dict.map(lambda x: (x[1], x[0])).sortByKey(ascending =False).take(5)

resultados['top 5  404'] = exe3

print 'Resultado 3 ', exe3

'''
retornos 404 por dia

'''


errosDia = data2.map(lambda x: (x[3][1:7], x[-2])).filter(lambda x:x[1]=='404').countByKey()

errosDia = sc.parallelize([errosDia])

exe4 = errosDia.flatMap(lambda x:x.items()).sortByKey()

resultados['erros dia'] = exe4.take(exe4.count())

print 'Resultado 4', exe4.take(exe4.count())


'''
total de bytes retornados

'''

exe5 = data2.filter(lambda x:x[-1] != '-').map(lambda x:int(x[-1])).reduce(lambda x, y: x+y)

resultados['total bytes'] = exe5

print 'Resultado 5',  exe5




'''
Salva Resultado

'''
rddResult = sc.parallelize([resultados])

rddResult = rddResult.flatMap(lambda x:x.items())

rddResult.saveAsTextFile('Resultados Finais.txt')

print 'Acabou'