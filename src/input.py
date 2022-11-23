import os

flames = ["R1K1", "R2K1", "R3K1", "R4K1"]

i = 0               # 0 = R1K1, 1 = R2K1, 2 = R3K1, 3 = R4K1
flame = flames[i]   # Select flame from array

in_path = f"/hpcwork/itv/Antonio/premixed_jet_flames/{flame}/"

# Input arguments
write_reduced_data = 1
write_plot_data = 1

# Data size array
nx_array = [720, 1440, 2880, 5760]
ny_array = [480, 960, 1922, 3844]
nz_array = [256, 256, 512, 1024]

# Chunk size array
nx_c_array = [20, 20, 20, 20]
ny_c_array = [100, 100, 300, 600]
nz_c_array = [255, 255, 511, 1023]

# Start point array
ix_start_array = [200, 400, 800, 1000]
iy_start_array = [185, 425, 800, 1600]
iz_start_array = [0, 0, 0, 0]

# Data size
nx = nx_array[i]
ny = ny_array[i]
nz = nz_array[i]

# Chunk size
nx_c = nx_c_array[i]
ny_c = ny_c_array[i]
nz_c = nz_c_array[i]

# Start point
ix_start = ix_start_array[i]
iy_start = iy_start_array[i]
iz_start = iz_start_array[i]

# End point
ix_end = ix_start + nx_c
iy_end = iy_start + ny_c
iz_end = iz_start + nz_c

# Oxygen values
o2_u = 2.237710e-01  # Unburned
o2_b = 6.677090e-02  # Burned

data_file1 = "data_1.300E-03.h5"
data_file2 = "data2_1.300E-03.h5"

data_file1_path = os.path.join(in_path, data_file1)
data_file2_path = os.path.join(in_path, data_file2)

# info = hdf5read(['../data_', listfile{i}], 'data', 'time_variables')
# dt = info(1)

# Constants
dt = 1.15577e-07
dx = 20e-6
