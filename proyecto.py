import numpy as np
import time


n = int(input("Ingrese el nro de filas: ")) #Filas
m = int(input("Ingrese el nro de columnas: ")) #Columnas

matriz = np.zeros((n,m)) #Matriz de nxm
x = np.zeros(n)

vector = np.zeros((m))


for f in range(0,n):
    for c in range(0,m):
        matriz[(f),(c)] = float(input("Ingrese el elemento a[{}]: ".format(str(f+1) + str(c+1))))
    vector[(f)] = float(input("Ingrese el elemento b[{}] de la matriz B:  ".format(str(f+1))))

print("A =")
for i in matriz:
    print(i)

print("B =")
for i in vector:
    print("[{}]".format(i))

cant_iteraciones = int(input("Ingrese la cantidad de iteraciones que desea realizar(mayor a 10): "))

while cant_iteraciones < 10:
    print("No puede ingresar un nro menor que 10")
    cant_iteraciones = int(input("Ingrese la cantidad de iteraciones que desea realizar(mayor a 10): "))
print("-------> Calculando número de condición <------")
time.sleep(2)

#Condicionamiento
norma_matriz = np.linalg.norm(matriz, ord = np.inf)
matriz_inversa = np.linalg.inv(matriz)
norma_matriz_inversa = np.linalg.norm(matriz_inversa, ord = np.inf)
condicionamiento = norma_matriz*norma_matriz_inversa
print("Número de condición: ", condicionamiento)
if condicionamiento < 100:
    print("Se puede decir que la matriz está bien condicionada por que su valor es menor a 100")
else:
    print("La matriz no está bien condicionada por que el valor es mayor a 100")
print("-------> Calculando iteraciones <------")
time.sleep(5) 

#Cálculos del método Gauss Seidel
k = 0
precision = []
while k < cant_iteraciones:
    suma = 0
    k = k+1
    print("------Iteración nro: {}----- ".format(k))
    for f in range(0,n):
        suma = 0
        for c in range(0,m):
            if c != f:
                suma = suma + matriz[f,c]*x[c] 
        x[f] = (vector[f]-suma)/matriz[f,f]
        precision.append(x[f])
        print("x[{}]: ".format(str(f)) + str(x[f]))
    if k == cant_iteraciones:
        break

#Grado de precisión
valores_iteraciones = []
for i in range(0,len(precision),n): #Leo las posiciones desde 0 al largo de la lista que contiene las iteraciones, del nro de la cantidad de incognitas al nro de la cantidad de incognitas.
    num = precision[i:i+n] #Ingreso los valores de las iteraciones en las posiciones del for.
    valores_iteraciones.append(num)
j = []
for i in reversed(valores_iteraciones):
    j.append(i)
p = j[:2] #Almaceno las dos primeras listas que contienen los valores de las incógnitas de las 2 primeras iteraciones.
y = 0
lista_grado = []
for i in range(n):
    resta = abs(p[0][0+y] - p[1][0+y])
    y = y+1
    lista_grado.append(resta)
print("-------> Calculando el grado de precisión <------")
time.sleep(4)
print("Grado de precisión: ",max(lista_grado))

    