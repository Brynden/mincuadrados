'''
    Programa que calcula los mínimos cuadrados de sistemas de ecuaciones
    y la aproximación de puntos a funciones lineales, cuadráticas y cúbicas.

    Archivo: MinCuad_func.py

    **Para sistemas de ecuaciones:
    Dada una matriz de coeficientes "A" de orden (nxm) y una matriz de soluciones "B"
    orden (nx1), el sistema A*X=B tiene solución única mediante mínimos cuadrados
    si y  sólo si el rango de la matriz A es igual a m, en otras palabras, el número
    de filas linealmente independientes de A es igual al número de columnas, en definitiva
    A es una matriz cuadrada y podemos entonces calcular su inversa. Por lo que la solución
    única mediante mínimos cuadrados es:
                X≈ [(A.t * A)^(-1)] * A.t * B
    Donde A.t es la matriz transpuesta de A, y ([]^(-1)) es la matriz inversa

    **Para puntos:
    Sea un conjunto de puntos (ai,bi) con i= [1,2....n]
    Si existen al menos m+1 puntos con coordenadas x distintas construimos matricez A de la forma:
        [1 a1 a1^2 a1^3 ... a1^m]
    A=  [...                 ...]
        [1 an an^2 an^3 ... an^m]

        [b1]
    B=  [..]
        [bn]
        
    Con lo cual resolvemos mediante mínimos cuadrados utilizando la formula previamente descrita.
    Si m=1 entonces obtenemos la ecuación de la recta
    Si m=2 una ecuación cuadrática
    Y si m=3 una ecuacíon cúbica


    
    --Para menu de usuario interactivo y opciones graficas por favor dirijase
    al archivo: "MinCuad.py"---
 
    Autores: Felix Perez <perez.felix15@hotmail.com>
             Hernan Puelles <darkfairth@gmail.com>
    Fecha inicio: 10/06/2014
    Fecha ultima modificacion: 15/06/2014
    Python Version: 3.4.1 x32
    Modulos: Numpy 1.8.1
             Matplotlib: 1.3.1
'''



from numpy import *


#Multiplicación de matrices, primero verifica que 2 matrices A(nxm) y B(pxq) sean multiplicables
#es decir m=p, luego crea una matriz de dimensiones (nxq) y va llenando cada posición [i][j] 
#con el resultado de la sumatoria de los productos entre cada elemento de las filas[i][..] de la matriz A
#y las columnas[..][j] de la matriz B

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



#Transpuesta de una matriz, dada una matriz de dimensiones(nxm)
#creamos una matriz transpuesta tmatriz de dimensiones(mxn)
#y llenamos cada una de las posiones de tmatriz[i][j] con el valor de matriz original
#en la posición matriz[j[i], es decir invertimos las filas y columnas

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
    if det(matriz)==0:
        return ("No tiene inversa")
    elif (fil,col)==(2,2):
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
    ata2=inversa(ata)
    return(mult(ata2,atb))

#grf=
#1recta
#2cuadratica
#3cubica

def aprox(pts,grf):
    
    x1=pts[:,0]
    y1=pts[:,1]
    y=hsplit(pts, 2)[1]
    n=len(x1)
    if grf==1:
        A1=array([[x1[j], 1] for j in range(n)])
        X1=mincuad(A1,y)
        recta=X1[0]*x1+X1[1]
        d1=sum((recta-y1)**2)
    elif grf==2:    
        x2=x1**2
        A2=array([[x2[j], x1[j], 1] for j in range(n)])
        X2=mincuad(A2,y)
        cuad=X2[0]*x1**2+X2[1]*x1+X2[2]
        d2=sum((cuad-y1)**2)
    else:
        x3=x1**3
        A3=array([[x3[j], x2[j], x1[j], 1] for j in range(n)])
        X3=mincuad(A3,y)
        cub=X3[0]*x1**3+X3[1]*x1**2+X3[2]*x1+X3[3]
        d3=sum((cub-y1)**2)


