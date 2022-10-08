import matplotlib.pyplot as plt


def plot_disp_speed(disp_speed):
    """Contour plot of displacement speed."""

    plt.figure(1)
    plt.contourf(disp_speed[:, :, 1])
    plt.xlabel('y-coordinate')
    plt.ylabel('x-coordinate')
    plt.colorbar(label=r'Displacement Speed, $\rmS_{d}$')
    plt.style.use('seaborn')
    plt.show()
