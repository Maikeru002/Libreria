from cmath import sqrt
import math
from re import T

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

#------------------------------------------------------------------------------------------
#SECCION DE OPERACIONES CON MATRICES Y VECTORES
#  Adición de vectores complejos.

def addComplex(c1,c2):
    if len(c1) == len(c2):
        vec = [(0,0) for i in range(len(c1))]
        for i in range(len(c1) ):
            vec[i] = ((c1[i][0] + c2[i][0]),c1[i][1] + c2[i][1])
        return vec
    else:
        return "Los vectores tienen longitudes diferentes"


# Inverso (aditivo) de un vector complejo.
def invaddComplex(c1):
    vec = [(0,0) for i in range(len(c1))]
    for i in range(len(c1)):
        vec[i] = ((c1[i][0]*-1),c1[i][1]*-1)
    return vec
# Multiplicación de un escalar por un vector complejo.
def EscxVecComplex(x,c1):
    vec = [(0, 0) for i in range(len(c1))]
    for i in range(len(c1)):
        vec[i] = (x*c1[i][0],x*c1[i][1])
    return vec
#Adición de matrices complejas.

def SumMatrix(c1,c2):
    vec = [[] for i in range(len(c1))]
    for i in range(len(c1)):
        vec[i] = addComplex(c1[i],c2[i])
    return vec

#Inversa (aditiva) de una matriz compleja
def InvaddMatrix(c1):
    vec = [[] for i in range(len(c1))]
    for i in range(len(c1)):
        vec[i] = invaddComplex(c1[i])
    return vec

#Multiplicación de un escalar por una matriz compleja.
def EscMatrix(x,c1):
    vec = [[] for i in range(len(c1))]
    for i in range(len(c1)):
        vec[i] = EscxVecComplex(x,c1[i])
    return vec

# Transpuesta de una matriz/vector
def Trans_Matrix(c1):
    vec = [[(0,0) for h in range(len(c1[0]))] for i in range(len(c1))]
    for i in range(len(c1)):
        for j in range(len(c1)):
            vec[i][j] = c1[j][i]
    return vec

# Conjugada de una matriz/vector
def Conj_Matrix(c1):
    vec = [[(0,0) for h in range(len(c1[0]))] for i in range(len(c1))]
    for i in range(len(c1)):
        for j in range(len(c1)):
            vec[i][j] = ConjComplex(c1[i][j])
    return vec

# Adjunta (daga) de una matriz/vector
def Adj_Matrix(c1):
    return Conj_Matrix(Trans_Matrix(c1)) 

# Producto entre dos matrices 
def sum_arr(c1):
    a = (0,0)
    for i in range(len(c1)):
        a = SumComplex(a,c1[i])
    return a

# Producto entre matrices
def Produc_Matrix(c1,c2):
    fila = len(c1)
    columna = len(c2[0])
    matriz = [[(0,0) for h in range(columna)] for i in range(fila)]
    if fila == columna:
        for i in range(len(c1[0])):
            elemnt = []
            for j in range(len(c2)):
                elemnt += Produc_Matrix((c1[i][j]),(c2[i][j])) 
            matriz[i][j] = sum_arr(elemnt) 
    else:
        print("Las longitudes de las matrizes con diferentes")
    return matriz
#Accion de una matriz sobre un vector
def accion(w,v):
    return Produc_Matrix(w,v)

def Producto_vectores(c1,c2):
    vec = 0
    if len(c1) == len(c2):
        for i in range(len(c1)):
            vec += c1[i] * c2[i]
    return vec

# Norma de un vectro:
def Norma(c1):
    vec = 0
    for i in range(len(c1)):
        vec += c1[i]**2
    return sqrt(vec)

#Distancia entre vectores
def Dis_Vectores(c1,c2):
    vec = []
    for i in range(len(c1)):
        vec.append(c1[i] - c2[i])
    return sqrt(Producto_vectores(vec,vec))

#Hermitiana de una matriz
def hermitiana(c1):
    if Adj_Matrix(c1) == c1:
        return True
    return False


