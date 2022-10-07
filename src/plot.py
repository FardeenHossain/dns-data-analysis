import matplotlib.pyplot as plt


def plot_displacement_speed(disp_speed_c):
    """Contour plot of displacement speed."""

    # Print title
    print('\nPlotting displacement speed...\n')

    plt.figure(1)
    plt.contourf(disp_speed_c[:, :, 1])
    plt.xlabel('y-coordinate')
    plt.ylabel('x-coordinate')
    plt.colorbar(label=r'Displacement Speed, $\rmS_{d}$')
    plt.style.use('seaborn')
    plt.show()
