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
    # Calculate U
    u_half = prog_var.calc_u(data_files1[i], data_files2[i],
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate V
    v_half = prog_var.calc_v(data_files1[i], data_files2[i],
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate W
    w_half = prog_var.calc_w(data_files1[i], data_files2[i],
                             input.ix_start, input.iy_start, input.iz_start,
                             input.ix_end, input.iy_end, input.iz_end)

    # Calculate progress variable
    prog_var = prog_var.calc_prog_var(data_files1[i], data_files2[i],
                                      input.ix_start, input.iy_start,
                                      input.iz_start, input.ix_end,
                                      input.iy_end, input.iz_end)

    c_half = prog_var[0]
    dc = prog_var[1]

    # Calculate displacement speed
    disp_speed = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

    # Write displacement speed and progress variable
    files.write_disp_speed(c_half, disp_speed, data_files1[i], flame)

# Print finish
print("\nFinished!\n")
print("\r----\n")
