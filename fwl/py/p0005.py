# -(0)
a = ['d', 'C', 'B', 'a']

b = sorted(a, key=lambda x: x.lower())
print(b)

# -(/0)
# -(1)
print(a)

# -(/1)
# -(2)
a.sort(key=lambda s: s.lower())
print(a)

# -(/2)
