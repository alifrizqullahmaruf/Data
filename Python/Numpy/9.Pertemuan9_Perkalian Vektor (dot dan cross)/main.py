# Import the numpy library with the alias np
import numpy as np

# Create two 1-dimensional arrays, a1 and b1
a1 = np.array([1, 3])
b1 = np.array([3, 0])

# Perform dot product of a1 and b1
c1 = np.dot(a1, b1)

# Create two 1-dimensional arrays, a2 and b2, with three elements each
a2 = np.array([1, 2, 0])
b2 = np.array([2, 1, 0])

# Perform cross product of a2 and b2
c2 = np.cross(a2, b2)

# Perform cross product of b2 and a2
c3 = np.cross(b2, a2)

# Print the result of the cross product of b2 and a2
print(c1)
