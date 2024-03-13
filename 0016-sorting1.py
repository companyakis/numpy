np.random.seed(2024)

a = np.random.randint(10, 30, 15)

print(a) #[18 10 10 14 19 11 13 20 12 10 15 27 25 20 24]

#without a variable

print(np.sort(a)) #[10 10 10 11 12 13 14 15 18 19 20 20 24 25 27]

#same array!

print(a) #[18 10 10 14 19 11 13 20 12 10 15 27 25 20 24]
