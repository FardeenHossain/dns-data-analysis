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


def write_data_files():
    """Writes reduced data files storing progress variable, displacement speed,
    and strain rate tensor eigenvalues."""

    # List of data files
    data_files = list_data_files()
    data_files1 = data_files[0]
    data_files2 = data_files[1]

    for i in range(0, len(data_files1)):
        data_file = data_files1[i]
        print('\nCalculating: %s ' % data_file)
        print('\r----\n')

        data_file1_path = os.path.join(in_path, data_files1[i])
        data_file2_path = os.path.join(in_path, data_files2[i])

        # Calculate variables
        var = calc_var.calculate_variables(data_file1_path, data_file2_path)

        # Assign variables
        c_half = var[0]
        s_d = var[1]
        lambda1 = var[2]
        lambda2 = var[3]
        lambda3 = var[4]
        rr1 = var[5]
        rr2 = var[6]
        rr3 = var[7]

        # Calculate PDF values
        pdf = calc_var.calculate_pdf(c_half, s_d, lambda1, lambda2, lambda3)

        # Assign variables
        s_d_pdf = pdf[0]
        s_d_bin_pdf = pdf[1]
        lambda1_pdf = pdf[2]
        lambda1_bin_pdf = pdf[3]
        lambda2_pdf = pdf[4]
        lambda2_bin_pdf = pdf[5]
        lambda3_pdf = pdf[6]
        lambda3_bin_pdf = pdf[7]

        write_disp_speed(data_file, c_half, s_d)
        write_lambda(data_file, lambda1, lambda2, lambda3, rr1, rr2, rr3)

        write_pdf(data_file, lambda1_pdf, lambda1_bin_pdf, lambda2_pdf,
                  lambda2_bin_pdf, lambda3_pdf, lambda3_bin_pdf)


def write_disp_speed(data_file, prog_var, disp_speed):
    """Write progress variable and displacement speed into reduced data
    files."""

    data_file = data_file.replace(".h5", "")
    file_path = "./data/%s/%s_disp_speed.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "w")

    # Save dataset
    f1.create_dataset("c_half", (nx_c, ny_c, nz_c), data=prog_var)
    f1.create_dataset("s_d", (nx_c, ny_c, nz_c), data=disp_speed)

    print("Saved displacement speed!")


def write_lambda(data_file, lambda1, lambda2, lambda3, rr1, rr2, rr3):
    """Write strain rate tensor eigenvalues into reduced data files."""

    data_file = data_file.replace(".h5", "")
    file_path = "./data/%s/%s_lambda.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "w")

    # Save dataset
    f1.create_dataset("lambda1", (nx_c, ny_c, nz_c), data=lambda1)
    f1.create_dataset("lambda2", (nx_c, ny_c, nz_c), data=lambda2)
    f1.create_dataset("lambda3", (nx_c, ny_c, nz_c), data=lambda3)
    f1.create_dataset("rr1", (nx_c, ny_c, nz_c, 3), data=rr1)
    f1.create_dataset("rr2", (nx_c, ny_c, nz_c, 3), data=rr2)
    f1.create_dataset("rr3", (nx_c, ny_c, nz_c, 3), data=rr3)

    print("Saved strain rate tensor eigenvalues!")


def read_disp_speed(data_file):
    """Read displacement speed from reduced data files."""

    data_file = data_file.replace(".h5", "")
    file_path = "./data/%s/%s_disp_speed.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "r")

    # Read variables
    c_half = np.array(f1['c_half'])
    s_d = np.array(f1['s_d'])

    print("Imported progress variable and displacement speed!")

    return [c_half, s_d]


def read_lambda(data_file):
    """Read strain rate tensor eigenvalues from reduced data files."""

    data_file = data_file.replace(".h5", "")
    file_path = "./data/%s/%s_lambda.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "r")

    # Read variables
    lambda1 = np.array(f1['lambda1'])
    lambda2 = np.array(f1['lambda2'])
    lambda3 = np.array(f1['lambda3'])
    rr1 = np.array(f1['rr1'])
    rr2 = np.array(f1['rr2'])
    rr3 = np.array(f1['rr3'])

    print("Imported strain rate tensor eigenvalues!")

    return [lambda1, lambda2, lambda3, rr1, rr2, rr3]


def write_pdf(data_file, lambda1_pdf, lambda1_bin_pdf, lambda2_pdf,
              lambda2_bin_pdf, lambda3_pdf, lambda3_bin_pdf):
    """Write probability density function to text file."""

    data_file = data_file.replace(".h5", "")
    file_path = "./data/%s/%s_plot.txt" % (flame, data_file)
    file = open(file_path, "w+")

    file.write("lambda1_pdf lambda2_pdf lambda3_pdf\n")

    for i in range(0, len(lambda1_pdf[:, 0, 0])):
        for j in range(0, len(lambda1_pdf[0, :, 0])):
            for k in range(0, len(lambda1_pdf[0, 0, :])):
                file.write("%d %d %d\n" %
                           (lambda1_pdf[i, j, k], lambda2_pdf[i, j, k],
                            lambda3_pdf[i, j, k]))

    print("Saved strain rate tensor PDF!")

    file.close()
