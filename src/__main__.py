import input
import files

from input import in_path, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end
import prog_var
import plot
import os

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

[data_files1, data_files2] = files.list_data_files()
data_file1_path = os.path.join(in_path, data_files1[0])
data_file2_path = os.path.join(in_path, data_files2[0])

[c_half, dc] = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                      ix_start, iy_start, iz_start, ix_end,
                                      iy_end, iz_end)

plot.plot_prog_var(c_half)

print("\nFinished!")
print("\r----\n")
