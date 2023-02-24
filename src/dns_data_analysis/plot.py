import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import h5py
import os
import files
import prog_var
from pyevtk.hl import gridToVTK

from input import in_path, data_path, ix_start, iy_start, iz_start, ix_end, \
    iy_end, iz_end

read_data = False
export_vtk = True


def main():
    print("\nDNS Data Analysis - Plot Flame")
    print("\r----\n")

    if read_data:
        print("Reading data...")
        [s_d, c_half] = read_disp_speed()

        print("Plotting data...")
        plot_prog_var(c_half)
        plot_disp_speed(s_d)
        plot_cond_disp_speed(s_d, c_half)
    elif export_vtk:
        [s_d, c_half] = read_disp_speed()
        export_vtk(c_half, s_d)
    else:
        print("Calculating data...")
        c_half = calc_plot_data()

        print("Plotting data...")
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


def plot_disp_speed(s_d):
    plt.contourf(s_d[:, :, 0], cmap='hot', extend='both')
    plt.xlabel(r'$y$')
    plt.ylabel(r'$x$')
    plt.colorbar(label=r'$S_d$')
    plt.show()


def plot_cond_disp_speed(s_d, c_half):
    for i in range(0, len(c_half[:, 0, 0])):
        for j in range(0, len(c_half[i, :, 0])):
            for k in range(0, len(c_half[i, j, :])):
                if c_half[i, j, k] < 0.60 or c_half[i, j, k] > 0.90:
                    s_d[i, j, k] = "NaN"

    plt.contour(c_half[:, 138:158, 0], levels=[0, 0.73], colors='white')
    plt.contourf(s_d[:, 138:158, 0], levels=100, cmap='hot', extend='both')
    plt.xlabel(r'$y$')
    plt.ylabel(r'$x$')
    plt.colorbar(label=r'$S_d$')

    line = Line2D([0], [0], label='C = 0.73', color='white')
    plt.legend(handles=[line], facecolor="gray", loc="upper left")

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

    return [s_d, c_half]


def export_vtk(c_half, s_d):
    # nx = 20
    # ny = 500
    # nz = 20
    #
    # x1 = np.linspace(0, 1, num=nx + 1)
    # y1 = np.linspace(0, 1, num=ny + 1)
    # z1 = np.linspace(0, 1, num=nz + 1)
    #
    # x, y, z = np.meshgrid(x1, y1, z1, indexing='ij')
    #
    # gridToVTK("./structured", x, y, z,
    #           cellData={"c": c_half[:, :, :20], "s_d": s_d[:, :, :20]})

    nx = 20
    ny = 50
    nz = 60

    x1 = np.linspace(0, 1, num=nx + 1)
    y1 = np.linspace(0, 1, num=ny + 1)
    z1 = np.linspace(0, 1, num=nz + 1)
    x, y, z = np.meshgrid(x1, y1, z1, indexing='ij')

    c = np.zeros((nx, ny, nz))
    q = np.zeros((nx, ny, nz))
    xm = 0.5 * (x1[0:-1] + x1[1:])
    ym = 0.5 * (y1[0:-1] + y1[1:])
    zm = 0.5 * (z1[0:-1] + z1[1:])
    for k in range(nz):
        for j in range(ny):
            for i in range(nx):
                c[i, j, k] = xm[i] * ym[j]
                q[i, j, k] = xm[i]

    gridToVTK("./structured", x, y, z, cellData={"c": c, "q": q})


if __name__ == "__main__":
    main()
