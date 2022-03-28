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
def MultEscalarMatriz(c, A):
    fila = [(0, 0)] * len(A[0])
    r = [fila] * len(A)
    for j in range(len(A)):
        fila = [(0, 0)] * len(A[0])
        r[j] = fila
        for k in range(len(A[0])):
            r[j][k] =ProduComplex(c, A[j][k])
    return r
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
    c = []
    for i in range(len(c1)):
        c.append([])
        for j in range(len(c2[0])):
            c[i].append((0,0))
            for k in range(len(c1[0])):
                c[i][j] = SumComplex(c[i][j],ProduComplex(c1[i][k],c2[k][j]))
    return c

#Accion de una matriz sobre un vector
def accion(w,v):
    return Produc_Matrix(w,v)

def Produc_Inter(V1,V2):
    return Produc_Matrix(Adj_Matrix(V1),V2)[0][0]

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


def ProductTensor(A,B):
    na = len(A)
    nb = len(B)
    nr = nb * na
    r = [(0,0)] * nr
    index = 0
    for j in range(na):
        for k in range(nb):
            r[index] = ProduComplex(A[j],B[k])
            index += 1
    return r

def TensorMatrices(A, B):
    m = len(A)
    n = len(B)
    size = (len(A)*len(B), len(A[0])*len(B[0]))
    result = [[(0, 0) for i in range(size[1])] for j in range(size[0])]
    for j in range(size[0]):
        for k in range(size[1]):
            result[j][k] = ProduComplex(A[j//n][k//m], B[j % n][k % m])
    return result


#Función que retorna el módulo al cuadrado de un Vector
def ModuloVector(vect):
    nv = len(vect)
    sqmodule = 0.0
    for j in range(nv):
        sqmodule += Module(vect[j][0])
    return sqmodule

#Función que retorna el módulo de un Vector
def ModuleVec(vect):
    return math.sqrt(ModuloVector(vect))

#Función que retorna el módulo al cuadrado de un valor complejo
def Module(c):
    return (c[0]**2) + (c[1]**2)

#Función que normaliza un vector
def normalizar(vect):
    escalar = 1/math.sqrt(ModuloVector(vect))
    return MultEscalarMatriz((escalar, 0), vect)

def identidad(mat):
    result = [[(0,0) for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j:
                result[i][j] = (1,0)
    return result
    