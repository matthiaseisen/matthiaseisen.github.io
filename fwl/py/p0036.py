# -(0)
from pprint import pprint
import itertools

a = [[0, 1], [2, 3], [4, 5]]

b = [p for p in itertools.product(*a)]
pprint(b)

# -(/0)
