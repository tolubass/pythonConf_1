class Calculator:
    def add(x):
        z = 0
        t = len(x)
        i = 0
        while i < t:
            z = z + x[i]
            i += 1
        return z
    def subtract(x):
        b = 0
        c = len(x)
        i = 0
        while i < c:
            b = b - x[i]
            i += 1
        return b
    def multiply(x,y):
        return x*y
    def divide(x,y):
        return x/y
