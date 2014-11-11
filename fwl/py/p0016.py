# -(0)
def func(x):
    print(x)

def func_2(x):
    return 2*x

a = [1, 2, 3, 4]
map(func, a)

# -(/0)
# -(1)
b = map(func_2, a)
print(b)

# -(/1)
# -(2)
c = [func_2(x) for x in a]
print(c)

# -(/2)
