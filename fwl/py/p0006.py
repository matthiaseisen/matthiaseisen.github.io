# -(0)
a = ['aaaa', 'B', 'CCC', 'dd']

b = sorted(a, key=lambda x: len(x))
print(b)

# -(/0)
# -(1)
print(a)

# -(/1)
# -(2)
a.sort(key=lambda x: len(x))
print(a)

# -(/2)
