import numpy as np
import h5py
import os
import calc_var

from input import nx_c, ny_c, nz_c, in_path, flame


def list_data_files():
    """Return lists of data files from input path."""

    # List of files in directory
    dir_list = os.listdir(in_path)

    # Initialise empty arrays
    data_file1_list = []
    data_file2_list = []

    for data_file in dir_list:
        if data_file.startswith("data2"):
            data_file1 = data_file.replace("data2", "data")
            data_file2 = data_file

            # Add to list
            data_file1_list.append(data_file1)
            data_file2_list.append(data_file2)

    return [data_file1_list, data_file2_list]


def write_reduced_data():
    """Writes reduced data files storing progress variable, displacement speed,
    and strain rate tensor eigenvalues."""

    # List of data files
    [data_files1, data_files2] = list_data_files()

    for i in range(0, len(data_files1)):
        data_file = data_files1[i]
        print(f"{data_file}")

        data_file1_path = os.path.join(in_path, data_files1[i])
        data_file2_path = os.path.join(in_path, data_files2[i])

        # Calculate variables
        [c_half, s_d, lambda1, lambda2, lambda3, rr1, rr2,
         rr3] = calc_var.calculate_data(data_file1_path, data_file2_path)

        # Save data
        write_disp_speed(data_file, c_half, s_d)
        write_lambda(data_file, lambda1, lambda2, lambda3, rr1, rr2, rr3)

        print("Finished writing reduced data!\n")


def read_reduced_data():
    """Reads reduced data files storing progress variable, displacement speed,
    and strain rate tensor eigenvalues."""

    # List of data files
    [data_files, data_files2] = list_data_files()

    # Initialise arrays
    [c_half_full, s_d_full] = read_disp_speed(data_files[0])
    [lambda1_full, lambda2_full, lambda3_full, rr1_full, rr2_full,
     rr3_full] = read_lambda(data_files[0])

    for i in range(1, len(data_files)):
        [c_half, s_d] = read_disp_speed(data_files[i])
        [lambda1, lambda2, lambda3, rr1, rr2, rr3] = read_lambda(data_files[i])

        # Append to array
        c_half_full = np.concatenate((c_half_full, c_half))
        s_d_full = np.concatenate((s_d_full, s_d))
        lambda1_full = np.concatenate((lambda1_full, lambda1))
        lambda2_full = np.concatenate((lambda2_full, lambda2))
        lambda3_full = np.concatenate((lambda3_full, lambda3))

    return [c_half_full, s_d_full, lambda1_full, lambda2_full, lambda3_full]


def write_plot_data():
    # Read reduced data
    [c_half, s_d, lambda1, lambda2, lambda3] = read_reduced_data()

    # Calculate PDF
    [s_d_pdf, s_d_pdf_bin, lambda1_pdf, lambda1_pdf_bin, lambda2_pdf,
     lambda2_pdf_bin, lambda3_pdf, lambda3_pdf_bin] = calc_var.calculate_pdf(
        c_half, s_d, lambda1, lambda2, lambda3)

    # Calculate JPDF
    [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, lambda2_jpdf,
     lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, lambda3_jpdf, lambda3_jpdf_bin_x,
     lambda3_jpdf_bin_y] = calc_var.calculate_jpdf(c_half, s_d, lambda1,
                                                   lambda2, lambda3)

    # Write to text file
    write_disp_speed_pdf(s_d_pdf, s_d_pdf_bin)
    write_lambda_pdf(lambda1_pdf, lambda1_pdf_bin, 1)
    write_lambda_pdf(lambda2_pdf, lambda2_pdf_bin, 2)
    write_lambda_pdf(lambda3_pdf, lambda3_pdf_bin, 3)
    write_lambda_jpdf(lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, 1)
    write_lambda_jpdf(lambda2_jpdf, lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, 2)
    write_lambda_jpdf(lambda3_jpdf, lambda3_jpdf_bin_x, lambda3_jpdf_bin_y, 3)

    print("Finished writing plot data!\n")


def write_disp_speed(data_file, prog_var, disp_speed):
    """Write progress variable and displacement speed into reduced data
    files."""

    data_file = data_file.replace(".h5", "")
    file_path = f"./data/{flame}/{data_file}_disp_speed.hdf5"

    # Open file
    f1 = h5py.File(file_path, "w")

    # Save dataset
    f1.create_dataset("c_half", (nx_c, ny_c, nz_c), data=prog_var)
    f1.create_dataset("s_d", (nx_c, ny_c, nz_c), data=disp_speed)


def write_lambda(data_file, lambda1, lambda2, lambda3, rr1, rr2, rr3):
    """Write strain rate tensor eigenvalues into reduced data files."""

    data_file = data_file.replace(".h5", "")
    file_path = f"./data/{flame}/{data_file}_lambda.hdf5"

    # Open file
    f1 = h5py.File(file_path, "w")

    # Save dataset
    f1.create_dataset("lambda1", (nx_c, ny_c, nz_c), data=lambda1)
    f1.create_dataset("lambda2", (nx_c, ny_c, nz_c), data=lambda2)
    f1.create_dataset("lambda3", (nx_c, ny_c, nz_c), data=lambda3)
    f1.create_dataset("rr1", (nx_c, ny_c, nz_c, 3), data=rr1)
    f1.create_dataset("rr2", (nx_c, ny_c, nz_c, 3), data=rr2)
    f1.create_dataset("rr3", (nx_c, ny_c, nz_c, 3), data=rr3)


def read_disp_speed(data_file):
    """Read displacement speed from reduced data files."""

    data_file = data_file.replace(".h5", "")
    file_path = f"./data/{flame}/{data_file}_disp_speed.hdf5"

    # Open file
    f1 = h5py.File(file_path, "r")

    # Read variables
    c_half = np.array(f1["c_half"])
    s_d = np.array(f1["s_d"])

    return [c_half, s_d]


def read_lambda(data_file):
    """Read strain rate tensor eigenvalues from reduced data files."""

    data_file = data_file.replace(".h5", "")
    file_path = f"./data/{flame}/{data_file}_lambda.hdf5"

    # Open file
    f1 = h5py.File(file_path, "r")

    # Read variables
    lambda1 = np.array(f1["lambda1"])
    lambda2 = np.array(f1["lambda2"])
    lambda3 = np.array(f1["lambda3"])
    rr1 = np.array(f1["rr1"])
    rr2 = np.array(f1["rr2"])
    rr3 = np.array(f1["rr3"])

    return [lambda1, lambda2, lambda3, rr1, rr2, rr3]


def write_disp_speed_pdf(s_d_pdf, s_d_pdf_bin):
    """Write probability density function to text file."""

    file_path = f"./data/plots/{flame}_pdf_disp_speed.txt"
    file = open(file_path, "w+")

    # Write headings
    file.write("s_d_bin s_d\n")

    # Write PDF
    for i in range(0, len(s_d_pdf[:, 0])):
        for j in range(0, len(s_d_pdf[i, :])):
            file.write(f"{s_d_pdf_bin[j]} {s_d_pdf[i, j]}\n")
        file.write("\n")

    file.close()


def write_lambda_pdf(lambda_pdf, lambda_pdf_bin, subscript):
    """Write probability density function to text file."""

    file_path = f"./data/plots/{flame}_pdf_lambda_{subscript}.txt"
    file = open(file_path, "w+")

    # Write headings
    file.write("lambda_bin lambda_pdf\n")

    # Write PDF
    for i in range(0, len(lambda_pdf[:, 0])):
        for j in range(0, len(lambda_pdf[i, :])):
            file.write(f"{lambda_pdf_bin[j]} {lambda_pdf[i, j]}\n")
        file.write("\n")

    file.close()


def write_lambda_jpdf(lambda_jpdf, lambda_jpdf_bin_x, lambda_jpdf_bin_y,
                      subscript):
    """Write joint probability density function to text file."""

    file_path = f"./data/plots/{flame}_jpdf_lambda_{subscript}.txt"
    file = open(file_path, "w+")

    # Write headings
    file.write("lambda_bin_x lambda_bin_y lambda_jpdf\n")

    # Write JPDF
    for i in range(0, len(lambda_jpdf[:, 0, 0])):
        for j in range(0, len(lambda_jpdf[i, :, 0])):
            for k in range(0, len(lambda_jpdf[i, j, :])):
                file.write(f"{lambda_jpdf_bin_x[j]} {lambda_jpdf_bin_y[k]} "
                           f"{lambda_jpdf[i, j, k]}\n")
        file.write("\n")

    file.close()
