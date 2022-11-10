import os

flames = ["R1K1", "R2K1", "R3K1", "R4K1"]

i = 2               # 0 = R1K1, 1 = R2K1, 2 = R3K1, 3 = R4K1
flame = flames[i]   # Select flame from array

in_path = '/hpcwork/itv/Antonio/premixed_jet_flames/%s/' % flame

# Input arguments
import_data = 1
write_data = 0

# Data size array
nx_list = [720, 1440, 4320, 2880, 5760]
ny_list = [480, 960, 2160, 1922, 3844]
nz_list = [256, 256, 512, 512, 1024]

# Data size
nx = nx_list[i]
ny = ny_list[i]
nz = nz_list[i]

# Chunk size
nx_c = 100
ny_c = 100
nz_c = 10

# Start point
ix_start = 800
iy_start = 850
iz_start = 1

# End point
ix_end = ix_start + nx_c
iy_end = iy_start + ny_c
iz_end = iz_start + nz_c

# Oxygen values
o2_u = 2.237710e-01  # Unburned
o2_b = 6.677090e-02  # Burned

data_file1 = 'data_1.300E-03.h5'
data_file2 = 'data2_1.300E-03.h5'

data_file1_path = os.path.join(in_path, data_file1)
data_file2_path = os.path.join(in_path, data_file2)

# info = hdf5read(['../data_', listfile{i}], 'data', 'time_variables')
# dt = info(1)

# Constants
dt = 1.15577e-07
dx = 20e-6
