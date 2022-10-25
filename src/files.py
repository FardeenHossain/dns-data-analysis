import os

# File path
path = '/hpcwork/itv/Antonio/premixed_jet_flames/'

# Flames
flames = ["R1K1", "R2K1", "R3K1", "R4K1"]

# Data size
nx = [720, 1440, 4320, 2880, 5760]
ny = [480, 960, 2160, 1922, 3844]
nz = [256, 256, 512, 512, 1024]

for flame in flames:
    # List of files in directory
    dir_list = os.listdir(path + flame + "/")

    # Data files
    for data_file in dir_list:
        if data_file.startswith("data2"):
            data_file1 = data_file.replace("data2", "data1")
            data_file2 = data_file
