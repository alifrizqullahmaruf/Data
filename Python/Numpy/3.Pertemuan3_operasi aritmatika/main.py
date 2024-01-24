import numpy as np

# List python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ELEMENTWISE

# penjumlahan
hasil = anp+bnp

# pengurangan
hasil =anp-bnp

# perkalian
hasil =anp*bnp

# pembagian
hasil =anp/bnp

# perpangkatan
hasil =anp**2

# multidimensi
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))
hasil = c+d
# hasil = c*d

print(hasil)
