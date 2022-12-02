import matplotlib.pyplot as plt
import numpy as np
import os
import files
import prog_var

from input import in_path, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end


def plot_flame():
    c_half = calc_plot_data()
    plot_prog_var(c_half)


def plot_prog_var(c_half):
    """Contour plot of progress variable."""

    plt.contourf(c_half[:, :, 0], levels=np.linspace(0, 1, 11), cmap='jet_r',
                 extend='both')
    plt.xlabel('y')
    plt.ylabel('x')
    plt.colorbar(label='C')
    plt.show()


def calc_plot_data():
    """Calculate progress variable."""

    # Data files
    [data_file1_list, data_file2_list] = files.list_data_files()
    data_file1_path = os.path.join(in_path, data_file1_list[0])
    data_file2_path = os.path.join(in_path, data_file2_list[0])

    # Calculate progress variable
    c_half = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                    ix_start, iy_start, iz_start, ix_end,
                                    iy_end, iz_end)

    return c_half[0]
