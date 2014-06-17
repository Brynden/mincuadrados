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
    Fecha ultima modificacion: 16/06/2014
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
#en la posición matriz[j[i], es decir invertimos las filas y columnas.

def transp(matriz):
	tmatriz=zeros((matriz.shape[1],matriz.shape[0]))
	for i in range(matriz.shape[0]):
		for j in range(matriz.shape[1]):
			tmatriz[j][i] = matriz[i][j]
	return tmatriz


                                                    
#Determinante de una matriz, dada una matriz de 2x2 [[a b],[c d]], realiza el producto de la diagonal principal
#menos la diagonal secundaria, es decir: [(a*d)-(b*c)].
#Para matrices mayores aplicamos teorema de Laplace, utilizando la primera fila calculamos la suma de cada elemento
#multiplicado por el determinante(de forma recursiva) de su matriz menor complementaria, o submatriz, con el 
#correspondiente signo (-1)^(i+j), en este caso i siempre es 0 ya que usamos la primera fila y como nuestros arreglos 
#estan basados en index 0calculamos de la forma (-1)^(j+2).
    
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



#Cofactores, esta función nos permite obtener la matriz de cofactores(cmatriz), substituyendo en cada termino de
#"matriz[i][j]", por el termino cofactor cmatriz[i][j], que corresponde al determinante de la submatriz con signo
#correspondiente a la posicion en que se encuentre.

def cofactores(matriz):
    cmatriz=zeros_like(matriz)
    fil,col =matriz.shape
    for i in range(fil):
        for j in range(col):
            cmatriz[i][j]+=((-1)**(i+j+2))*(det(subm(matriz,i,j)))
    return cmatriz


                                                                                                                                         
#Para obtener la matriz inversa, si está es de dimension 2x2 se aplica la formula: (1/det)*[[d -b],[-c a]],
#si las dimensiones de la matriz son mayores a 2x2, se realiza el producto entre:
# (1/(det(matriz))*adjunta(matriz), donde la adjunta corresponde a la transpuesta de la matriz cofactores
#Nota: en el ingreso de datos del progama principal comprobamos que la matriz (A.t*A) que necesita ser invertida tiene
#efectivamente matriz inversa pero de todos modos hemos incluido aqui los condicionantes necesarios.
                                                                                                              
def inversa(matriz):
    fil,col=matriz.shape
    if det(matriz)==0 and fil!=col:
        return ("No tiene inversa")
    elif (fil,col)==(2,2):
        return (1/det(matriz))*array([[matriz[1][1],-matriz[1][0]],[-matriz[0][1],matriz[0][0]]])
    else:
        return (1/det(matriz))*(transp(cofactores(matriz)))



#Función Submatriz, devuelve la matriz resultante de eliminar una fila "i" y columna "j"
     
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



#Teniendo todas las funciones necesarias podemos resolver la ecuación de mínimos cuadrados
# X≈ [(A.t * A)^(-1)] * A.t * B
#Cabe destacar que está ecuación puede resolverse sólo si existe la inversa de "A.t*A"
#En el programa principal determinamos que esta condición se cumple al momento de ingresar los datos
#de todas formas hemos incluido la condición en está version para que la función funcione por si sola.
#usamos matrix_rank del modulo álgebra lineal de numpy para obtener el rango, y shape[1] las columnas.

def mincuad(a,b):
    if matrizA.shape[1]==linalg.matrix_rank(matrizA):
        ata=mult((transp(a)),a)
        atb=mult((transp(a)),b)
        ata2=inversa(ata)
        return(mult(ata2,atb))
    else:
        return("El rango de la matriz A es distinto al número de columnas. \nNo tiene solución única por minimos cuadrados")



#Dado un conjunto de puntos de la forma [(a,b)...(an,bn)]
#Primero obtenemos las coordenadas (x,y) por separado en x1, y1 respectivamente,
#formamos la matriz A de la forma [x 1]*n filas en A1, calculamos los mínimos cuadrados entra la
#matriz construida A1 y la matriz de coordenadas "y", la matriz solución que obtenemos correspondiente
#a los valores de la pendiente y coeficiente de posición, estos valores los podemos evaluar en la ecuación
#de la recta usando las coordenadas x originales, obteniendo las coordenadas "y" correspondientes a la recta
#aproximada, teniendo esto podemos obtener la suma de los cuadrados de los residuos d1=sum((recta-y1)**2)
#De forma similar operamos para encontrar la ecuación cuadrática y cúbica que más se aproxima, construyendo matrices
#de la forma  [x^2 x 1]*n filas y [x^3 x^2 x 1]*n filas respectivamente.

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
        return(X1)
    elif grf==2:    
        x2=x1**2
        A2=array([[x2[j], x1[j], 1] for j in range(n)])
        X2=mincuad(A2,y)
        cuad=X2[0]*x1**2+X2[1]*x1+X2[2]
        d2=sum((cuad-y1)**2)
        return(X2)
    else:
        x3=x1**3
        A3=array([[x3[j], x2[j], x1[j], 1] for j in range(n)])
        X3=mincuad(A3,y)
        cub=X3[0]*x1**3+X3[1]*x1**2+X3[2]*x1+X3[3]
        d3=sum((cub-y1)**2)
        return(X3)


#Nota: para poder encontrar una ecuación de grado m necesitamos m+1 puntos, esta condición está determinada
#en el ingreso de datos del programa principal donde la variable grf determina las ecuaciones que se pueden
#y desean calcular.

