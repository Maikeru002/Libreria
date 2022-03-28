
import Libreria as lb
import numpy as np
from numpy.linalg import eig as e
 

def Transicion(ket1, ket2):
    transition = lb.Produc_Inter(lb.normalizar(ket2),lb.normalizar(ket1))
    return transition

def Matriz_inferencia(matriz_inf):
    """
    La funcion retorna la matriz de inferencia del sistema
    La entrada del sistema es la matriz que representa el sistema
    """
    result_inf = []
    for i in range(len(matriz_inf)):
        for j in range(len(matriz_inf)):
            cons = 0
            for h in range(len(matriz_inf[i])):
                if matriz_inf[i][h] * matriz_inf[h][i] + cons == cons:
                    if matriz_inf[i][j] != 0 or matriz_inf[j][i] != 0:
                        result_inf.append([i,j])
    return result_inf


def clicks(matriz, vector, tiempos):
    i = 0
    while i < tiempos:
        estado = lb.accion(matriz, vector)
        i += 1
    return vector
    
def Multiples_rendijas(matriz, vector, tiempos):
    """
    retorna el estado despues de varios clicks 
    """
    matriz_matriz = lb.Produc_Matrix(matriz, matriz)
    vector_estado = clicks(matriz_matriz, vector, tiempos)
    return vector_estado

def Probabilidades(matriz, probabilidaes):
    """ funcion que retorna las probababilidades de los estados
    """
    h = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 1:
                matriz[i][j] = probabilidaes[h]
                h += 1
    return matriz


def Matriz_Boleana(inicial, final):
    """Devuelte una matriz booleana 
    """
    matriz_01 = [(0, 0) for j in range(len(inicial))]
    matriz_02 = [matriz_01 for i in range(len(final))]
    for i in range(len(inicial)):
        for j in range(len(final)):
            if i == j:
                matriz_02[final[j]][inicial[i]] = [1,0]
    return matriz_02

#-------------------------------------------------------------------------------------------

#SECCION 4.3

def Cn_Not(notation):
    """ Funcion que cambia la notacion de los nuemros complejors"""
    for i in range(len(notation)):
        for j in range(len(notation[0])):
            notation[i][j] = complex(notation[i][j][0], notation[i][j][1])
    return notation

def Valores_Propios(sig):
    """Funcion que retorna los valores propios"""
    mat = np.array(Cn_Not(sig))
    ValorActual, FuturoVector = np.linalg.e(mat)
    ValorActual = str(ValorActual).replace("[", "").replace("]", "").split()
    return ValorActual

def Generate_value(sig):
    """Genera todas las medidas que podría llegar a registrar respecto al observable (valores propios)"""
    mat = np.array(Cn_Not(sig))
    ValorActual, FuturoVecto = np.linalg.e(mat)
    return FuturoVecto

def Probabilidad_Trans(phi, e):
    """ La funciuon retorna la Probabilidad de la transicion """
    return lb.Module(Transicion(e, phi))

def Estado_Final(matx, P, t):
    """Funcion que retorna el estado final """
    vector = P
    index = 1
    while index < t:
        fin = lb.ProductMatrix(matx,matx)
        final = fin
        index += 1
    return lb.accion(final, P)
    