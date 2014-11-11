# -(0)
a = [1, 2, 3]
b = [4, 5, 6]

c = [(x, y) for x in a for y in b]
print(c)

# -(/0)
# -(1)
import itertools
d = [p for p in itertools.product(a, b)]
print(d)

# -(/1)
