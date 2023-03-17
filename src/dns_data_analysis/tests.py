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
    x = np.linspace(-1, 1, 100)
    z = np.linspace(-2, 2, 100)
    x_c, z_c = np.meshgrid(x, z)
    y_c = np.sqrt(1 - x_c ** 2)

    # Calculate curvature
    k_m = curvature.mean_curv([x_c, y_c, z_c], 1)

    # Export VTK
    nx = len(x_c)
    ny = len(y_c)
    nz = len(z_c)
    x1 = np.linspace(0, nx, num=nx + 1)
    y1 = np.linspace(0, ny, num=ny + 1)
    z1 = np.linspace(0, nz, num=nz + 1)
    x, y, z = np.meshgrid(x1, y1, z1, indexing='ij')
    gridToVTK("./output", x, y, z,
              cellData={"k_m": k_m[:, :, :]})


if __name__ == "__main__":
    main()
