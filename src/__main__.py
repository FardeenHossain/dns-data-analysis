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

# PLOT PROGRESS VARIABLE
[data_file1_list, data_file2_list] = files.list_data_files()
data_file1_path = os.path.join(in_path, data_file1_list[0])
data_file2_path = os.path.join(in_path, data_file2_list[0])
[c_half, dc] = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                      ix_start, iy_start, iz_start, ix_end,
                                      iy_end, iz_end)
plt.contourf(c_half[:, :, 0], cmap='plasma')
plt.xlabel('Y-Coordinate')
plt.ylabel('X-Coordinate')
plt.colorbar(label='Progress Variable, C (-)')
plt.show()

print("\nFinished!")
print("\r----\n")
