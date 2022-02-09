def f(x):
    return x**2

g = f
print(f(4))
print(g(4))

def calc1(x):
    return x * 10

def math(op, x):
    print(op(x))

math(calc1, 10)

def sum(x,y):
    return x + y

def mylt(x, y):
    return x * y

def calc (op, a, b):
    print(op(a, b))

calc(lambda x, y: x * y, 3, 4)