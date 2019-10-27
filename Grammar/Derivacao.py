import sys

from Config import configs
from .SymbolsEnum import *

def acha_primeiro(lista):
    """
        Acha o primeiro símbolo não-terminal na lista.
        Retorna a posição e o símbolo.
        Caso não ache um não-terminal, retorna [-1,0].
    """
    cont = 0
    for prim in lista:
        if (type(prim) == NaoTerminal):
            return [cont, prim]
        cont = cont + 1
    return [-1,0]

def gera_producoes(cromossomo):
    """
        Gera produções segundo a gramática especificada em SymbolsEnum.
        Recebe uma lista de números entre 0 e 255 que servirão para sortear os símbolos.
        Retorna uma lista de enums (segundo SymbolsEnum).
    """
    l = [NaoTerminal.EXPRESSION]

    cont = 0
    numVoltas = 0
    while (numVoltas < configs["NUM_VOLTAS_CROMOSSOMO"]):
        
        [pos_primeiro, element] = acha_primeiro(l)
        if (pos_primeiro == -1):
            break

        ci = cromossomo[cont]

        if (element == NaoTerminal.EXPRESSION):
            op = ci % 4

            if (op == 0):
                l[pos_primeiro] = Parenteses.ABRE_PAR
                l.insert(pos_primeiro + 1, NaoTerminal.EXPRESSION)
                l.insert(pos_primeiro + 2, NaoTerminal.BIN_OP)
                l.insert(pos_primeiro + 3, NaoTerminal.EXPRESSION)
                l.insert(pos_primeiro + 4, Parenteses.FECHA_PAR)
            elif (op == 1):
                l[pos_primeiro] = NaoTerminal.UNI_OP
                l.insert(pos_primeiro + 1, Parenteses.ABRE_PAR)
                l.insert(pos_primeiro + 2, NaoTerminal.EXPRESSION)
                l.insert(pos_primeiro + 3, Parenteses.FECHA_PAR)
            elif (op == 2):
                l[pos_primeiro] = NaoTerminal.VAR
            else:
                l[pos_primeiro] = NaoTerminal.CONST

        elif (element == NaoTerminal.VAR):
            op = ci % 8
            if (op == 0):
                l[pos_primeiro] = Variavel.X1
            elif (op == 1):
                l[pos_primeiro] = Variavel.X2
            elif (op == 2):
                l[pos_primeiro] = Variavel.X3
            elif (op == 3):
                l[pos_primeiro] = Variavel.X4
            elif (op == 4):
                l[pos_primeiro] = Variavel.X5
            elif (op == 5):
                l[pos_primeiro] = Variavel.X6
            elif (op == 6):
                l[pos_primeiro] = Variavel.X7
            else:
                l[pos_primeiro] = Variavel.X8

        elif (element == NaoTerminal.CONST):
            l[pos_primeiro] = ci

        elif (element ==NaoTerminal.BIN_OP):
            op = ci % 5

            if (op == 0):
                l[pos_primeiro] = BinOperations.ADD
            elif (op == 1):
                l[pos_primeiro] = BinOperations.DIV
            elif (op == 2):
                l[pos_primeiro] = BinOperations.MUT
            elif (op == 3):
                l[pos_primeiro] = BinOperations.POW
            else:
                l[pos_primeiro] = BinOperations.SUB

        else:
            op = ci % 6

            if (op == 0):
                l[pos_primeiro] = UniOperations.ABS
            elif (op == 1):
                l[pos_primeiro] = UniOperations.COS
            elif (op == 2):
                l[pos_primeiro] = UniOperations.EXP
            elif (op == 3):
                l[pos_primeiro] = UniOperations.LOG
            elif (op == 4):
                l[pos_primeiro] = UniOperations.SIN
            else:
                l[pos_primeiro] = UniOperations.SQRT

        cont = cont + 1
        if (cont == len(cromossomo)):
            cont = cont % len(cromossomo)
            numVoltas = numVoltas + 1

    if (numVoltas == configs["NUM_VOLTAS_CROMOSSOMO"]):
        l.clear()
        l.append(sys.maxsize)

    return l

def derivacao (cromossomo):
    """
        Apartir de um cromossomo, gera uma produção segundo 
        a gramática especificada em SymbolsEnum e em seguida
        converte para uma string que pode ser executada pelo
        python com eval.

        Recebe: cromossomo => lista de inteiros entre 0 e 255 inclusive.

        Retorna: expressao_final => string a ser executada com eval.
    """
    lista = gera_producoes(cromossomo)

    expressao_final = ""
    for elem in lista:
        expressao_final = expressao_final + str(elem)

    return expressao_final
