import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol


def calculate_constraint(a_value, b_value, x_value):
    return a_value * x_value + b_value


class Constraints():
    def __init__(self):
        self.constraints = []

    def add_contraint(self, a_value, b_value, x_value):
        return self.constraints.append(calculate_constraint(a_value, b_value, x_value))


if __name__ == "__main__":
    constraints = Constraints()
    x_parameter = Symbol('x')

    x1, = solve(
        calculate_constraint(4.0, -2.0, x_parameter) - calculate_constraint(0.5, 2.0, x_parameter))
    x2, = solve(
        calculate_constraint(4.0, -2.0, x_parameter) - calculate_constraint(-0.3, 7.0, x_parameter))
    x3, = solve(
        calculate_constraint(0.5, 2.0, x_parameter) - calculate_constraint(-0.3, 7.0, x_parameter))

    y1 = calculate_constraint(4, -2, x1)
    y2 = calculate_constraint(4, -2, x2)
    y3 = calculate_constraint(0.5, 2.0, x3)

    plt.plot(x1, y1, 'go--', markersize=10)
    plt.plot(x2, y2, 'go--', markersize=10)
    plt.plot(x3, y3, 'go--', markersize=10)

    plt.fill([x1, x2, x3, x1], [y1, y2, y3, y1], 'red', alpha=0.5)

    xr = np.linspace(0.5, 7.5, 100)
    y1r = calculate_constraint(4, -2, xr)
    y2r = calculate_constraint(0.5, 2, xr)
    y3r = calculate_constraint(-0.3, 7, xr)

    plt.plot(xr, y1r, 'k--')
    plt.plot(xr, y2r, 'k--')
    plt.plot(xr, y3r, 'k--')

    plt.xlim(0.5, 7)
    plt.ylim(2, 8)

    plt.show()
