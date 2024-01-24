import numpy as np

# Membuat array 2x2 dengan bilangan acak standar normal, dikali 10, dan dibulatkan ke bawah
a = np.floor(np.random.randn(2, 2) * 10)

# Menampilkan array a
print(a)

# Menampilkan nilai maksimum dari array a
print('nilai max dari a = ', a.max())

# Menampilkan posisi nilai maksimum dari array a
print('posisi max dari a = ', a.argmax())

# Menampilkan nilai minimum dari array a
print('nilai min dari a = ', a.min())

# Menampilkan posisi nilai minimum dari array a
print('posisi min dari a = ', a.argmin())

# Menampilkan array a setelah diurutkan
print('mengurutkan nilai a:')
print(np.sort(a))

# Menampilkan indeks yang mengurutkan array a
print(np.argsort(a))
