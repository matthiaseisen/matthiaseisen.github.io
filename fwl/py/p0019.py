# -(0)
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = [x for x in a if x in b]
print(c)

# -(/0)
# -(1)
d = list(set(a) & set(b))
print(d)

# -(/1)
# -(2)
e = list(set(a).intersection(b))
print(e)

# -(/2)
