from numpy import*

filas = int(input("Cantidad de Filas: "))
columnas = int(input("Cantidad de Columnas: "))
matriz = empty((filas,columnas))
for i in range(filas):
        for j in range(columnas):
                matriz[i][j]=int(input("Elemento %d,%d : " % (i,j) ))
                  
print (matriz)

