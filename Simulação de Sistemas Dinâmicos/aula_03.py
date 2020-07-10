#Definir uma função f(x) = e^-(x^2)
#sua derivada f'(x) = (f(x+h) - f(x-h))/2h
# e plotar dois gráficos (x, y), (y, dy)

from pylab import *

def f(x):
    return exp(-(x**2))

def derivative(f, x, h = 1e-12):
    return (f(x+h) - f(x-h))/(2*h)

def integral(f,a,b,n=10001):
	n = int(ceil(n))
	h = (b-a)/(n-2)
	x = linspace(a,b,n)
	return h*sum(f(x))

def integral_sen2(a, b):
    return ((a/2) - (sin(2*a)/4))-(b/2) - (sin(2*b)/4)


x = linspace(-5, 5, 1000)
y = f(x)
h = 0.00001
dy = derivative(f, x)


plot(x, y)
plot(x, dy)
show()
