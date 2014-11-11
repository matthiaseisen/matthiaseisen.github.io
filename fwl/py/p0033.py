# -(0)
x = 4

a = [1, 2, 3, 4, 4, 5, 6, 1, 4]
for i in range(a.count(x)):
    a[a.index(x)] = 0
print(a)

# -(/0)
# -(1)
a = [1, 2, 3, 4, 4, 5, 6, 1, 4]
b = [v if v != x else 0 for v in a ]
print(b)

# -(/1)
# -(2)
print(a)

# -(/2)
