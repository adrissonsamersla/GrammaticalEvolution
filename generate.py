from random import randrange
from math import exp,log,sqrt,cos,sin
from readCSV import readCSV
from Grammar import derivacao

overFlowError = 1000000000

def generateChromos(sizeChromo,rangeLimit):
    """ Função geradora dos cromossomos, com valores aleatórios entre [0,rangeLimit) """
    chromos = []
    
    for i in range(0,sizeChromo):
        chromos.append(randrange(rangeLimit))
    
    return chromos

def generateEquation(expression):
    """Função geradora de f(X) para a string inserida"""
    return lambda X1,X2,X3,X4,X5,X6,X7,X8: eval(expression)

def generatePopulation(populationSize,sizeChromo,rangeLimit = 255):
    """Função geradora de população chromossomos, com tamanho igual a populationSize"""
    chromoList = []

    for single in range(0,populationSize):
        chromoList.append(generateChromos(sizeChromo,rangeLimit))
    
    return chromoList

def generate_error_expression_list(data,chromoList):

    """Função responsável por calcular o erro e devolver a expressão relativa ao erro calculado"""

    ##############Pre-Sets#############
    errorAverage = []  
    expressionList = []
    rows_data = len(data)
    populationSize = len(chromoList)
    ###################################
        
    for single in range(0,populationSize):
        
        error = []
        expression = derivacao(chromoList[single]) #Calcula a expressão baseado na gramática pre determinada
        expressionList.append(expression) #Recebe as expressão dependendo do cromossomo
        print(expression)
        function = generateEquation(expressionList[single]) #Calcula a função

        for i in range(0,rows_data):
            try:
                [id,*args,f_real] = data[i].values()
                e = abs((f_real - function(*args))**2)

            except ValueError:
                e = overFlowError
            
            except OverflowError:
                e = overFlowError

            except ZeroDivisionError:
                e = overFlowError
            

            error.append(e)
            
        errorAverage.append((sum(error)/rows_data))
    
    return [errorAverage,expressionList]
