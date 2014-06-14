from numpy import*

print("Ingrese dimensiones de la matriz(Filas x Columnas) entre 1 y 5")
while True:
        try:
            filas = int(input('Filas:'))
            columnas = int(input('Columnas:'))
        except ValueError:
            print("Intentelo nuevamente")
        else:
            if filas < 1 or filas > 5 or columnas < 1 or columnas > 5:
                print("Intentelo nuevamente")
            else:
                break
        
matriz = empty((filas,columnas))

for i in range(filas):
        for j in range(columnas):
                while True:
                        try:
                                valor=float(input("Elemento %d,%d : " % (i+1,j+1) ))
                        except ValueError:
                                print("Intentelo nuevamente")
                        else:
                                matriz[i][j]=valor
                                break
print (matriz)

