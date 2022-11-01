import h5py
import os
from input import nx_c, ny_c, nz_c

# File path
path = '/hpcwork/itv/Antonio/premixed_jet_flames'

# Flames
flames = ["R1K1", "R2K1", "R3K1", "R4K1"]

# Data size
nx = [720, 1440, 4320, 2880, 5760]
ny = [480, 960, 2160, 1922, 3844]
nz = [256, 256, 512, 512, 1024]


def list_data_files(flame):
    """Return lists of data files."""

    # List of files in directory
    file_path = "%s/%s/" % (path, flame)
    dir_list = os.listdir(file_path)

    # Initialise empty arrays
    data_file1_list = []
    data_file2_list = []

    # Data files
    for data_file in dir_list:
        if data_file.startswith("data2"):
            # Data file name
            data_file1 = data_file.replace("data2", "data1")
            data_file2 = data_file

            # Add to list
            data_file1_list.append(data_file1)
            data_file2_list.append(data_file2)

    return [data_file1_list, data_file2_list]


def write_disp_speed(prog_var, disp_speed, data_file, flame):
    """
    Write progress variable and displacement speed into reduced data files.
    """

    # Set file path
    file_path = ".data/%s/%s_disp_speed.hdf5" % (flame, data_file)

    # Open file
    f1 = h5py.File(file_path, "w")

    # Save dataset
    f1.create_dataset("c_half", (nx_c, ny_c, nz_c), data=prog_var)
    f1.create_dataset("s_d", (nx_c, ny_c, nz_c), data=disp_speed)

    print("\nSaved progress variable and displacement speed!\n")


# Driver function
data_files = list_data_files(flames[0])
data_files1 = data_files[0]
data_files2 = data_files[1]

# Print files
print(data_files1)
print(data_files2)
