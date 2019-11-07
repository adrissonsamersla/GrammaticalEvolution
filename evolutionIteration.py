from generate import generatePopulation,generate_error_expression_list
from readCSV import readCSV
from evolve import evolve

def evolutionIteration(numberGenerations):    
    
    populationSize = 2000
    sizeChromo = 500
    #rangeLimit = 255
    data = readCSV('training.csv')
    
    chromoList = generatePopulation(populationSize,sizeChromo)
    
    [errorAverage,expressionList] = generate_error_expression_list(data,chromoList)

    for i in range(0,numberGenerations):
        chromoList = evolve(chromoList,errorAverage)
        [errorAverage,expressionList] = generate_error_expression_list(data,chromoList)
    
    optimalList = sorted(tuple(zip(errorAverage,expressionList)),key = lambda x: x[0])
    
    optimalExpression = optimalList[0][1]
    optimalError = optimalList[0][0]

    return [optimalList]
    

    

