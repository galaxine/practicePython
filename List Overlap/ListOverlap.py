# Write a program that takes these two lists and return a new list that only returns the the same elements.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# new way
c = list(set(a).intersection(set(b)))
print(c)

