#####################################################
#####################################################
############### Ejercicio en Sesión ##############
#####################################################
from random import *

b= [0,4,8,9,7,5,8, [1,2,3,4,5,6,7,8,9]]
print(b)

for i in range(len(b)):
            print(b[i]) 

for i in ["Hola", 3, [4,8,9], 3+-1j, "mundo"]:
    print(i)

i=0
while i<10:
    print(i)
    i+=1

while i<5:
    i=int(10*random())
    print("i= ",i)

#####################################################
#####################################################
############### Ejercicio de nuestra parte ##############
#####################################################
# Cree una lista con varios valores (enteros y otra lista dentro).
# Imprima todos los elementos uno por uno.
# Recorra otra lista con distintos tipos de datos y los imprima.
# Use un bucle while para contar del 0 al 9.
# Genere valores aleatorios entre 0 y 9 hasta que se obtenga un número menor a 5.
#####################################################
#####################################################
from random import *

# Paso 1: Crear lista
b = [0, 4, 8, 9, 7, 5, 8, [1, 2, 3]]
print("Lista completa:", b)

# Paso 2: Imprimir elementos
print("\nElementos individuales de la lista:")
for i in range(len(b)):
    print(b[i])

# Paso 3: Recorrer lista con varios tipos de datos
print("\nLista con distintos tipos de datos:")
for i in ["Hola", 3, [4, 8, 9], 3 + -1j, "mundo"]:
    print(i)

# Paso 4: Contar del 0 al 9
print("\nContador con while:")
i = 0
while i < 10:
    print(i)
    i += 1

# Paso 5: Valores aleatorios hasta que salga uno menor que 5
print("\nGenerando números aleatorios hasta obtener uno menor a 5:")
i = 10  # Para que entre al while
while i >= 5:
    i = int(10 * random())
    print("i =", i)