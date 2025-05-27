import numpy as np

# Crear una matriz a partir de una lista de listas
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("A =\n", A)

# Crear una matriz de ceros
B = np.zeros((3, 3))
print("\nB =\n", B)

# Crear una matriz de unos
C = np.ones((3, 3))
print("\nC =\n", C)

# Crear una matriz con valores aleatorios
D = np.random.rand(3, 3)
print("\nD =\n", D)