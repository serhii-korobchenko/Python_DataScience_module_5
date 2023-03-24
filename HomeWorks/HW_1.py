from scipy.optimize import minimize

def goal_func(x):
    a, b = x
    return a + 2*b

def constraint(x):
    return x[0]*x[1] - 1000

# задаем начальное приближение
x0 = [100, 10]

# задаем ограничения на значения переменных
bounds = ((0, 1000), (0, 1000))

# задаем ограничения на функцию
cons = {'type': 'eq', 'fun': constraint}

# используем метод оптимизации SLSQP
solution = minimize(goal_func, x0, method='SLSQP', bounds=bounds, constraints=cons)

print(solution)
