from random import randrange,random

def tournament(chromosList,errorAverage):
    
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
    
    newGeneration = []
    probCrossing = 0.8
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
            if random() < 0.1:
                l[i] = randrange(rangeLimit)
        

    return newGeneration
        
def evolve(chromosList,errorAverage):
    evolvedList = mutation(tournament(chromosList,errorAverage))
    return evolvedList