import numpy as np

# Membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.2,2.4,3,4,5])

# Membuat vector dengan range
c = np.arange(1,20,4)

# Membuat linspace
d = np.linspace(1,5,10)

# Membuat matrix
e = np.array([ [1,2,3], [4,5,6] ])

# Membuat matrix dengan nilai 0
f = np.zeros((5,2))

# Matrix dengan nilai 1
g = np.ones((4,5))

# Matrix identitas
h1 = np.identity(6)
h2 = np.eye(10)

# Display
print(h2)