import input
import plot
import prog_var
import disp_speed

# Print title
print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

# Calculate U
u_half = prog_var.calc_u(input.data_file1,
                         input.data_file2,
                         input.Nx,
                         input.Ny,
                         input.Nz,
                         input.ix_start,
                         input.iy_start,
                         input.iz_start,
                         input.ix_end,
                         input.iy_end,
                         input.iz_end)

# Calculate V
v_half = prog_var.calc_v(input.data_file1,
                         input.data_file2,
                         input.Nx,
                         input.Ny,
                         input.Nz,
                         input.ix_start,
                         input.iy_start,
                         input.iz_start,
                         input.ix_end,
                         input.iy_end,
                         input.iz_end)

# Calculate W
w_half = prog_var.calc_w(input.data_file1,
                         input.data_file2,
                         input.Nx,
                         input.Ny,
                         input.Nz,
                         input.ix_start,
                         input.iy_start,
                         input.iz_start,
                         input.ix_end,
                         input.iy_end,
                         input.iz_end)

# Calculate progress variable
prog_var = prog_var.calc_prog_var(input.data_file1,
                                  input.data_file2,
                                  input.Nx,
                                  input.Ny,
                                  input.Nz,
                                  input.ix_start,
                                  input.iy_start,
                                  input.iz_start,
                                  input.ix_end,
                                  input.iy_end,
                                  input.iz_end,
                                  input.o2_u,
                                  input.o2_b,
                                  input.dt)

c_half = prog_var[0]
dc = prog_var[1]

# Calculate displacement speed
print('\nCalculating displacement speed...')
disp_speed = disp_speed.calc_disp_speed(input.Nx_c,
                                        input.Ny_c,
                                        input.Nz_c,
                                        u_half,
                                        v_half,
                                        w_half,
                                        c_half,
                                        input.dx,
                                        dc)

# Plot displacement speed
print('\nPlotting displacement speed...')
plot.plot_disp_speed(disp_speed)

# Print finish
print("\nFinished!\n")
print("\n----\n")
