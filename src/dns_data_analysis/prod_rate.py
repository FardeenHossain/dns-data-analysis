import numpy as np
import h5py
import os
import mystat
from input import data_path


def main():
    [prod_rate, s_d, c_half] = read_prod_rate()
   
    [prod_rate_cond_jpdf, prod_rate_cond_jpdf_bin_x, 
    prod_rate_cond_jpdf_bin_y] = calc_prod_rate_cond_jpdf(c_half, s_d,
                                                          prod_rate)

    write_prod_rate_cond_jpdf(prod_rate_cond_jpdf, prod_rate_cond_jpdf_bin_x,
                              prod_rate_cond_jpdf_bin_y)


def read_prod_rate():
    prod_rate_data_file_path = "R3K1/mid/data_1.800E-03_prate.h5"
    disp_speed_data_file_path = "R3K1/mid/data_1.800E-03_disp_speed.h5"

    prod_rate_file_path = os.path.join(data_path, prod_rate_data_file_path)
    disp_speed_file_path = os.path.join(data_path, disp_speed_data_file_path)

    # Open file
    f1 = h5py.File(prod_rate_file_path, "r")
    f2 = h5py.File(disp_speed_file_path, "r")

    # Read variables
    prod_rate_transpose = np.array(f1["data/source_O2"])
    s_d = np.array(f2["s_d"])
    c_half = np.array(f2["c_half"])

    # Initialise arrays with zeroes
    prod_rate = np.zeros([len(prod_rate_transpose[0, 0, :]), 
                          len(prod_rate_transpose[0, :, 0]), 
                          len(prod_rate_transpose[:, 0, 0])])

    # Transpose array
    for i in range(0, len(prod_rate_transpose[:, 0, 0])):
        for j in range(0, len(prod_rate_transpose[i, :, 0])):
            for k in range(0, len(prod_rate_transpose[i, j, :])):
                prod_rate[k, j, i] = prod_rate_transpose[i, j, k]

    return [prod_rate, s_d, c_half]


def calc_prod_rate_prog_var_jpdf(c_half, prod_rate):
    # Bin spacing
    c_half_bin_edges_pdf = np.linspace(0, 1, 100)
    prod_rate_bin_edges_pdf = np.linspace(-1e4, 0, 200)

    # Calculate JPDF
    [prod_rate_jpdf, prod_rate_jpdf_bin_x,
     prod_rate_jpdf_bin_y] = mystat.pdf2d(prod_rate, c_half, c_half_bin_edges_pdf, prod_rate_bin_edges_pdf)

    return [prod_rate_jpdf, prod_rate_jpdf_bin_x, prod_rate_jpdf_bin_y]


def calc_prod_rate_cond_jpdf(c_half, s_d, prod_rate):
    # Bin spacing
    s_d_bin_edges_pdf = np.linspace(-1e2, 1e2, 200)
    prod_rate_bin_edges_pdf = np.linspace(-1e4, 0, 200)

    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    # Calculate JPDF
    [prod_rate_cond_jpdf, prod_rate_cond_jpdf_bin_x,
     prod_rate_cond_jpdf_bin_y] = mystat.cond_pdf2d(prod_rate, s_d, c_half,
                                               prod_rate_bin_edges_pdf,
                                               s_d_bin_edges_pdf,
                                               bin_c_cond, d_bin_c_cond)

    return [prod_rate_cond_jpdf, prod_rate_cond_jpdf_bin_x, prod_rate_cond_jpdf_bin_y]


def write_prod_rate_cond_jpdf(prod_rate_jpdf, prod_rate_jpdf_bin_x,
                         prod_rate_jpdf_bin_y):
    data_file_path = "plots/R3K1_mid_jpdf_c_half_prod_rate.txt"
    file_path = os.path.join(data_path, data_file_path)
    file = open(file_path, "w+")

    # Write headings
    file.write("prod_rate_bin_x prod_rate_bin_y prod_rate_jpdf\n")

    # Write JPDF
    for i in range(0, len(prod_rate_jpdf[:, 0])):
        for j in range(0, len(prod_rate_jpdf[i, :])):
            file.write(
                f"{prod_rate_jpdf_bin_x[i]} {prod_rate_jpdf_bin_y[j]} {prod_rate_jpdf[i, j]}\n")
        file.write("\n")

    file.close()
    

def write_prod_rate_cond_jpdf(prod_rate_jpdf, prod_rate_jpdf_bin_x,
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
                file.write(
                    f"{prod_rate_jpdf_bin_x[j]} {prod_rate_jpdf_bin_y[k]} {prod_rate_jpdf[i, j, k]}\n")
        file.write("\n")

    file.close()


main()
