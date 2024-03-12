import numpy as np

# NumPy Array

a = np.array([i for i in range(10)])

print(a) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(a)) # <class 'numpy.ndarray'>

b = np.array([i + 0.1 for i in range(10)])

print(b) # [0.1 1.1 2.1 3.1 4.1 5.1 6.1 7.1 8.1 9.1]

b = np.array([i + 0.1 for i in range(10)], dtype="int")

print(b) # [0 1 2 3 4 5 6 7 8 9]
