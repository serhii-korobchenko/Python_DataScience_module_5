from scipy import integrate

f = lambda y, x: x**2 + y**2
a, b = 0, 1
gfun = lambda x: 0
hfun = lambda x: x**2

result = integrate.dblquad(f, a, b, gfun, hfun)

print(result)