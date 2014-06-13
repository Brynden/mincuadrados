from numpy import* 
matriz =array([[None,None],[None,None]])#solo serviria para 2x2

filas = int(input("Cantidad de Filas: "))
columnas = int(input("Cantidad de Columnas: "))
for i in range(filas):
        for j in range(columnas):
                matriz[i][j]=int(input("Elemento %d,%d : " % (i,j) ))
                  
print (matriz)

