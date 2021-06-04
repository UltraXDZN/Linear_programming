import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol


def calculate_constraint(a_value, b_value, x_value):
    return a_value * x_value + b_value


class Constraints():
    def __init__(self):
        self.constraints = []

    def add_constraint(self, a_value, b_value, x_value):
        return self.constraints.append(calculate_constraint(a_value, b_value, x_value))


if __name__ == "__main__":
    # constraints = Constraints()
    # x_parameter = Symbol('x')
    #
    # x1, = solve(
    #     calculate_constraint(4.0, -2.0, x_parameter) - calculate_constraint(0.5, 2.0, x_parameter))
    # x2, = solve(
    #     calculate_constraint(4.0, -2.0, x_parameter) - calculate_constraint(-0.3, 7.0, x_parameter))
    # x3, = solve(
    #     calculate_constraint(0.5, 2.0, x_parameter) - calculate_constraint(-0.3, 7.0, x_parameter))
    #
    # y1 = calculate_constraint(4, -2, x1)
    # y2 = calculate_constraint(4, -2, x2)
    # y3 = calculate_constraint(0.5, 2.0, x3)
    #
    # plt.plot(x1, y1, 'go--', markersize=10)
    # plt.plot(x2, y2, 'go--', markersize=10)
    # plt.plot(x3, y3, 'go--', markersize=10)
    #
    # plt.fill([x1, x2, x3, x1], [y1, y2, y3, y1], 'red', alpha=0.5)
    #
    # xr = np.linspace(0.5, 7.5, 100)
    # y1r = calculate_constraint(4, -2, xr)
    # y2r = calculate_constraint(0.5, 2, xr)
    # y3r = calculate_constraint(-0.3, 7, xr)
    #
    # plt.plot(xr, y1r, 'k--')
    # plt.plot(xr, y2r, 'k--')
    # plt.plot(xr, y3r, 'k--')
    #
    # plt.xlim(0.5, 7)
    # plt.ylim(2, 8)

    constraints = Constraints()
    x_parameter = Symbol('x')
    y_parameter = Symbol('y')

    plt.figure()

    # Set x-axis range
    plt.xlim((-10, 10))
    # Set y-axis range
    plt.ylim((-10, 10))
    # Draw lines to split quadrants
    plt.plot([-10, 10], [0, 0], color='C0')
    plt.plot([0, 0], [-10, 10], color='C0')


    current_inequality = input()
    inequality = current_inequality.split()

    a = int(list(inequality[0])[0])
    b = int(list(inequality[2])[0]) if inequality[1] == "+" else -int(list(inequality[2])[0])
    c = int(inequality[-1])


    x1 = np.arange(-10, 10, 0.01)  # between -10 and 10, 0.01 stepsize
    y1 = a * x1 + c

    a = np.array([[a, b]])

    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    # plt.figure()
    # Set x-axis range
    plt.xlim((-10, 10))
    # Set y-axis range
    plt.ylim((-10, 10))
    # Draw lines to split quadrants
    # plt.plot([-10, -10], [10, 10], linewidth=4, color='blue')
    plt.plot(x1, y1, color='red')

    # draw the equations
    plt.plot(a[0][0], a[0][1], linewidth=2, color='red')

    plt.title('Solution')

    plt.show()

    print(a, b, c)

#5x + 7y >= 0