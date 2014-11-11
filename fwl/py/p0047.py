# -(0)
x = 3
y = 4
a = [1, 2, 4, 5, 4, 6, 2]

try:
    a.insert(a.index(y), x)
except ValueError:
    a.append(x)
print(a)

# -(/0)
# -(1)
a = [1, 2, 4, 5, 4, 6, 2]
try:
    i = a.index(y)
    b = a[:i] + [x] + a[i:]
except ValueError:
    b = a + [x]
print(b)

# -(/1)
# -(2)
print(a)

# -(/2)
