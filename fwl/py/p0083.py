# -(0)
from pprint import pprint
from itertools import permutations as perm

a = ['a', 'b', 'c']

b = list(perm(a))
pprint(b)

# -(/0)
# -(1)
c = [''.join(p) for p in perm(a)]
print(c)

# -(/1)
# -(2)
d = [''.join(p) for p in perm(a, 2)]
print(d)

# -(/2)
