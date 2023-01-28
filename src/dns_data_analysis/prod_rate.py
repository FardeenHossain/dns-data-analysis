import numpy as np
import h5py
import os
import mystat
import plot
from input import data_path


def main():
    [prod_rate, s_d, c_half] = read_prod_rate()

    [prod_rate_jpdf, prod_rate_jpdf_bin_x,
     prod_rate_jpdf_bin_y] = calc_prod_rate_jpdf(c_half, s_d, prod_rate)

    write_prod_rate_jpdf(prod_rate_jpdf, prod_rate_jpdf_bin_x,
                         prod_rate_jpdf_bin_y)


def read_prod_rate():
    prod_rate_data_file_path = "R3K1/mid/data_1.800E-03_prate.h5"
    disp_speed_data_file_path = "R3K1/mid/data_1.800E-03_disp_speed.h5"

    prod_rate_file_path = os.path.join(data_path, prod_rate_data_file_path)
    disp_speed_file_path = os.path.join(data_path, disp_speed_data_file_path)

    f1 = h5py.File(prod_rate_file_path, "r")
    f2 = h5py.File(disp_speed_file_path, "r")

    prod_rate = np.array(f1["T"])
    s_d = np.array(f2["s_d"])
    c_half = np.array(f2["c_half"])

    print(prod_rate.size)
    print(s_d.size)

    plot.plot_prog_var(c_half)

    return [prod_rate, s_d, c_half]


def calc_prod_rate_jpdf(c_half, s_d, prod_rate):
    s_d_bin_edges_pdf = np.linspace(-1e2, 1e2, 200)
    prod_rate_bin_edges_pdf = np.linspace(-2e5, 2e5, 200)

    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    [prod_rate_jpdf, prod_rate_jpdf_bin_x,
     prod_rate_jpdf_bin_y] = mystat.cond_pdf2d(prod_rate, s_d, c_half,
                                               prod_rate_bin_edges_pdf,
                                               s_d_bin_edges_pdf,
                                               bin_c_cond, d_bin_c_cond)

    return [prod_rate_jpdf, prod_rate_jpdf_bin_x, prod_rate_jpdf_bin_y]


def write_prod_rate_jpdf(prod_rate_jpdf, prod_rate_jpdf_bin_x,
                         prod_rate_jpdf_bin_y):
    data_file_path = "plots/R3K1_mid_jpdf_prod_rate.txt"
    file_path = os.path.join(data_path, data_file_path)
    file = open(file_path, "w+")

    # Write headings
    file.write("prod_rate_bin_x prod_rate_bin_y prod_rate_jpdf\n")

    # Write JPDF
    for i in range(0, len(prod_rate_jpdf[:, 0, 0])):
        for j in range(0, len(prod_rate_jpdf[i, :, 0])):
            for k in range(0, len(prod_rate_jpdf[i, j, :])):
                file.write("{0} {1} {2}\n".format(prod_rate_jpdf_bin_x[j],
                                                  prod_rate_jpdf_bin_y[k],
                                                  prod_rate_jpdf[i, j, k]))
        file.write("\n")

    file.close()


main()
