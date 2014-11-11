# -(0)
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = [x for x in set(a + b)]
print(c)

# -(/0)
# -(1)
d = list(set(a) | set(b))
print(d)

# -(/1)
# -(2)
e = list(set(a).union(b))
print(e)

# -(/2)
