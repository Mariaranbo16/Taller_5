import numpy as np         # Forma estandar de impotar la biblioteca 
# Matplotlib tiene muchos módulos 
import matplotlib.pyplot as plt

# Dibujar una función seno
# Crear un ndarray de 1 dimensión, 100 elementos equiespaciados, desde 0 a 2*PI

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

# Usar matplotlib
# 1. Definir el tamaño de la función 
plt.figure(figsize=(8,4))

# Añade un titulo
plt.title ("Mi primer gráfico científico en programación")

# 2. Crear un grafico y los valores de las funicones en los ejes 
plt.plot (x,y)

# Muestra las etiquetas de los ejes 
plt.xlabel("x")
plt.ylabel("Seno de x")

#Muestra una grilla
plt.grid(True)

# 3. Mostrar el grafico
plt.show()