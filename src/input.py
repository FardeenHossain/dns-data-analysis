import os

# File path
in_path = '/hpcwork/itv/Antonio/premixed_jet_flames/R3K1/'
IF_save = 0

# Data range
Nx = 2880
Ny = 1922
Nz = 512

# Chunk range
Nx_c = 30
Ny_c = 10
Nz_c = 50

# Start point
ix_start = 800
iy_start = 850
iz_start = 1

# End point
ix_end = ix_start + Nx_c
iy_end = iy_start + Ny_c
iz_end = iz_start + Nz_c

# Oxygen values
o2_u = 2.237710e-01  # Unburned
o2_b = 6.677090e-02  # Burned

# Data files
data_file1 = os.path.join(in_path, 'data_1.300E-03.h5')
data_file2 = os.path.join(in_path, 'data2_1.300E-03.h5')

# info = hdf5read(['../data_', listfile{i}], 'data', 'time_variables')
# dt = info(1)

# Time derivative
dt = 1.15577e-07

# x derivative
dx = 20e-6
