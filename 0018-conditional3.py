a = np.array([2 * i -3 for i in range(5, 20)])

print(a)

b = a[(a > 15) & (a % 3 == 0)]

print(b)

"""
[ 7  9 11 13 15 17 19 21 23 25 27 29 31 33 35]

[21 27 33]
"""
