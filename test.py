from evolutionIteration import evolutionIteration
import readCSV
[lista] = evolutionIteration(10)
print(lista[0][0])
print(lista[0][1])
readCSV.writeCSV('sample.csv','testing.csv',lista[0][1])