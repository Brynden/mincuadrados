
from numpy import *
import matplotlib.pyplot as plt


def mult(matriz1,matriz2):
    if matriz1.shape[1] != matriz2.shape[0]:
        return ("Dimensiones incorrectas")
    else:
        nmatriz = zeros((matriz1.shape[0],matriz2.shape[1]))
        for i in range(matriz1.shape[0]):
            for j in range(matriz2.shape[1]):
                for k in range(matriz2.shape[0]):
                    nmatriz[i][j]+= matriz1[i][k]*matriz2[k][j]
        return nmatriz
		
def transp(matriz):
	tmatriz=zeros((matriz.shape[1],matriz.shape[0]))
	for i in range(matriz.shape[0]):
		for j in range(matriz.shape[1]):
			tmatriz[j][i] = matriz[i][j]
	return tmatriz

def mincuad(a,b):
    ata=mult((transp(a)),a)
    atb=mult((transp(a)),b)
    ata2=linalg.inv(ata)
    return(mult(ata2,atb))

def apxrecta(a):
    if dot.shape[1] != 2:
        return ("Formato incorrecto")
    else:
        b=hsplit(dot, 2)[1]
        x1=ones_like(b)
        x=hsplit(dot, 2)[0]
        a=column_stack((a[:,0],x1))
        r=mincuad(a,b)
        ec=r[0]*x+r[1]
        plt.plot(x,ec,"r-")
        plt.plot(x,b,"o")
        return(plt.show())
