import input
import files

import os
import prog_var
from input import in_path, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end
import matplotlib.pyplot as plt

print("\nDNS Data Analysis")
print("\r----\n")

if input.write_reduced_data == 1:
    print("Writing reduced data...\n")
    files.write_reduced_data()

if input.write_plot_data == 1:
    print("Writing plot data...\n")
    files.write_plot_data()

if input.write_reduced_data == 0 & input.write_plot_data == 0:
    print("No input arguments!\n")

print("\nFinished!")
print("\r----\n")
