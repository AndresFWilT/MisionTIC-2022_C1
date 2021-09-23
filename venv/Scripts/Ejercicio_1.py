##Ley gravitacion Universal
import math

def leyGravedad(g, m1, m2, r):
    return g * ((m1 * m2) / math.pow(r, 2));

g = 6.67384E-11;
##F = fuerza gravitacional
F:float = leyGravedad(g,3.5,5.0,10.6);
print("Fuerza gravitacional: "+str(F));