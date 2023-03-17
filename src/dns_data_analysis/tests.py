import numpy as np
import os
import files
import pdf
from input import flame, position, data_path


def main():
    print("\nDNS Data Analysis - Validation")
    print("\r----\n")

    print("\nFinished!")
    print("\r----\n")


def cond_mean():
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


if __name__ == "__main__":
    main()
