# -(0)
n = 3

a = [1, 2, 3, 4, 5, 6]
b = a.pop(n - 1)
print(b)

# -(/0)
# -(1)
print(a)

# -(/1)
# -(2)
a = [1, 2, 3, 4, 5, 6]
del a[n - 1]
print(a)

# -(/2)
# -(3)
a = [1, 2, 3, 4, 5, 6]
c = a[:n - 1] + a[n:]
print(c)

# -(/3)
# -(4)
print(a)

# -(/4)
# -(5)
a = [1, 2, 3, 4, 5, 6]
c = [v for i, v in enumerate(a) if i != n - 1]
print(c)

# -(/5)
# -(6)
print(a)

# -(/6)
