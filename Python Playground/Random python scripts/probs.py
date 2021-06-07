#! /usr/bin/env python3

x = [0, 1, 2, 3, 4, 5]
pofx = [0.1, 0.2, 0.2, 0.3, 0.15, 0.05]

def expectValue(x, pofx):
    buff = [( x[i] * pofx[i]) for i in range(len(x))]
    return sum(buff)

def variance(y, pofy):
    variance = 0
    expect_V = expectValue(y, pofy)
    for i in range(len(y)):
        variance += ((y[i] - expect_V)**2) * pofy[i]

    return variance

print("Variance is: " + str( variance(x, pofx) ))