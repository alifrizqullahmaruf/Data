import numpy as np

# Membuat matriks
a = np.array([(1, -1), (1, 1)])
print(a)

# Matriks invers
a_inv = np.linalg.inv(a)
print(a_inv)

# Determinan matriks
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print(det_a)
print(det_a_inv)
