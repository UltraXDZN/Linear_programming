from main import *

if __name__ == "__main__":
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')

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

    plt.fill([x1, x2, x3], [y1, y2, y3], 'red', alpha=0.5)

    xr = np.linspace(0.5, 7.5, 100)
    y1r = calculate_constraint(4, -2, xr)
    y2r = calculate_constraint(0.5, 2, xr)

    plt.plot(xr, y1r, 'k--')
    plt.plot(xr, y2r, 'k--')

    # plt.xlim(0.5, 7)
    # plt.ylim(2, 8)

    plt.show()
