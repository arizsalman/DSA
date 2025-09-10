# What is zip
"""zip ek iterator banata hai jo multiple lists (ya iterables) ko ek saath pair karke deta hai."""


a = [1, 2, 3]
b = ["x", "y", "z"]

for i, j in zip(a, b):
    print(i, j)


a = [1, 2, 3]
b = ["x", "y", "z"]
c = [True, False, True]

for i, j, k in zip(a, b, c):
    print(i, j, k)
