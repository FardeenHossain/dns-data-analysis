import h5py
import os
from input import nx_c, ny_c, nz_c, in_path


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


def write_disp_speed(data_file, flame, prog_var, disp_speed):
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

    print("Saved progress variable and displacement speed!\n")


def write_lambda(data_file, flame, lambda1, lambda2, lambda3, rr1, rr2, rr3):
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

    print("Saved strain rate tensor eigenvalues!\n")
