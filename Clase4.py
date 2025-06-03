#### Ejercicio Sesion 4###
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y,color="red",label="$sin(x)$")
plt.title("Funciones Trigonométricas")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid(ls="dashed")
plt.legend()
plt.show()

### Ejercicio Propio ###
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.sin(x) - np.cos(x)
x = np.linspace(0, 2*np.pi, 100)
y = f(x)

plt.plot(x, y, color="blue", label="$sin(x) - cos(x)$")
plt.title("Gráfica de la función $sin(x) - cos(x)$")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.grid(ls="dashed")
plt.legend()
plt.show()