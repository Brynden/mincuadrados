#Trabajo de algebra 2: Aporximacion de minimos Cuadrados
#Integrantes:Felix Perez.  Hernán Puelles
#Lenguaje: Python 3.4.0
#Sistema Operativo Windows 

from numpy import *                                    #En este trabajo utilizaremos las librerias numpy y matplotlib para el lenguaje python. Con numpy podremos
import matplotlib.pyplot as plt                        #utilizar herramientas matematicas, en especial las orientadas a matrices (arreglos), y con matplotlib mostraremos
set_printoptions(precision=6)                          #la graficas de las rectas que se vayan generando al ingresar los puntos el usuario. 

def mult(matriz1,matriz2):                             # Función encargada de realizar la multiplicaión de matrices, Recibe las dos matrices correspondientes al sistema 
    if matriz1.shape[1] != matriz2.shape[0]:           # de ecuaciones, luego verifica si es posible realizar  la operación de multiplicaion, y de serlo, la funcion retorna
        return ("Dimensiones incorrectas")             #el resultado al programa principal.
    else:
        nmatriz = zeros((matriz1.shape[0],matriz2.shape[1]))
        for i in range(matriz1.shape[0]):
            for j in range(matriz2.shape[1]):
                for k in range(matriz2.shape[0]):
                    nmatriz[i][j]+= matriz1[i][k]*matriz2[k][j]
        return nmatriz

		
def transp(matriz):                                      #La funion recibe una matriz, y devuelve la matriz con su filas interambiadas por columnas,finalmente
	tmatriz=zeros((matriz.shape[1],matriz.shape[0])) # retorna la nueva matriz al programa principal.
	for i in range(matriz.shape[0]):
		for j in range(matriz.shape[1]):
			tmatriz[j][i] = matriz[i][j]
	return tmatriz


def det(matriz):                                         #Esta funcion recibe una matriz y obtiene el determinante preguntando primero si filas y columnas son de iguales
    fil=matriz.shape[0]                                  #a 2,de serlo se realiza la multiplicaion (sarrus para matrices 2x2), si la matriz es de una dimension mayor
    col=matriz.shape[1]                                  #se llamara a la funcion subm, para crear submatrices y realizar el metodo de LAPLACE.
    d=0
    if fil==2 and col==2:
        return (matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0])
    else:
        for j in range(fil):
            d+=matriz[0][j]*(((-1)**(j+2))*(det(subm(matriz,0,j))))
    return d


def cofactores(matriz):                                 #Esta funcion recibe una matriz con el fin de realizar el metodo de los cofactores, el cual necesitaremos 
    cmatriz=zeros_like(matriz)                          #para realizar la matriz inversa, por lo tanto esta funcion sera llamada a travez de la funcion "inversa"
    fil,col =matriz.shape
    for i in range(fil):
        for j in range(col):
            cmatriz[i][j]+=((-1)**(i+j+2))*(det(subm(matriz,i,j)))
    return cmatriz


def inversa(matriz):                                    #Esta función calcula la inversa de una matriz preguntando la dimension de la matriz, si el numero de
    fil,col=matriz.shape                                #de filas y columnas es igual a 2 y su determinante es igual a 0 se devuelve un cero, si el determinante no es cero
    if (fil,col)==(2,2):                                #se aplica la formula de matrices de 2x2 :1/det(a  -d )
        if det(matriz)==0:                                                                            #(-b  c)  
            return (0)
        else:
            return (1/det(matriz))*array([[matriz[1][1],-matriz[1][0]],[-matriz[0][1],matriz[0][0]]])
    else:
        if det(matriz)==0:
            return(0)
        else:
            return (1/det(matriz))*(transp(cofactores(matriz))) #  si la matriz no es de 2x2 y su determinante no es cero se aplica la formula de "cofactores"
                                                                #   llamando a la funcion cofactores la cual retornara el resultado a la funcion "inversa" y esta a su vez                         
                                                                # retornara la matriz a la funcion principal     
def subm(matriz,i,j):                                           
    smatriz = zeros((matriz.shape[0]-1,matriz.shape[1]-1))      #la funcion subm obtiene submatrices, necesarias para desarrollar el metodo LAPLACE y el metodo de 
    ccol = cfil = 0                                             #cofactores, retornando una submatriz(smatriz) a las funciones nombradas.
    for fil in range(matriz.shape[0]):
	    if not fil == i:
		    for col in range(matriz.shape[1]):
			    if not col == j:					
				    smatriz[cfil][ccol]=matriz[fil][col]
				    ccol+=1
		    ccol=0
		    cfil+=1
    return smatriz


def mincuad(a,b):                                   #Esta función recibe dos matrices, luego se encarga entregarnos la proximacion de minimos cudrados,mediante la llamada
    ata=mult((transp(a)),a)                         #de diversar funciones  que calculan la multiplicacion, transpuesta e inversa de una matriz,a su vez en este proceso se realizan
    atb=mult((transp(a)),b)                         #una serie de comprobaciones a las matrices recibidas, para que finalmente podamos aplicar la formula de sistemas de ecuaciones.
    ata2=inversa(ata)
    return(mult(ata2,atb))

#grf=
#1recta
#2cuadratica
#3recta y cuadratica
#4calcular recta y cuadra
#5cubica
#6calcular todas
#7 graficar todas

def aprox(pts,grf):                                 #Esta funcion recibe los puntos que entregamos, grafica la recta, y segun sea el caso realiza la aproximacion 
                                                    #a la recta, funcion, cuadratica,funcion cubica, y realizar el mejor ajuste
    x1=pts[:,0]
    y1=pts[:,1]
    y=hsplit(pts, 2)[1]
    n=len(x1)
    plt.plot(x1,y,"ko",label="$Puntos$")
    plt.xlabel("X")
    plt.ylabel("Y")    
    plt.title("Aproximación polinomial de puntos metodo mínimos cuadrados")
    A1=array([[x1[j], 1] for j in range(n)])
    X1=mincuad(A1,y)
    xr=linspace(amin(x1)-2,amax(x1)+2,3)
    recta=X1[0]*x1+X1[1]
    recta2=X1[0]*xr+X1[1]
    d1=sum((recta-y1)**2)
    if grf>=2:
        x2=x1**2
        A2=array([[x2[j], x1[j], 1] for j in range(n)])
        X2=mincuad(A2,y)
        xcd=linspace(amin(x1)-2,amax(x1)+2,40)
        cuad=X2[0]*x1**2+X2[1]*x1+X2[2]
        cuad2=X2[0]*xcd**2+X2[1]*xcd+X2[2]
        d2=sum((cuad-y1)**2)    
    if grf>=5:
        x3=x1**3
        A3=array([[x3[j], x2[j], x1[j], 1] for j in range(n)])
        X3=mincuad(A3,y)
        xcb=linspace(amin(x1)-1,amax(x1)+1,60)
        cub=X3[0]*x1**3+X3[1]*x1**2+X3[2]*x1+X3[3]
        cub2=X3[0]*xcb**3+X3[1]*xcb**2+X3[2]*xcb+X3[3]
        d3=sum((cub-y1)**2)
    if grf==6 or grf==4:
        print("La funcion que minimiza la suma de los cuadrados de los residuos (scr) es: ")
        if grf==6 and d3<d2 and d3<d1:
            plt.plot(xcb,cub2,"g",label=r'$%.3f*x^3%+.3f*x^2%+.3f*x%+.3f" $'% (X3[0],X3[1],X3[2],X3[3]))
            print("La ecuacion cúbica: \n %.6f*x^3%+.6f*x^2%+.6f*x%+.6f" % (X3[0],X3[1],X3[2],X3[3]))
            print("scr para funcion cúbica= %f" % (d3))
        elif d1<=d2:
            plt.plot(xr,recta2,"b-",label=r'$y=%10.3f*x%+.3f" $'% (X1[0],X1[1]))
            print("La recta: \n %10.6f*x%+.6f" % (X1[0],X1[1]))
        elif d2<d1:            
            plt.plot(xcd,cuad2,"r",label=r'$%.3f*x^2%+.3f*x%+.3f" $'% (X2[0],X2[1],X2[2]))
            print("La curva que mejor se aproxima es la ecuacion cuadrática\n %.6f*x^2%+.6f*x%+.6f" % (X2[0],X2[1],X2[2]))
        print("scr para funcion cuadrática= %f \nscr para la recta= %f" % (d2,d1))
    elif grf==7 or grf==3:
        if grf==7:
            plt.plot(xcb,cub2,"g",label=r'$%.3f*x^3%+.3f*x^2%+.3f*x%+.3f" $'% (X3[0],X3[1],X3[2],X3[3]))
            print("La ecuacion cúbica es: \n %.6f*x^3%+.6f*x^2%+.6f*x%+.6f" % (X3[0],X3[1],X3[2],X3[3]))
        plt.plot(xcd,cuad2,"r",label=r'$%.3f*x^2%+.3f*x%+.3f" $'% (X2[0],X2[1],X2[2]))
        print("La ecuacion cuadrática es: \n %.6f*x^2%+.6f*x%+.6f" % (X2[0],X2[1],X2[2]))
        plt.plot(xr,recta2,"b-",label=r'$%10.3f*x%+.3f" $'% (X1[0],X1[1]))
        print("La recta es: \n %.6f*x%+.6f" % (X1[0],X1[1]))
    elif grf==1:
        plt.plot(xr,recta2,"b-",label=r'$%10.3f*x%+.3f" $'% (X1[0],X1[1]))
        print("La recta es: \n %.6f*x%+.6f" % (X1[0],X1[1]))
    elif grf==2:
        plt.plot(xcd,cuad2,"r",label=r'$%.3f*x^2%+.3f*x%+.3f" $'% (X2[0],X2[1],X2[2]))
        print("La ecuacion cuadrática es: \n %.6f*x^2%+.6f*x%+.6f" % (X2[0],X2[1],X2[2]))
    else:
        plt.plot(xcb,cub2,"g",label=r'$%.3f*x^3%+.3f*x^2%+.3f*x%+.3f" $'% (X3[0],X3[1],X3[2],X3[3]))
        print("La ecuacion cúbica es: \n %.6f*x^3%+.6f*x^2%+.6f*x%+.6f" % (X3[0],X3[1],X3[2],X3[3]))
              
    plt.legend(loc = 4)            
    plt.show()
    
def ingreso (matrizA,matrizB):                          #Una de las primeras funciones en ser llamada, se encarga de ingresar los datos a la matriz, tambien
    print("Ingrese dimensiones de la matriz(max 5x5)")  #realiza una comprobacion si los datos no son correctos(enteros) , si hemos ingresado correctamente los datos
    while True:                                         #se retornara al programa principal la matriz.
        try:
            filas = int(input('Filas:'))
            columnas = int(input('Columnas:'))
        except ValueError:
            print("Intentelo nuevamente")
        else:
            if filas < 2 or filas > 5 or columnas < 2 or columnas > 5:
                print("Intentelo nuevamente")
            else:
                break
        
    matrizA = empty((filas,columnas))                   #con esta asignacion generamos una matriz vacia,"empty",idealmente para matrices cuyas dimensiones son desconocidas
    matrizB = empty((filas))
    
    print ("Ingrese valores de la matriz A: ")
    for i in range(filas):
        for j in range(columnas):
            while True:
                try:
                    valor=float(input("Elemento %d,%d : " % (i+1,j+1) ))
                except ValueError:
                    print("Intentelo nuevamente")
                else:
                    matrizA[i][j]=valor
                    break

    print("Ingrese valores matriz de soluciones: ")
    for i in range(filas):
        while True:
            try:
                valor=float(input("Elemento %d : " % (i+1) ))
            except ValueError:
                print("Intentelo nuevamente")
            else:
                matrizB[i]=valor
                break
    matrizB=matrizB.reshape(filas,1)
    print ("A=")
    print (matrizA)
    print ("B=",)
    print (matrizB)
    return matrizA,matrizB

def ingpto(puntos):                                 #Funcion encargada de ingresar los puntos para la aproximacion, de igual manera que en la funcion"ingreso"
    print("Cuantos puntos desea ingresar: "),       #se comrprueba que los datos sean correctos(float),tambien como minimo se piden dos puntos
    while True:                                     #ya que sino, no se podria realizar la grafica,ni mucho menos la recta. 
        try:
            npts=int(input())
        except ValueError:
            print("Intentelo nuevamente")
        else:
            if npts>20:
                print("Son demasiados puntos por favor sea más considerado")
            elif npts<2:
                print("Se necesitan al menos 2 puntos!")
            else:
                break
    puntos=empty((npts,2))                        #definimos la variable puntos, y le asignamos "empty", similar a lo realizado con las matrices antes de ser
    while True:                                   #ingresados los datos.
        for i in range(npts):
                while True:
                    try:
                        valorx=float(input("Coordenada X N° %d : " % (i+1)))
                        valory=float(input("Coordenada Y N° %d : " % (i+1)))
                    except ValueError:
                        print("Intentelo nuevamente")       
                    else:
                        puntos[i][0]=valorx
                        puntos[i][1]=valory
                        break
        if len(unique(puntos[:,0]))<2:
            print("Se necesitan al menos 2 coordenadas X distintas!")    #otra condicion importante para poder generar una grafica a partir de puntos.       
        else:
            break
    print(puntos)
    return(puntos,len(unique(puntos[:,0])))

    
print("Aproximación de Minimos cuadrados \n 1)Sistemas de ecuaciones \n 2)Aproximacion a partir de puntos")

while True:                             #Menu Principa: desde aqui podemos elegir el tipo de aproximación, y luego el programa llamara a las
    try:                                #a las funciones necesarias para relizar el proceso de aproximacion elegido.
        elije=int(input())
    except ValueError:
        print("Intentelo nuevamente")
    else:
        if elije!=1 and elije!=2 and elije !=3:
            print("Ingrese una opción válida")
        elif elije==1:                   #esta funcion nos presentara un menu, el cual se ejecutara hasta que el usuario lo necesite,
            matrizA=matrizB=array        #se definen las matrices a ser ingresadas eventualmente.
            matrizA,matrizB=ingreso(matrizA,matrizB) #se envian las matrices a la funcion que ingresara los datos a cada una(por el usuario).
            if matrizA.shape[1]==linalg.matrix_rank(matrizA):   #(se realiza la comprobacion entre el rango de la matriz A y su N° dec olumnas)
                print ("Soluciones por minimos cuadrados: ")
                print (mincuad(matrizA,matrizB))      #se imprime en pantalla la aproximacion de los minimos cuadrados, llamando a su vez a las funciones 
            else:                                     #que sea necesario ocupar.
                print("El rango de la matriz A es distinto al número de columnas. \nNo tiene solución única por minimos cuadrados")


        elif elije==2:
            puntos=array  #definimos la variable "puntos" a utilizar para el ingreso de puntos.
            puntos,cx=ingpto(puntos) 
            grf=0
            sw1=0
            if cx==2:
                grf=1
                aprox(puntos,grf)   #es llamada la funcion que aproxima los puntos, enviando la variable "puntos y grf"
            elif cx==3:       
                while sw1==0:
                    print("Aproximar los puntos a: \n 1)Recta \n 2)Función Cuadrática \n 3)Ambas \n 4)Calcular la que mejor aproxime \n 5)Salir")
                    try:
                        grf=int(input())   # segun sea la cantidad de puntos que ingresamos, se nos desplegaran varias opciones de aproximacion de rectas
                    except ValueError:
                                print("Intentelo nuevamente")     # se verificara que la opcion este dentro de las posibilidades.
                    else:
                        if grf!=1 and grf!=2 and grf!=3 and grf!=4 and grf!=5:
                            print("Ingrese una opción válida")
                        elif grf!=5:
                            aprox(puntos,grf)
                        else:
                            sw1=1
            else:
                while sw1==0:
                    print("Aproximar los puntos a: \n 1)Recta \n 2)Función Cuadrática \n 3)Función Cubica \n 4)Calcular la que mejor aproxime \n 5)Todas \n 6)Salir")
                    try:
                        grf=int(input())
                    except ValueError:
                                print("Intentelo nuevamente")
                    else:
                        if grf!=1 and grf!=2 and grf!=3 and grf!=4 and grf!=5 and grf!=6:
                            print("Ingrese una opción válida")
                        elif grf!=6:    
                            if grf==5:
                                grf=7
                            if grf==4:
                                grf=6
                            if grf==3:
                                grf=5
                            aprox(puntos,grf)
                        else:
                            sw1=1
        else:
            break
    input()
    print("\n\n 1)Sistemas de ecuaciones \n 2)Aproximacion a partir de puntos \n 3)Salir")


            
