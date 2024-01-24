import numpy as np

# Mendefinisikan data type (dtipe) dengan format nama ('S10' untuk string maksimal 10 karakter) dan tinggi (int)
dtipe = [('nama', 'S10'), ('tinggi', int)]

# Membuat array a dengan menggunakan data dan data type yang telah ditentukan
data = [
    ('Ucup', 170),
    ('Otong', 150),
    ('Mario', 160)
]
a = np.array(data, dtype=dtipe)

# Menampilkan array a
print(a)

print("")
# Menampilkan array a setelah diurutkan berdasarkan kolom 'tinggi'
print("Menampilkan array a setelah diurutkan berdasarkan kolom 'tinggi'")
print(np.sort(a, order='tinggi'))

# Menampilkan array a setelah diurutkan berdasarkan kolom 'nama'
print("Menampilkan array a setelah diurutkan berdasarkan kolom 'nama'")
print(np.sort(a, order='nama'))
