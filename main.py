from random import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sympy import Symbol


class Constraints():
    def __init__(self):
        self.constraints = []

    def add_constraint(self, constraint_data):
        return self.constraints.append(constraint_data)

    def is_constraint_max(self, type_of_constraint):
        if "=" in type_of_constraint:
            return "k"
        return "k--"

    def calculate_constraint(self, a_value, b_value, x_value):
        return a_value * x_value + b_value


class Constraint():
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c


if __name__ == "__main__":
    import warnings
    import operator

    ops = {
        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '=': operator.eq
    }

    warnings.filterwarnings("ignore")

    constraints = Constraints()

    # Input
    current_inequality = input()
    inequality = current_inequality.split()

    a_param = int(inequality[0][:-1])
    b_param = int(inequality[2][:-1]) if inequality[1] == "+" else -int(inequality[2][:-1])
    c_param = int(inequality[-1])

    constraint = Constraint(a_param, b_param, c_param)
    constraints.add_constraint(constraint)

    # Calculation

    x_parameter = Symbol('x')
    y_parameter = Symbol('y')

    mpl.rcParams['toolbar'] = 'None'
    plt.figure("Solution")

    plt.xlim((-10, 10))
    plt.ylim((-10, 10))

    x1 = np.arange(-10, 10, 0.01)
    y1 = a_param / -b_param * x1 + c_param / b_param  # y = ax + b

    coordinates = np.array([[a_param, b_param]])

    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')

    plt.grid()

    plt.xlim((-10, 10))
    plt.ylim((-10, 10))

    plt.plot(x1, y1, constraints.is_constraint_max(current_inequality), color='red')

    plt.plot(coordinates[0][0], coordinates[0][1], linewidth=2, color='red')

    plt.title('Solution')

    N = 10000
    M = 10
    X = []
    Y = []

    for count in range(N):
        x = 1.1 * M * (2 * random() - 1)
        y = 1.1 * M * (2 * random() - 1)
        z = a_param * x + b_param * y
        if ops[inequality[3]](z, c_param):
            X.append(x)
            Y.append(y)
    plt.plot(X, Y, c='red', alpha=0.3, linewidth=3)
    # plt.show()
    plt.show()

# Tests
# 5x + 7y >= 0
# 2x - 3y = -6
# 1x + 3y < 9
# 69x + 420y >= 0
