import matplotlib.pyplot as plt
import numpy as np
import h5py
import os
import files
import prog_var

from input import in_path, data_path, ix_start, iy_start, iz_start, ix_end, \
    iy_end, iz_end

read_data = True


def main():
    print("\nDNS Data Analysis - Plot Flame")
    print("\r----\n")

    if read_data:
        print("Reading data...")
        [s_d, c_half] = read_disp_speed()

        print("Plotting data...")
        plot_prog_var(c_half)
        plot_disp_speed(s_d)
    else:
        print("Calculating data...")
        c_half = calc_plot_data()

        print("Plotting data...")
        plot_prog_var(c_half)

    print("\nFinished!")
    print("\r----\n")


def plot_prog_var(c_half):
    plt.contourf(c_half[:, :, 0], levels=np.linspace(0, 1, 11), cmap='jet_r',
                 extend='both')
    plt.xlabel(r'$y$')
    plt.ylabel(r'$x$')
    plt.colorbar(label=r'$C$')
    plt.show()


def plot_disp_speed(s_d):
    plt.contourf(s_d[:, :, 0], cmap='jet_r', extend='both')
    plt.xlabel(r'$y$')
    plt.ylabel(r'$x$')
    plt.colorbar(label=r'$S_d$')
    plt.show()


def calc_plot_data():
    [data_file1_list, data_file2_list] = files.list_data_files()

    data_file1_path = os.path.join(in_path, data_file1_list[0])
    data_file2_path = os.path.join(in_path, data_file2_list[0])

    c_half = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                    ix_start, iy_start, iz_start, ix_end,
                                    iy_end, iz_end)

    return c_half[0]


def read_disp_speed():
    """Read displacement speed from reduced data files."""

    data_file_path = "R3K1/mid/data_1.800E-03_disp_speed.h5"
    file_path = os.path.join(data_path, data_file_path)

    f1 = h5py.File(file_path, "r")

    c_half = np.array(f1["c_half"])
    s_d = np.array(f1["s_d"])

    return [c_half, s_d]


if __name__ == "__main__":
    main()
