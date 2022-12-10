# Input arguments
write_reduced_data = 0
write_plot_data = 1
plot_flame = 0
full_data_range = 0

i = 2   # 0 = R1K1, 1 = R2K1, 2 = R3K1, 3 = R4K1
j = 1   # 0 = bot, 1 = mid, 2 = top

flames = ["R1K1", "R2K1", "R3K1", "R4K1"]
positions = ['bot', 'mid', 'top']

flame = flames[i]
position = positions[j]

in_path = f"/hpcwork/itv/Antonio/premixed_jet_flames/{flame}/"
data_path = f"/hpcwork/itv/Antonio/Fardeen/python/data/"

# Data size array
nx_array = [720, 1440, 2880, 5760]
ny_array = [480, 960, 1922, 3844]
nz_array = [256, 256, 512, 1024]

# Chunk size array
nx_c_array = [20, 20, 20, 20]
ny_c_array = [75, 150, 300, 600]
nz_c_array = [255, 255, 511, 1023]

# Start point array
iy_start_array = [200, 400, 800, 1600]
iz_start_array = [0, 0, 0, 0]

# Position start point
if position == 'bot':
    ix_start_array = [20, 40, 80, 100]
if position == 'mid':
    ix_start_array = [200, 400, 800, 1000]
if position == 'top':
    ix_start_array = [450, 900, 1350, 1800]

if full_data_range:
    ix_start_array = [0, 0, 0, 0]
    iy_start_array = [0, 0, 0, 0]
    iz_start_array = [0, 0, 0, 0]

    nx_c_array = [719, 1439, 2879, 5759]
    ny_c_array = [479, 959, 1921, 3843]
    nz_c_array = [1, 1, 1, 1]

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

# Constants
dx = 20e-6
