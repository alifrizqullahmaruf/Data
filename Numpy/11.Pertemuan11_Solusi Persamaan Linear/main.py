# Mengimport library numpy dengan alias np
import numpy as np

# Membuat matriks A
A = np.array([(2, 3), (1, 2)])

# Membuat vektor Y
Y = np.array([23, 14])

# Menampilkan matriks A dan vektor Y
print("Matrix A:")
print(A)
print("\nVector Y:")
print(Y)

# Menghitung invers dari matriks A
A_inv = np.linalg.inv(A)

# Menyelesaikan persamaan linear menggunakan metode invers
X1 = np.dot(A_inv, Y)

# Menampilkan hasil menggunakan metode invers
print("\nSolution using inverse method:")
print(X1)

# Menyelesaikan persamaan linear menggunakan fungsi solve dari numpy
X2 = np.linalg.solve(A, Y)

# Menampilkan hasil menggunakan fungsi solve
print("\nSolution using solve function:")
print(X2)
