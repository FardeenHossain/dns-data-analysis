import matplotlib.pyplot as plt


def plot_prog_var(c_half):
    """Contour plot of progress variable."""

    plt.contourf(c_half[:, :, 0], cmap='plasma')
    plt.xlabel('Y-Coordinate')
    plt.ylabel('X-Coordinate')
    plt.colorbar(label='Progress Variable, C (-)')
    plt.show()
