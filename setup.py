from Grammar import derivacao

if __name__ == "__main__":
    from math import exp, sin, pi
    print(derivacao([1, 2, 3, 4, 5]))
    print(eval(derivacao([1, 2, 3, 4, 5])))
    
    print(derivacao([5, 4, 3, 3, 0]))
    print(eval(derivacao([5, 4, 3, 3, 0])))

    X4 = pi
    print(derivacao([5, 4, 2, 3, 0]))
    print(eval(derivacao([5, 4, 2, 3, 0])))
    
    print(derivacao([1, 1, 1, 1, 1]))
    print(eval(derivacao([1, 1, 1, 1, 1])))
