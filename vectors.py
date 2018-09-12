import math

def vectors(x,y):
    Fa = (2/3) * x
    Fb = ((-1/3) * x) + (-1/math.sqrt(3))*y
    Fc = ((-1/3) * x) + (1/math.sqrt(3))*y

    return Fa, Fb, Fc;


