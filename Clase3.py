# Clase3.py
#####################################################
#####################################################
############### Ejercicio en Sesión #1 ##############
#####################################################
import numpy as np #libreria para manejar algebra lineal y matrices

def f(x):
    y=np.exp(-0.5*np.sinh(x)) + x - 3.2 
    return y

a=2.0 #limite inferior
b=4.0 #limite superior
contador=0 #contador de iteraciones

Tolerancia=0.000001 #tolerancia
xNuevo=0.0
error=0.0

print("%d \t %f \t %f \t %f \t %f" %(contador, a, b, xNuevo, error))
while abs(a-b)>= Tolerancia:
    xNuevo = (a+b)/2.0
    if f(xNuevo) * f(a)> 0.0:
        a = xNuevo
    else:
        b = xNuevo 
    contador= contador + 1
    error=abs(a-b)
    print("%d \t %f \t %f \t %f \t %f" %(contador, a, b, xNuevo, error))

print("La raiz de f es", xNuevo, "el valor real es ", 3.1977779078)

# Clase3.py
#####################################################
#####################################################
############### Ejercicio en Sesión #2 ##############
#####################################################
import numpy as np
import matplotlib.pyplot as plt


def PILeibniz(n):
    suma = 0.0
    for i in range(n):
        suma += ((-1) ** i) / (2 * i + 1)
    return 4.0 * suma

def PIWallis(n):
    prod=1.0
    for i in range(1, n+1):
        prod= prod*((2.0*i)/(2.0*i-1.0)) * ((2.0*i)/(2.0*i+1.0))
    return 2.0 * prod

listaN= np.linspace(1, 1000, 1000, dtype=(int))  # genera una lista de números enteros de 1 a 1000
listaWallis= []
listaLeibniz= []  # inicializa una lista vacía para almacenar los valores de pi calculados con Wallis

for i in listaN:
    listaWallis.append(PIWallis(i))  # calcula el valor de pi usando la función PIWallis para cada n en listaN
    listaLeibniz.append(PILeibniz(i))  # calcula el valor de pi usando la función PILeibniz para cada n en listaN
plt.plot(listaN, listaLeibniz,"o-", label='Aproximación de pi (Leibniz)', color='red')  # grafica la aproximación de pi
plt.plot(listaN, listaWallis, "o-", label='Aproximación de pi (Wallis)', color='blue')  # grafica la aproximación de pi
plt.legend()  # muestra la leyenda de la gráfica
plt.xlabel('Número de términos') # etiqueta del eje x
plt.ylabel('Valor de pi')  # etiqueta del eje y
plt.grid(ls="dashed")  # muestra la cuadrícula en la gráfica
plt.show()  # muestra la gráfica



#####################################################
#####################################################
############### Ejercicio de nuestra parte ##############
#####################################################
#Usa la serie de Taylor para aproximar el número e sumando distintos números de términos, y grafica cómo mejora la precisión al aumentar N.

import numpy as np
import matplotlib.pyplot as plt
import math

# Función para aproximar e usando la serie de Taylor
def aproximar_e(N):
    suma = 0
    for n in range(N + 1):
        suma += 1 / math.factorial(n)
    return suma

# Lista de valores de N (número de términos)
valoresN = list(range(1, 51))
aproximaciones = []

# Calculamos la aproximación para cada N
for n in valoresN:
    aproximaciones.append(aproximar_e(n))

# Graficamos la aproximación
plt.plot(valoresN, aproximaciones, label='Aproximación de e', color='green')
plt.axhline(y=np.e, color='gray', linestyle='--', label='Valor real de e')
plt.xlabel('Número de términos (N)')
plt.ylabel('Valor aproximado de e')
plt.title('Aproximación del número e usando la serie de Taylor')
plt.grid(ls='dashed')
plt.legend()
plt.show()

