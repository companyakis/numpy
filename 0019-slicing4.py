np.random.seed(12)

a = np.random.randint(15, size = (6, 5)) # elements between 0 and 15 and 6 * 5 dimemnsion

print(a)

print("......................")

print(a[0:2, 1:])

"""
[[11 11  6 13  1]
 [ 2  3  3 12  0]
 [ 6  1  4  5 13]
 [ 9  2 11  6 10]
 [ 0  5  8 12 13]
 [ 2  9  3 14  4]]
......................
[[11  6 13  1]
 [ 3  3 12  0]]
"""
