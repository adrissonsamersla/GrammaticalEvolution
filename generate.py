from random import randrange
from math import exp,log,sqrt,cos,sin

def generateChromos(sizeChromo,rangeLimit):
    
    chromos = []
    
    for i in range(0,sizeChromo):
        chromos.append(randrange(rangeLimit))
    
    return chromos

def generateEquation(expression):
    
    return lambda x1,x2,x3,x4,x5,x6,x7,x8: eval(expression)

