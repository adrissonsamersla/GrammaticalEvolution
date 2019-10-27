from random import randrange,random

def tournament(chromosList,errorAverage):
    
    """Função é responsável por selecionar aleatoriamente os chromossomos e selecionar os mais aptos a seguirem"""
    afterTournamentList = []
    sizeList = len(chromosList)

    for i in range(0,sizeList):
        
        posicA = randrange(sizeList)
        posicB = randrange(sizeList)

        if errorAverage[posicA] < errorAverage[posicB]:
            posicWinner = posicA
        else:
            posicWinner = posicB

        chromoWinner = chromosList[posicWinner]
        afterTournamentList.append(chromoWinner)

    return afterTournamentList


def crossing(singleA,singleB):
    
    """Função responsável pelo provável cruzamento dos chromossomos"""

    lenChromo = len(singleA)
    randPosic = randrange(lenChromo)
    
    newSingleA = []
    newSingleB = []

    newSingleA.extend(singleA[:randPosic])
    newSingleA.extend(singleB[randPosic:])

    newSingleB.extend(singleB[:randPosic])
    newSingleB.extend(singleA[randPosic:])

    return [newSingleA,newSingleB]


def mutation(chromosList):
    """Função que promove a mutação e o cruzamento de acordo com as probabilidades estipuladas"""
    newGeneration = []
    probCrossing = 0.8
    probMutation = 0.1
    rangeLimit = 255
    
    while chromosList:
        
        if len(chromosList) != 1:

            singleA = chromosList.pop()
            singleB = chromosList.pop()

            if random() < probCrossing:
               [newSingleA,newSingleB] = crossing(singleA,singleB)
               newGeneration.append(newSingleA)
               newGeneration.append(newSingleB)

            
            else:
                newGeneration.append(singleA)
                newGeneration.append(singleB)


        else: newGeneration.append(chromosList.pop())
    

    for l in newGeneration:
        sizeL = len(l)
        for i in range(0,sizeL):
            if random() < probMutation:
                l[i] = randrange(rangeLimit)
        

    return newGeneration
        
def evolve(chromosList,errorAverage):
    """Função principal responsável por chamar todas as funções desse arquivo"""

    evolvedList = mutation(tournament(chromosList,errorAverage))
    return evolvedList