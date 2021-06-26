import random as r

x = r.sample(range(1,30), 14)
y = r.sample(range(1,30), 15)
z = [l for l in set(x) if l in y]
print(z)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [i for i in set(b) if i in a]

print(c)