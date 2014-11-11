# -(0)
n = 3

a = [1, 2, 3, 4]
a[n - 1] = 0
print(a)

# -(/0)
# -(1)
a = [1, 2, 3, 4]
b = [v if i != n -1 else 0 for i, v in enumerate(a)]
print(b)

# -(/1)
# -(2)
print(a)

# -(/2)
