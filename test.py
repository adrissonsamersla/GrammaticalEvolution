from evolutionIteration import evolutionIteration
import readCSV
lista = evolutionIteration(75)
print(lista)
melhor = sorted(lista, key = lambda x: x[0])
print(melhor[0][0])
print(melhor[0][1])
readCSV.writeCSV('sample.csv','testing.csv',melhor[0][1])