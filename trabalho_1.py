#Trabalho 1

from pylab import *

### a)
#integrates sen^2(x) in the interval [a, b]
def definite_integral(a, b):
    return ((a/2) - (sin(2*a)/4))-(b/2) - (sin(2*b)/4)

### b)
definite_integral(0, 2*pi)

### c)
#integral of cos(x)
x = linspace(0,2*pi,1000)
plot(x, sin(x))
show()

