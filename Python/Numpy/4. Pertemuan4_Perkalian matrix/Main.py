import numpy as np

a = np.array(([1,2],[3,4]))
b = np.ones([2,2])


print("matriks a:")
print(a)

print("matriks b:")
print(b)

# Perkalian matrix
c1 = np.dot(a,b)
c2 = a.dot(b)
print("")

print("Hasil c1:")
print(c1)
print("")
print("Hasil c2:")
print(c2)

