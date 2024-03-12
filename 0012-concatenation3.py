a = np.array([[3, 4, 5], [6, 7, 8]])

b = np.array([[-5, -2, -10], [-11, -33, -44]])

concat_ab = np.concatenate([a, b], axis = 1)

print(concat_ab)

"""
[[  3   4   5  -5  -2 -10]
 [  6   7   8 -11 -33 -44]]

"""
