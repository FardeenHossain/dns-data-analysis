import os
import input
import prog_var
import disp_speed
import files

# Print title
print('\nDirect Numerical Simulation (DNS) Premixed - Reduced Data')
print('\r----\n')

# List of data files
data_files = files.list_data_files(input.flame)
data_files1 = data_files[0]
data_files2 = data_files[1]

# Begin loop
for i in range(0, len(data_files1)):
    # Print current data file
    data_file = data_files1[i]
    print("Calculating: %s\n " % data_file)

    # Set data file path
    data_file1_path = os.path.join(input.in_path, data_files1[i])
    data_file2_path = os.path.join(input.in_path, data_files2[i])

    # Calculate U
    u_half = prog_var.calc_u(data_file1_path, data_file2_path,
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate V
    v_half = prog_var.calc_v(data_file1_path, data_file2_path,
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate W
    w_half = prog_var.calc_w(data_file1_path, data_file2_path,
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate progress variable
    c = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                               input.ix_start, input.iy_start,
                               input.iz_start, input.ix_end,
                               input.iy_end, input.iz_end)

    c_half = c[0]
    dc = c[1]

    # Calculate displacement speed
    s_d = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

    # Write displacement speed and progress variable
    files.write_disp_speed(data_file, input.flame, c_half, s_d)

# Print finish
print("\nFinished!\n")
print("\r----\n")
