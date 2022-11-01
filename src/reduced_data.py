import os
import input
import prog_var
import disp_speed
import files


# Print title
print('\nDirect Numerical Simulation (DNS) Premixed - Reduced Data')
print('\r----\n')

# Flame
flame = "R3K1"

# List of data files
data_files = files.list_data_files(flame)
data_files1 = data_files[0]
data_files2 = data_files[1]

# Begin loop
for i in range(0, len(data_files1)):
    # Set path
    in_path = '/hpcwork/itv/Antonio/premixed_jet_flames/%s/' % flame

    # Set data file path
    data_file = data_files1[i]
    data_file1 = os.path.join(in_path, data_files1[i])
    data_file2 = os.path.join(in_path, data_files2[i])

    # Calculate U
    u_half = prog_var.calc_u(data_file1, data_file2,
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate V
    v_half = prog_var.calc_v(data_file1, data_file2,
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate W
    w_half = prog_var.calc_w(data_file1, data_file2,
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate progress variable
    c = prog_var.calc_prog_var(data_file1, data_file2,
                               input.ix_start, input.iy_start,
                               input.iz_start, input.ix_end,
                               input.iy_end, input.iz_end)

    c_half = c[0]
    dc = c[1]

    # Calculate displacement speed
    disp_speed = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

    # Write displacement speed and progress variable
    files.write_disp_speed(c_half, disp_speed, data_file, flame)

# Print finish
print("\nFinished!\n")
print("\r----\n")
