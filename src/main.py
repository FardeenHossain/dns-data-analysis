import input
import plot
import disp_speed

# Print title
print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

# Calculate displacement speed
print('\nCalculating displacement speed...')
disp_speed = disp_speed.calc_disp_speed(input.in_path,
                                        input.ix_start,
                                        input.iy_start,
                                        input.iz_start,
                                        input.ix_end,
                                        input.iy_end,
                                        input.iz_end,
                                        input.Nx,
                                        input.Ny,
                                        input.Nz,
                                        input.Nx_c,
                                        input.Ny_c,
                                        input.Nz_c)

# Plot displacement speed
print('\nPlotting displacement speed...')
plot.plot_disp_speed(disp_speed)

# Print finish
print("\nFinished!\n")
print("\n----\n")
