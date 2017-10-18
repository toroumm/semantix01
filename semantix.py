
from pyspark.sql import Row

from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf


'''
Setup inicial
'''

conf = SparkConf().setMaster('local').setAppName('semantix')

sc = SparkContext(conf=conf)

'''
carrega as bases de dados

'''
rawData1 = sc.textFile("access_log_Aug95,access_log_Jul95")

#rawData2 = sc.textFile("access_log_Jul95")

data1 = rawData1.map(lambda x: x.split(" "))#.collect #retorn list

'''
numero de hosts unicos
'''
#exe1 = data1.map(lambda x:x[0]).distinct().count()

'''
total de retornos 404

'''
#exe2 = data1.filter(lambda x:x[-2] =='404' ).count()

'''
As 5 urls que contem mais retornos 404

'''

'''
dataPair1 = rawData1.map(lambda x: (x.split(" ")[0],x.split(" ")[-2])).filter(lambda keyValue: keyValue[1]=='404')

dict = dataPair1.countByKey()

dict = sc.parallelize([dict])

dict = dict.flatMap(lambda x: x.items())

exe3 = dict.map(lambda x: (x[1], x[0])).sortByKey(ascending =False).take(5)

'''

'''
retornos 404 por dia

'''

'''
errosDia = data1.map(lambda x: (x[3][1:7], x[-2])).filter(lambda x:x[1]=='404').countByKey()

errosDia = sc.parallelize([errosDia])

exe4 = errosDia.flatMap(lambda x:x.items()).sortByKey()

print exe4.take(exe4.count())
'''


'''
total de bytes retornados

'''
exe4 = data1.filter(lambda x:x[-1] != '-').map(lambda x:int(x[-1])).reduce(lambda x, y: x+y)

print exe4

print 'Acabou'