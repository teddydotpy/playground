import math

def Fixed_point(x, y, tol):
    f = 2*(math.exp(-x))

    for i in range(tol):
        print(f)
        f = 2*(math.exp(-f))
    

def Newton_Raphson(x, tol):
    f = x - (x*math.exp(x)-2)/(-x*math.exp(-x)+math.exp(-x))
    for i in range(tol):
        print(f)
        f - (f*math.exp(f)-2)/(-f*math.exp(-f)+math.exp(-f))

Newton_Raphson(1, 5)

print("Fixed point now//")
Fixed_point(0.7, 0, 10)