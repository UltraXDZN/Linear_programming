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

    def calculate_optimal_point(self, id1, id2):
        try:
            xi = ((self.constraints[id1].c * self.constraints[id2].b) - (
                    self.constraints[id1].b * self.constraints[id2].c)) \
                 / ((self.constraints[id1].a * self.constraints[id2].b) - (
                    self.constraints[id2].a * self.constraints[id1].b))
        except ZeroDivisionError:
            xi = 0
        yi = self.constraints[id1].a / -self.constraints[id1].b * xi + \
             self.constraints[id1].c / self.constraints[id1].b
        print(
            "Points of ideal coordinates are:\n\t"
            f"( {xi} , {yi} )"
        )
        return [xi, yi]

    def find_optimal_point(self, id1, id2):
        ideal_x, ideal_y = self.calculate_optimal_point(id1, id2)
        plt.plot(ideal_x, ideal_y, color="black", marker="o")
        plt.text(ideal_x, ideal_y, f'( {ideal_x:.2f} , {ideal_y:.2f} )')


class Constraint():
    def __init__(self, a=0, b=0, c=0, operator="="):
        self.a = a
        self.b = b
        self.c = c
        self.operator = operator


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

    mpl.rcParams['toolbar'] = 'None'
    plt.figure("Solution")

    plt.xlim((-10, 10))
    plt.ylim((-10, 10))

    current_inequality = ""
    print(f"Enter all equations in style of \"ax + by <=> c\"\n and all color codes with # before hex number!")
    while True:
        # Input
        current_inequality = input("Please enter new equation: ")
        line_color = input("Please enter new color: ")
        if current_inequality == "0":
            break
        inequality = current_inequality.split()

        a_param = int(inequality[0][:-1])
        b_param = int(inequality[2][:-1]) if inequality[1] == "+" else -int(inequality[2][:-1])
        c_param = int(inequality[-1])

        constraint = Constraint(a_param, b_param, c_param, inequality[3])
        constraints.add_constraint(constraint)

        # Calculation

        x_parameter = Symbol('x')
        y_parameter = Symbol('y')

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

        plt.plot(x1, y1, constraints.is_constraint_max(current_inequality), color=line_color)

        plt.plot(coordinates[0][0], coordinates[0][1], linewidth=2, color=line_color)

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
        plt.plot(X, Y, color=line_color, alpha=0.3, linewidth=3)
        # plt.show()

    if len(constraints.constraints) > 1:
        for i in range(1, len(constraints.constraints)):
            constraints.find_optimal_point(i, i - 1)
            # plt.show()
        constraints.find_optimal_point(-1, 0)
    plt.show()

# Tests
# 5x + 7y >= 0
# 2x - 3y = -6
# 2x - 3y < -6
# 1x + 3y < 9
# 69x + 420y >= 0
# 3x + 2y <= 10000
# Please enter new color: red
# Please enter new equation: 10x + 10y <= 43200
# Please enter new color: blue
