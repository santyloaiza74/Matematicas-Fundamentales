#####################################################
#####################################################
############### Ejercicio en Sesión ##############
#####################################################

from math import *  # Importa todas las funciones y constantes del módulo math (incluyendo pi)
from random import *  # Importa todas las funciones del módulo random (incluyendo random())

print("Programa para calcular el valor de pi")  # Imprime el título del programa 
N=10000000 # Asigna 10 millones a N, que será el número total de puntos a generar
Pdentro=0 # Inicializa el contador de puntos que caen dentro del círculo
r=0.5 # Define el radio del círculo como 0.5 (el círculo estará centrado en (0.5, 0.5))

for i in range(N):  # Inicia un bucle que se ejecutará N veces (10 millones)
  x=random()  # Genera un número aleatorio entre 0 y 1 para la coordenada x
  y=random()  # Genera un número aleatorio entre 0 y 1 para la coordenada y
  if ((x-0.5)**2 + (y-0.5)**2)<=0.5**2:  # Comprueba si el punto (x,y) está dentro del círculo
   Pdentro=Pdentro+1  # Si está dentro, incrementa el contador Pdentro

PI=(Pdentro)/((r**2)*float(N))  # Calcula la aproximación de pi usando la relación de áreas
print("El valor de pi con el método de Montecarlo es: ", PI)  # Muestra el valor calculado
print("El error es de: ", abs(PI-pi))  # Muestra el error absoluto respecto al valor real de pi
print("El error porcentual es: ", abs((PI-pi)/PI)*100)  # Muestra el error porcentual


#####################################################
#####################################################
############### Ejercicio de nuestra parte ##############
#####################################################
# Usa un ciclo for para calcular una aproximación de π con la serie de Leibniz, sumando una cantidad determinada de términos.

suma = 0
iteraciones = 1000000

for n in range(iteraciones):
    termino = ((-1) ** n) / (2 * n + 1)
    suma += termino

pi_aproximado = 4 * suma
print(f"Aproximación de pi con {iteraciones} términos: {pi_aproximado}")
