x = [1, 2, 3, 4, 5, 6, 7]
y = x.copy()

for i in range(6):
    x[i] = x[i] * 2

print(x)
print(y)