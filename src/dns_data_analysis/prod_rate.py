import numpy as np
import h5py
import os
import mystat
from input import data_path, o2_b, o2_u


def main():
    print("\nDNS Data Analysis - Production Rate")
    print("\r----\n")

    print("Reading data...\n")
    [prod_rate, s_d, c_half, s_d_r] = read_prod_rate()

    print("Calculating data...\n")
    [prod_rate_pdf, prod_rate_bin_pdf] = calc_prod_rate_pdf(c_half, prod_rate)

    [prod_rate_cond_jpdf, prod_rate_cond_jpdf_bin_x,
     prod_rate_cond_jpdf_bin_y] = calc_prod_rate_cond_jpdf(c_half, s_d,
                                                           prod_rate)

    [s_d_cond_jpdf, s_d_cond_jpdf_bin_x,
     s_d_cond_jpdf_bin_y] = calc_disp_speed_cond_jpdf(c_half, s_d, s_d_r)

    [prod_rate_jpdf, prod_rate_jpdf_bin_x,
     prod_rate_jpdf_bin_y] = calc_prod_rate_prog_var_jpdf(c_half, prod_rate)

    print("Writing data...\n")
    write_prod_rate_pdf(prod_rate_pdf, prod_rate_bin_pdf)

    write_prod_rate_prog_var_jpdf(prod_rate_jpdf,
                                  prod_rate_jpdf_bin_x,
                                  prod_rate_jpdf_bin_y)

    write_prod_rate_cond_jpdf(prod_rate_cond_jpdf, prod_rate_cond_jpdf_bin_x,
                              prod_rate_cond_jpdf_bin_y)

    print("\nFinished!")
    print("\r----\n")


def read_prod_rate():
    prod_rate_data_file_path = "R3K1/mid/data_1.800E-03_prate.h5"
    disp_speed_data_file_path = "R3K1/mid/data_1.800E-03_disp_speed.h5"

    prod_rate_file_path = os.path.join(data_path, prod_rate_data_file_path)
    disp_speed_file_path = os.path.join(data_path, disp_speed_data_file_path)

    # Open file
    f1 = h5py.File(prod_rate_file_path, "r")
    f2 = h5py.File(disp_speed_file_path, "r")

    # Read variables
    source_o2 = np.array(f1["data/source_O2"])
    s_d = np.array(f2["s_d"])
    c_half = np.array(f2["c_half"])
    mag_g_c = np.array(f2["mag_g_c"])
    rho_half = np.array(f2["rho_half"])

    # Initialise arrays with zeroes
    prod_rate = np.zeros([len(source_o2[0, 0, :]),
                          len(source_o2[0, :, 0]),
                          len(source_o2[:, 0, 0])])

    s_d_r = np.zeros([len(source_o2[0, 0, :]),
                      len(source_o2[0, :, 0]),
                      len(source_o2[:, 0, 0])])

    # Transpose array and calculate omega
    for i in range(0, len(source_o2[:, 0, 0])):
        for j in range(0, len(source_o2[i, :, 0])):
            for k in range(0, len(source_o2[i, j, :])):
                prod_rate[k, j, i] = - (source_o2[i, j, k] / (o2_u - o2_b))

    # Calculate reactive displacement speed
    for i in prod_rate[:, 0, 0]:
        for j in prod_rate[i, :, 0]:
            for k in prod_rate[i, j, :]:
                s_d_r[i, j, k] = (prod_rate[i, j, k] /
                                  rho_half[i, j, k]) / mag_g_c[i, j, k]

    return [prod_rate, s_d, c_half, s_d_r]


def calc_prod_rate_pdf(c_half, prod_rate):
    """Calculate displacement speed probability density function."""

    # Bin spacing
    bin_edges_pdf = np.linspace(0, 5e4, 200)
    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    # Calculate PDF
    prod_rate_pdf, prod_rate_bin_pdf = mystat.cond_pdf(prod_rate, c_half,
                                                       bin_edges_pdf,
                                                       bin_c_cond,
                                                       d_bin_c_cond)

    return [prod_rate_pdf, prod_rate_bin_pdf]


def calc_prod_rate_prog_var_jpdf(c_half, prod_rate):
    # Bin spacing
    c_half_bin_edges_pdf = np.linspace(0.0, 1.0, 100)
    prod_rate_bin_edges_pdf = np.linspace(0, 5e4, 200)

    # Calculate JPDF
    [prod_rate_jpdf, prod_rate_jpdf_bin_x,
     prod_rate_jpdf_bin_y] = mystat.pdf2d(prod_rate, c_half,
                                          prod_rate_bin_edges_pdf,
                                          c_half_bin_edges_pdf)

    return [prod_rate_jpdf, prod_rate_jpdf_bin_x, prod_rate_jpdf_bin_y]


def calc_prod_rate_cond_jpdf(c_half, s_d, prod_rate):
    # Bin spacing
    s_d_bin_edges_pdf = np.linspace(-1e2, 1e2, 200)
    prod_rate_bin_edges_pdf = np.linspace(0, 5e4, 200)

    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    # Calculate JPDF
    [prod_rate_cond_jpdf, prod_rate_cond_jpdf_bin_x,
     prod_rate_cond_jpdf_bin_y] = mystat.cond_pdf2d(prod_rate, s_d, c_half,
                                                    prod_rate_bin_edges_pdf,
                                                    s_d_bin_edges_pdf,
                                                    bin_c_cond, d_bin_c_cond)

    return [prod_rate_cond_jpdf, prod_rate_cond_jpdf_bin_x,
            prod_rate_cond_jpdf_bin_y]


def calc_disp_speed_cond_jpdf(c_half, s_d, s_d_r):
    # Bin spacing
    s_d_bin_edges_pdf = np.linspace(-1e2, 1e2, 200)
    s_d_r_bin_edges_pdf = np.linspace(-1e2, 1e2, 200)

    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    # Calculate JPDF
    [s_d_cond_jpdf, s_d_cond_jpdf_bin_x,
     s_d_cond_jpdf_bin_y] = mystat.cond_pdf2d(s_d_r, s_d, c_half,
                                              s_d_r_bin_edges_pdf,
                                              s_d_bin_edges_pdf,
                                              bin_c_cond, d_bin_c_cond)

    return [s_d_cond_jpdf, s_d_cond_jpdf_bin_x, s_d_cond_jpdf_bin_y]


def write_prod_rate_pdf(prod_rate_pdf, prod_rate_pdf_bin):
    """Write probability density function to text file."""

    data_file_path = f"plots/R3K1_mid_pdf_prod_rate.txt"
    file_path = os.path.join(data_path, data_file_path)
    file = open(file_path, "w+")

    # Write headings
    file.write("prod_rate_bin prod_rate\n")

    # Write PDF
    for i in range(0, len(prod_rate_pdf[:, 0])):
        for j in range(0, len(prod_rate_pdf[i, :])):
            file.write(f"{prod_rate_pdf_bin[j]} {prod_rate_pdf[i, j]}\n")
        file.write("\n")

    file.close()


def write_prod_rate_prog_var_jpdf(prod_rate_jpdf, prod_rate_jpdf_bin_x,
                                  prod_rate_jpdf_bin_y):
    data_file_path = "plots/R3K1_mid_jpdf_prod_rate_prog_var.txt"
    file_path = os.path.join(data_path, data_file_path)
    file = open(file_path, "w+")

    # Write headings
    file.write("prod_rate_bin_x prod_rate_bin_y prod_rate_jpdf\n")

    # Write JPDF
    for i in range(0, len(prod_rate_jpdf[:, 0])):
        for j in range(0, len(prod_rate_jpdf[i, :])):
            file.write(
                f"{prod_rate_jpdf_bin_x[i]} {prod_rate_jpdf_bin_y[j]} "
                f"{prod_rate_jpdf[i, j]}\n")

    file.close()


def write_prod_rate_cond_jpdf(prod_rate_jpdf, prod_rate_jpdf_bin_x,
                              prod_rate_jpdf_bin_y):
    data_file_path = "plots/R3K1_mid_jpdf_prod_rate_cond.txt"
    file_path = os.path.join(data_path, data_file_path)
    file = open(file_path, "w+")

    # Write headings
    file.write("prod_rate_bin_x prod_rate_bin_y prod_rate_jpdf\n")

    # Write JPDF
    for i in range(0, len(prod_rate_jpdf[:, 0, 0])):
        for j in range(0, len(prod_rate_jpdf[i, :, 0])):
            for k in range(0, len(prod_rate_jpdf[i, j, :])):
                file.write(
                    f"{prod_rate_jpdf_bin_x[j]} {prod_rate_jpdf_bin_y[k]} "
                    f"{prod_rate_jpdf[i, j, k]}\n")
        file.write("\n")

    file.close()


def write_disp_speed_cond_jpdf(s_d_cond_jpdf, s_d_cond_jpdf_bin_x,
                               s_d_cond_jpdf_bin_y):
    data_file_path = "plots/R3K1_mid_jpdf_disp_speed_reactive.txt"
    file_path = os.path.join(data_path, data_file_path)
    file = open(file_path, "w+")

    # Write headings
    file.write("s_d_jpdf_bin_x s_d_jpdf_bin_y s_d_cond_jpdf\n")

    # Write JPDF
    for i in range(0, len(s_d_cond_jpdf[:, 0, 0])):
        for j in range(0, len(s_d_cond_jpdf[i, :, 0])):
            for k in range(0, len(s_d_cond_jpdf[i, j, :])):
                file.write(
                    f"{s_d_cond_jpdf_bin_x[j]} {s_d_cond_jpdf_bin_y[k]} "
                    f"{s_d_cond_jpdf[i, j, k]}\n")
        file.write("\n")

    file.close()


if __name__ == '__main__':
    main()
