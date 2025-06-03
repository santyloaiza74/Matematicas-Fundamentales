### Ejercicio Sesion 5 ###
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits import mplot3d

fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')

x=np.arange(-2,2,0.25)
y=np.arange(-2,2,0.25)

x,y=np.meshgrid(x,y)
z=np.sin(x**2)+0.5*np.cos(y**2)

surf=ax.plot_surface(x,y,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

# Ejercicio propio
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(-2, 2, 0.25)
y = np.arange(-2, 2, 0.25)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
surf = ax.plot_surface(x, y, z, cmap=cm.viridis, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()