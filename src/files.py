import numpy as np
import h5py
import os

import calc_var

from input import nx_c, ny_c, nz_c, in_path, flame


def write_disp_speed(data_file, prog_var, disp_speed):
    """
    Write progress variable and displacement speed into reduced data files.
    """

    # Reformat data file name
    data_file = data_file.replace(".h5", "")

    # Set file path
    file_path = "./data/%s/%s_disp_speed.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "w")

    # Save dataset
    f1.create_dataset("c_half", (nx_c, ny_c, nz_c), data=prog_var)
    f1.create_dataset("s_d", (nx_c, ny_c, nz_c), data=disp_speed)

    print("Saved progress variable and displacement speed!")


def write_lambda(data_file, lambda1, lambda2, lambda3, rr1, rr2, rr3):
    """
    Write strain rate tensor eigenvalues into reduced data files.
    """

    # Reformat data file name
    data_file = data_file.replace(".h5", "")

    # Set file path
    file_path = "./data/%s/%s_lambda.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "w")

    f1.create_dataset("lambda1", (nx_c, ny_c, nz_c), data=lambda1)
    f1.create_dataset("lambda2", (nx_c, ny_c, nz_c), data=lambda2)
    f1.create_dataset("lambda3", (nx_c, ny_c, nz_c), data=lambda3)
    f1.create_dataset("rr1", (nx_c, ny_c, nz_c, 3), data=rr1)
    f1.create_dataset("rr2", (nx_c, ny_c, nz_c, 3), data=rr2)
    f1.create_dataset("rr3", (nx_c, ny_c, nz_c, 3), data=rr3)

    print("Saved strain rate tensor eigenvalues!")


def read_disp_speed(data_file):
    """Read displacement speed from reduced data files."""

    # Reformat data file name
    data_file = data_file.replace(".h5", "")

    # Set file path
    file_path = "./data/%s/%s_disp_speed.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "r")

    # Import variables
    c_half = np.array(f1['c_half'])
    s_d = np.array(f1['s_d'])

    print("Imported progress variable and displacement speed!")

    return [c_half, s_d]


def read_lambda(data_file):
    """
    Read strain rate tensor eigenvalues from reduced data files.
    """

    # Reformat data file name
    data_file = data_file.replace(".h5", "")

    # Set file path
    file_path = "./data/%s/%s_lambda.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "r")

    # Import variables
    lambda1 = np.array(f1['lambda1'])
    lambda2 = np.array(f1['lambda2'])
    lambda3 = np.array(f1['lambda3'])
    rr1 = np.array(f1['rr1'])
    rr2 = np.array(f1['rr2'])
    rr3 = np.array(f1['rr3'])

    print("Imported strain rate tensor eigenvalues!")

    return [lambda1, lambda2, lambda3, rr1, rr2, rr3]


def list_data_files():
    """Return lists of data files."""

    # List of files in directory
    dir_list = os.listdir(in_path)

    # Initialise empty arrays
    data_file1_list = []
    data_file2_list = []

    # Data files
    for data_file in dir_list:
        if data_file.startswith("data2"):
            # Data file name
            data_file1 = data_file.replace("data2", "data")
            data_file2 = data_file

            # Add to list
            data_file1_list.append(data_file1)
            data_file2_list.append(data_file2)

    return [data_file1_list, data_file2_list]


def write_reduced_data_files():
    """
    Writes reduced data files storing progress variable, displacement speed,
    and strain rate tensor eigenvalues.
    """

    # List of data files
    data_files = list_data_files()
    data_files1 = data_files[0]
    data_files2 = data_files[1]

    for i in range(0, len(data_files1)):
        # Print current data file
        data_file = data_files1[i]
        print('\nCalculating: %s ' % data_file)
        print('\r----\n')

        # Set data file path
        data_file1_path = os.path.join(in_path, data_files1[i])
        data_file2_path = os.path.join(in_path, data_files2[i])

        # Calculate data
        c_half, s_d, lambda1, lambda2, lambda3, rr1, rr2, rr3 \
            = calc_var.calculate_variables(data_file1_path, data_file2_path)

        # Write reduced data file
        print('\nWriting file...')
        write_disp_speed(data_file, c_half, s_d)
        write_lambda(data_file, lambda1, lambda2, lambda3, rr1, rr2, rr3)
