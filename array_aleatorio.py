import numpy as np

# Crear un array de 100 elementos con números aleatorios entre 0 y 1
array_aleatorio = np.random.rand(100)

# Calcular la media
media = np.mean(array_aleatorio)

# Calcular la desviación estándar
desviacion_estandar = np.std(array_aleatorio)

# Encontrar el valor máximo
maximo = np.max(array_aleatorio)

# Encontrar el valor mínimo
minimo = np.min(array_aleatorio)

# Imprimir los resultados
print("Array aleatorio:", array_aleatorio)
print(f"Media: {media}")
print(f"Desviación estándar: {desviacion_estandar}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
