import numpy as np

# Membuat matriks a
a = np.array((
    [1, 2, 3],
    [4, 5, 6]
))

# Menampilkan ukuran matriks a dan isi matriks
# print('matrix a dengan ukuran:', a.shape)
# print(a)

# Transpose matriks a
# print('transpose matrix dari a:')
# print(np.transpose(a))  # atau a.T

# Menampilkan kembali ukuran matriks a setelah transpose
# print('matrix a dengan ukuran:', a.shape)

# # Flatten array, mengubah matriks menjadi vektor baris
# print('flatten matrix a:')
# print(np.ravel(a))  # atau 

# # Menampilkan kembali ukuran matriks a setelah flatten
# print('matrix a dengan ukuran:', a.shape)

# # Reshape matriks a
# print("reshape matrix a:")
# print(a.reshape(3, 2))

# # Menampilkan kembali ukuran matriks a setelah reshape
# print('matrix a dengan ukuran:', a.shape)

# # Resize matriks a
print("resize matrix a:")
a.resize(3, 2)
print(a)

# # Menampilkan kembali ukuran matriks a setelah resize
# print('matrix a dengan ukuran:', a.shape)
