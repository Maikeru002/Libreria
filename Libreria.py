from cmath import sqrt
import math

def SumComplex(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def RestComplex(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def ProduComplex(c1, c2): # (c1[0],c1[1])  , (c2[0],c2[1])
    return c1[0]*c2[0]- c1[1]*c2[1] , c1[0]*c2[1]+ c1[1]*c2[0]

def DivisComplex(c1, c2): # (c1[0],c1[1])  , (c2[0],c2[1])
    Re = (c1[0]*c2[0] + c1[1]*c2[1])/ (c2[0]**2 + c2[1]**2)
    Im = (c1[1]*c1[1] - c1[0]*c2[1])/ (c2[0]**2 + c2[1]**2)
    return(Re, Im)

def ModComplex(c1):
    return sqrt(c1[0]**2 + c1[1]**2)

def ConjComplex(c1):
    return (c1[0],-1*c1[1])

def Car_PolComplex(c1):
    p = (sqrt(c1[0]**2 + c1[1]**2))
    theta = math.atan(c1[1]/c1[0])
    return (p, theta*(180/math.pi))

def Pol_CarComplex(c1):
    return c1[0]*round(math.cos(math.pi)), c1[0]*round(math.sin(math.pi))
    