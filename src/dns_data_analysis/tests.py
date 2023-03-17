import numpy as np
import os
import curvature
import files
import pdf
from pyevtk.hl import gridToVTK
from input import flame, position, data_path


def main():
    print("\nDNS Data Analysis - Validation")
    print("\r----\n")

    print("Conditional mean test...\n")
    cond_mean_test()

    print("Curvature test...\n")
    curvature_test()

    print("\nFinished!")
    print("\r----\n")


def cond_mean_test():
    # List of data files
    [data_files, data_files2] = files.list_data_files()

    # Calculate progress variable and displacement speed
    [c_half, s_d, mag_g_c, k_m] = files.read_disp_speed(
        data_files[0])

    # Calculate conditional mean
    [c_bin, s_d_cond_mean] = pdf.calc_disp_speed_cond_mean(c_half, s_d)

    # Write file
    data_file_path = f"plots/{flame}_{position}_cond_mean_disp_speed_1.txt"
    file_path = os.path.join(data_path, data_file_path)
    file = open(file_path, "w+")
    file.write("c_bin s_d_cond_mean\n")
    for i in range(0, len(s_d_cond_mean[:])):
        file.write(f"{c_bin[i]} {s_d_cond_mean[i]}\n")
    file.close()

    for i in range(1, 9):
        [c_half_i, s_d_i, mag_g_c_i, k_m_i] = files.read_disp_speed(
            data_files[i])
        c_half = np.concatenate((c_half, c_half_i))
        s_d = np.concatenate((s_d, s_d_i))

    # Calculate conditional mean
    [c_bin, s_d_cond_mean] = pdf.calc_disp_speed_cond_mean(c_half, s_d)

    # Write file
    data_file_path = f"plots/{flame}_{position}_cond_mean_disp_speed_10.txt"
    file_path = os.path.join(data_path, data_file_path)
    file = open(file_path, "w+")
    file.write("c_bin s_d_cond_mean\n")
    for i in range(0, len(s_d_cond_mean[:])):
        file.write(f"{c_bin[i]} {s_d_cond_mean[i]}\n")
    file.close()


def curvature_test():
    # Cylinder
    center_x = 0.2
    center_y = 0.2
    radius = 0.05
    height_z = 0.1
    z = np.linspace(0, height_z, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid) + center_x
    y_grid = radius * np.sin(theta_grid) + center_y

    # Calculate curvature
    dx = 1
    c_half = [x_grid, y_grid, z_grid]
    k_m = curvature.mean_curv(c_half, dx)

    # Export VTK
    nx = len(c_half[:, 0, 0])
    ny = len(c_half[0, :, 0])
    nz = len(c_half[0, 0, :])
    x1 = np.linspace(0, nx * dx, num=nx + 1)
    y1 = np.linspace(0, ny * dx, num=ny + 1)
    z1 = np.linspace(0, nz * dx, num=nz + 1)
    x, y, z = np.meshgrid(x1, y1, z1, indexing='ij')
    gridToVTK("./output", x, y, z,
              cellData={"k_m": k_m[:, :, :]})


if __name__ == "__main__":
    main()
