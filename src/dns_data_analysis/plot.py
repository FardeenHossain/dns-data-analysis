import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import h5py
import os
import files
import prog_var
import disp_speed
from pyevtk.hl import gridToVTK

from input import in_path, data_path, ix_start, iy_start, iz_start, ix_end, \
    iy_end, iz_end

read = False
calculate = False
export = True
    
def main():
    print("\nDNS Data Analysis - Plot Flame")
    print("\r----\n")

    if read:
        print("Reading data...")
        [s_d, c_half] = read_disp_speed()
        plot_prog_var(c_half)
        plot_disp_speed(s_d)
        plot_cond_disp_speed(s_d, c_half)
        
    if export:
        print("Exporting data...")    
        [c_half, s_d] = calc_plot_data()
        export_vtk(c_half, s_d)
        
    if calculate:
        print("Calculating data...")
        [c_half, s_d] = calc_plot_data()
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

    ix_start = 2075
    ix_end = 2175

    iy_start = 1750
    iy_end = 1850

    iz_start = 0
    iz_end = 100
    
    u_half = prog_var.calc_u(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    v_half = prog_var.calc_v(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    w_half = prog_var.calc_w(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)
                             

    [c_half, dc] = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                          ix_start, iy_start, iz_start, ix_end,
                                          iy_end, iz_end)

    [s_d, mag_g_c] = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

    return [c_half, s_d]


def read_disp_speed():
    """Read displacement speed from reduced data files."""

    data_file_path = "R3K1/mid/data_1.800E-03_disp_speed.h5"
    file_path = os.path.join(data_path, data_file_path)

    f1 = h5py.File(file_path, "r")

    c_half = np.array(f1["c_half"])
    s_d = np.array(f1["s_d"])

    return [s_d, c_half]


def export_vtk(c_half, s_d):
       
    nx = len(c_half[:, 0, 0])
    ny = len(c_half[0, :, 0])
    nz = len(c_half[0, 0, :])

    x1 = np.linspace(0, 1, num=nx + 1)
    y1 = np.linspace(0, 1, num=ny + 1)
    z1 = np.linspace(0, 1, num=nz + 1)

    x, y, z = np.meshgrid(x1, y1, z1, indexing='ij')

    gridToVTK("./output", x, y, z,
              cellData={"c": c_half[:, :, :], "s_d": s_d[:, :, :]})


if __name__ == "__main__":
    main()
