import numpy as np
import matplotlib.pyplot as plt

# Crear un array con los cuadrados de los números del 1 al 10
numeros = np.arange(1, 11)  # Crea un array de números del 1 al 10
cuadrados = numeros ** 2     # Calcula los cuadrados de esos números

# Crear un array de 100 elementos con números aleatorios entre 0 y 1
array_aleatorio = np.random.rand(100)

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Graficar los cuadrados en azul
plt.plot(numeros, cuadrados, 'bo-', label='Cuadrados de 1 a 10')

# Graficar los números aleatorios en rojo
plt.plot(range(1, 101), array_aleatorio, 'ro-', label='Números aleatorios')

# Añadir etiquetas y título
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Gráfica de cuadrados y números aleatorios')
plt.legend()

# Mostrar el gráfico
plt.grid()
plt.show()
