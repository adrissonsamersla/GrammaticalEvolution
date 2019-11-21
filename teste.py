from evolutionIteration import evolutionIteration
import readCSV

exp = "(X1-((X4*sqrt(abs((X1*X4))))-sqrt(abs(X8))))"

readCSV.writeCSV('sample.csv','testing.csv',exp)