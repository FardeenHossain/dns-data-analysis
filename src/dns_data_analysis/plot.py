import matplotlib.pyplot as plt
import files
import prog_var
import os

from input import in_path, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end


def plot_flame():
    c_half = calc_plot_data()
    plot_prog_var(c_half)


def plot_prog_var(c_half):
    """Contour plot of progress variable."""

    plt.contourf(c_half[:, :, 0], cmap='plasma')
    plt.xlabel('Y-Coordinate')
    plt.ylabel('X-Coordinate')
    plt.colorbar(label='Progress Variable, C (-)')
    plt.show()


def calc_plot_data():
    """Calculate progress variable."""

    [data_file1_list, data_file2_list] = files.list_data_files()

    data_file1_path = os.path.join(in_path, data_file1_list[0])
    data_file2_path = os.path.join(in_path, data_file2_list[0])

    [c_half, dc] = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                          ix_start, iy_start, iz_start, ix_end,
                                          iy_end, iz_end)

    return c_half
