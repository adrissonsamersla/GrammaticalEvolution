from random import randrange
from math import exp,log,sqrt,cos,sin
from readCSV import readCSV

def generateChromos(sizeChromo,rangeLimit):
    
    chromos = []
    
    for i in range(0,sizeChromo):
        chromos.append(randrange(rangeLimit))
    
    return chromos

def generateEquation(expression):
    
    return lambda X1,X2,X3,X4,X5,X6,X7,X8: eval(expression)

def generatePopulation(populationSize):
    ##############Pre-Sets###############
    sizeChromo = 10
    rangeLimit = 255
    chromoList = []

    for single in range(0,populationSize):
        chromoList.append(generateChromos(sizeChromo,rangeLimit))
    
    return chromoList

def generate_error_expression_list(data,chromoList):

    ##############Pre-Sets#############
    errorAverage = []  
    expressionList = []
    rows_data = len(data)
    populationSize = len(chromoList)
    ###################################
        
    for single in range(0,populationSize):
        
        error = []
        
        expressionList.append('X1*X2 + 3.5*exp(X1*X1)') #Recebe as expressão dependendo do cromossomo
        
        function = generateEquation(expressionList[single]) #Calcula a função

        for i in range(0,rows_data):
            
            [id,*args,f_real] = data[i].values()
            e = abs((f_real - function(*args))**2)
            error.append(e)
            
        errorAverage.append((sum(error)/rows_data).round(5))
    
    return [errorAverage,expressionList]
