import matplotlib.pyplot as plt
import numpy as np
import os
import files
import prog_var
import disp_speed

from input import in_path, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end


def main():
    print("\nDNS Data Analysis - Plot Flame")
    print("\r----\n")

    print("Calculating data...\n")
    [s_d, c_half] = calc_plot_data()

    print("Plotting data...\n")
    plot_prog_var(c_half)
    plot_disp_speed(s_d)

    print("\nFinished!")
    print("\r----\n")


def plot_prog_var(c_half):
    plt.contourf(c_half[:, :, 0], levels=np.linspace(0, 1, 11), cmap='jet_r',
                 extend='both')
    plt.xlabel(r'$y')
    plt.ylabel(r'$x')
    plt.colorbar(label=r'$C')
    plt.show()


def plot_disp_speed(s_d):
    plt.contourf(s_d[:, :, 0], levels=np.linspace(0, 1, 11), cmap='jet_r',
                 extend='both')
    plt.xlabel(r'$y')
    plt.ylabel(r'$x')
    plt.colorbar(label=r'$S_d')
    plt.show()


def calc_plot_data():
    [data_file1_list, data_file2_list] = files.list_data_files()

    data_file1_path = os.path.join(in_path, data_file1_list[0])
    data_file2_path = os.path.join(in_path, data_file2_list[0])

    u_half = prog_var.calc_u(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    v_half = prog_var.calc_v(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    w_half = prog_var.calc_w(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    [c_half, dc] = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                          ix_start, iy_start, iz_start, ix_end,
                                          iy_end, iz_end)

    s_d = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

    return [s_d, c_half]


if __name__ == "__main__":
    main()
