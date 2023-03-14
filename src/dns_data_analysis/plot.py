import matplotlib.pyplot as plt
import numpy as np
import h5py
import os
import curvature
import disp_speed
import files
import prog_var
from pyevtk.hl import gridToVTK
from input import in_path, data_path, dx, o2_u, o2_b, ix_start, iy_start, \
    iz_start, ix_end, iy_end, iz_end

# Input arguments
read = False
calculate = False
export = True
reaction = False


def main():
    print("\nDNS Data Analysis - Plot Flame")
    print("\r----\n")

    if read:
        print("Reading data...\n")
        [s_d, c_half] = read_disp_speed()
        plot_prog_var(c_half)
        plot_disp_speed(s_d)
        plot_cond_disp_speed(s_d, c_half)

    if export:
        print("Exporting data...\n")
        [c_half, s_d, k] = calc_plot_data()
        export_vtk(c_half, s_d, k)

    if calculate:
        print("Calculating data...\n")
        [c_half, s_d, k] = calc_plot_data()
        plot_prog_var(c_half)

    print("\nFinished!")
    print("\r----\n")


def plot_prog_var(c_half):
    plt.contourf(c_half[:, :, 0], levels=np.linspace(0, 0.9, 10), cmap='hot',
                 extend='both')
    plt.xlabel(r'$y$')
    plt.ylabel(r'$x$')
    plt.colorbar(label=r'$C$')
    plt.show()


def calc_plot_data():
    [data_file1_list, data_file2_list] = files.list_data_files()

    data_file1_path = os.path.join(in_path, data_file1_list[0])
    data_file2_path = os.path.join(in_path, data_file2_list[0])

    ix_start = 500
    ix_end = 2500

    iy_start = 1600
    iy_end = 2200

    iz_start = 0
    iz_end = 8

    u_half = prog_var.calc_u(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    v_half = prog_var.calc_v(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    w_half = prog_var.calc_w(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    [c_half, dc] = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                          ix_start, iy_start, iz_start, ix_end,
                                          iy_end, iz_end)

    [s_d, mag_g_c] = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half,
                                                dc)

    k = curvature.mean_curv(c_half, dx)

    return [c_half, s_d, k]


def read_disp_speed():
    """Read displacement speed from reduced data files."""

    data_file_path = "R3K1/mid/data_1.800E-03_disp_speed.h5"
    file_path = os.path.join(data_path, data_file_path)

    f1 = h5py.File(file_path, "r")

    c_half = np.array(f1["c_half"])
    s_d = np.array(f1["s_d"])

    return [s_d, c_half]


def read_prod_rate():
    prod_rate_data_file_path = "R4K1/top/data_1.600E-03_prate.h5"
    prod_rate_file_path = os.path.join(data_path, prod_rate_data_file_path)

    # Open file
    f1 = h5py.File(prod_rate_file_path, "r")

    # Read variables
    source_o2 = np.array(f1["data/source_O2"])

    # Initialise arrays with zeroes
    prod_rate = np.zeros([len(source_o2[0, 0, :]),
                          len(source_o2[0, :, 0]),
                          len(source_o2[:, 0, 0])])

    # Transpose array and calculate omega
    for i in range(0, len(source_o2[:, 0, 0])):
        for j in range(0, len(source_o2[i, :, 0])):
            for k in range(0, len(source_o2[i, j, :])):
                prod_rate[k, j, i] = - (source_o2[i, j, k] / (o2_u - o2_b))

    return prod_rate


def export_vtk(c_half, s_d, k):
    nx = len(c_half[:, 0, 0])
    ny = len(c_half[0, :, 0])
    nz = len(c_half[0, 0, :])

    x1 = np.linspace(0, nx * dx, num=nx + 1)
    y1 = np.linspace(0, ny * dx, num=ny + 1)
    z1 = np.linspace(0, nz * dx, num=nz + 1)

    x, y, z = np.meshgrid(x1, y1, z1, indexing='ij')

    if reaction:
        omega_c = read_prod_rate()
        gridToVTK("./output", x, y, z,
                  cellData={"c": c_half[:, :, :], "s_d": s_d[:, :, :],
                            "k": k[:, :, :], "omega_c": omega_c[:, :, :]})
    else:
        gridToVTK("./output", x, y, z,
                  cellData={"c": c_half[:, :, :], "s_d": s_d[:, :, :],
                            "k": k[:, :, :]})


if __name__ == "__main__":
    main()
