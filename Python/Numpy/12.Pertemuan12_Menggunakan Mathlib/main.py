import numpy as np
import matplotlib.pyplot as plt

# Persamaan garis: y = 2x + 3
x = np.arange(0, 11, 1)  # Membuat array x dari 0 hingga 10 dengan langkah 1
y = 2 * x + 3  # Menghitung nilai y sesuai persamaan garis

# Menampilkan nilai x dan y
print("Nilai x:", x)
print("Nilai y:", y)

# Membuat plot garis
plt.figure(1)
plt.plot(x, y)
plt.title("Grafik Persamaan Garis: y = 2x + 3")
plt.xlabel("Nilai x")
plt.ylabel("Nilai y")
plt.grid(True)
plt.show()

# Lingkaran dengan jari-jari 5
jari2 = 5
sudut = np.linspace(0, 2*np.pi, 100)  # Membuat array sudut dari 0 hingga 2π dengan 100 titik
x2 = jari2 * np.cos(sudut)  # Menghitung nilai x untuk lingkaran
y2 = jari2 * np.sin(sudut)  # Menghitung nilai y untuk lingkaran

# Membuat plot lingkaran
plt.figure(2)
plt.plot(x2, y2)
plt.title("Grafik Lingkaran dengan Jari-Jari 5")
plt.xlabel("Nilai x")
plt.ylabel("Nilai y")
plt.grid(True)
plt.axis('equal')  # Mengatur skala sumbu x dan y agar sama
plt.show()
