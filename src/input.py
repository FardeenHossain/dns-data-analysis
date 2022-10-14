import os

# File path
in_path = '/hpcwork/itv/Antonio/premixed_jet_flames/R3K1/'
if_save = 0

# Data size
nx = 2880
ny = 1922
nz = 512

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

# Data files
data_file1 = os.path.join(in_path, 'data_1.300E-03.h5')
data_file2 = os.path.join(in_path, 'data2_1.300E-03.h5')

# info = hdf5read(['../data_', listfile{i}], 'data', 'time_variables')
# dt = info(1)

# Constants
dt = 1.15577e-07
dx = 20e-6
