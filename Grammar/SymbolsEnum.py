from enum import Enum

class MyEnum(Enum):
    def __str__(self):
        return str(self.value)

class NaoTerminal(MyEnum):
    EXPRESSION = 1
    VAR = 2
    CONST = 3
    BIN_OP = 4
    UNI_OP = 5

class Variavel(MyEnum):
    X1 = "X1"
    X2 = "X2"
    X3 = "X3"
    X4 = "X4"
    X5 = "X5"
    X6 = "X6"
    X7 = "X7"
    X8 = "X8"

class Parenteses(MyEnum):
    ABRE_PAR = "("
    FECHA_PAR  = ")"

class BinOperations(MyEnum):
    ADD = "+"
    SUB = "-"
    MUT = "*"
    DIV = "/"
    POW = "**"

class UniOperations(MyEnum):
    ABS = "abs"
    SIN = "sin"
    COS = "cos"
    EXP = "exp"
    LOG = "log"
    SQRT = "sqrt"
