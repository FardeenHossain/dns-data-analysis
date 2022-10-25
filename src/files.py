import os

# File path
path = '/hpcwork/itv/Antonio/premixed_jet_flames/'

# Flames
flames = ["R1K1", "R2K1", "R3K1", "R4K1"]

# Flames directory
flames_dir = []
for flame in flames:
    flames_dir.append(path + flame + "/")

# Data size of each flame
nx = [720, 1440, 4320, 2880, 5760]
ny = [480, 960, 2160, 1922, 3844]
nz = [256, 256, 512, 512, 1024]

# Data files
for path in flames_dir:
    dir_list = os.listdir(path)
