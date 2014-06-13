
from numpy import *
import matplotlib.pyplot as plt
set_printoptions(precision=4)

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


def det(matriz):
    fil=matriz.shape[0]
    col=matriz.shape[1]
    d=0
    if fil==2 and col==2:
        return (matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0])
    else:
        for j in range(fil):
            d+=matriz[0][j]*(((-1)**(j+2))*(det(subm(matriz,0,j))))
    return d


def cofactores(matriz):
    cmatriz=zeros_like(matriz)
    fil,col =matriz.shape
    for i in range(fil):
        for j in range(col):
            cmatriz[i][j]+=((-1)**(i+j+2))*(det(subm(matriz,i,j)))
    return cmatriz


def inversa(matriz):
    fil,col=matriz.shape
    if (fil,col)==(2,2):
        return (1/det(matriz))*array([[matriz[1][1],-matriz[1][0]],[-matriz[0][1],matriz[0][0]]])
    else:
        return (1/det(matriz))*(transp(cofactores(matriz)))

        
def subm(matriz,i,j):
    smatriz = zeros((matriz.shape[0]-1,matriz.shape[1]-1))
    ccol = cfil = 0
    for fil in range(matriz.shape[0]):
	    if not fil == i:
		    for col in range(matriz.shape[1]):
			    if not col == j:					
				    smatriz[cfil][ccol]=matriz[fil][col]
				    ccol+=1
		    ccol=0
		    cfil+=1
    return smatriz


def mincuad(a,b):
    ata=mult((transp(a)),a)
    atb=mult((transp(a)),b)
    ata2=linalg.inv(ata)
    return(mult(ata2,atb))


def apxrecta(dot):
    if dot.shape[1] != 2:
        return ("Formato incorrecto")
    else:
        b=hsplit(dot, 2)[1]
        x1=ones_like(b)
        x=hsplit(dot, 2)[0]
        x2=arange(amin(x)-2,amax(x)+2)
        a=column_stack((dot[:,0],x1))
        r=mincuad(a,b)
        ec=r[0]*x2+r[1]
        plt.plot(x2,ec,"r-",label="Recta Aproximada")
        plt.plot(x,b,"o",label="Puntos ingresados")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(loc = 2)
        plt.title(("y = %s * x  + %s " % (str(r[0]),r[1])), style='italic')
        plt.suptitle("Aproximacion a la recta")
        print("y = %s * x  + %s " % (str(r[0]),r[1]))
        return(plt.show())
