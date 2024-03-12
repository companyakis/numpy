a = np.array([i for i in range(10)])

b = np.array([i for i in range(15, 30)])

print(a) # [0 1 2 3 4 5 6 7 8 9]

print(b) # [15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]

concat_ab = np.concatenate([a, b])

print(concat_ab)

"""
[ 0  1  2  3  4  5  6  7  8  9 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]

"""
