from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

k = 0.5
N = 1000
y0 = 10
t0, tf = 0, 25


def dydt(t, y):
    return k * y * (1 - y / N)


soln = solve_ivp(dydt, (t0, tf), [y0])
print(soln)


t, y = soln.t, soln.y[0]
plt.plot(t, y, 'o', color='k', label='solve_ivp')
plt.legend()
plt.show()

soln = solve_ivp(dydt, (t0, tf), [y0], dense_output=True)
t, y = soln.t, soln.y[0]
z, = soln.sol(t)
plt.plot(t, y, 'o', color='k', label='solve_ivp')
plt.plot(t, z, color='blue', label='Interpolation')
plt.legend()
plt.show()