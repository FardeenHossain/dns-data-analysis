# Print title
print('\nDNS Premixed - Compute disp_speed & c')
print('\r----\n')

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
