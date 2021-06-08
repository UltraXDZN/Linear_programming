import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sympy import Symbol, solve


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

    # def choose_constraint_side(self, type_of_constraint):
    #     if ">" in type_of_constraint or "<" in type_of_constraint:
    #
    #     return None

class Constraint():
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")

    current_inequality = input()
    inequality = current_inequality.split()

    a_param = int(list(inequality[0])[0])
    b_param = int(list(inequality[2])[0]) if inequality[1] == "+" else -int(list(inequality[2])[0])
    c_param = int(inequality[-1])



    # Try 2
    constraints = Constraints()
    x_parameter = Symbol('x')
    y_parameter = Symbol('y')

    mpl.rcParams['toolbar'] = 'None'
    plt.figure()

    # Set x-axis range
    plt.xlim((-10, 10))
    # Set y-axis range
    plt.ylim((-10, 10))


    x1 = np.arange(-10, 10, 0.01)  # between -10 and 10, 0.01 stepsize
    y1 = a_param / -b_param * x1 + c_param / b_param  # y = ax + b

    plt.fill(x1,y1, color='red', alpha=0.3, zorder=10)

    a = np.array([[a_param, b_param]])

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

    plt.plot(x1, y1, constraints.is_constraint_max(current_inequality), color='red')

    # draw the equations
    plt.plot(a[0][0], a[0][1], linewidth=2, color='red')

    plt.title('Solution')

    plt.show()

    # print(a_param, b_param, c_param)

# Tests
# 5x + 7y >= 0
# 2x - 3y = -6
# 1x + 3y < 9
