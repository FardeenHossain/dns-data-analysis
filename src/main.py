import input
import plot
import prog_var
import disp_speed
import strain_rate_tensor

# Print title
print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

# Calculate U
u_half = prog_var.calc_u(input.data_file1,
                         input.data_file2,
                         input.nx,
                         input.ny,
                         input.nz,
                         input.ix_start,
                         input.iy_start,
                         input.iz_start,
                         input.ix_end,
                         input.iy_end,
                         input.iz_end)

# Calculate V
v_half = prog_var.calc_v(input.data_file1,
                         input.data_file2,
                         input.nx,
                         input.ny,
                         input.nz,
                         input.ix_start,
                         input.iy_start,
                         input.iz_start,
                         input.ix_end,
                         input.iy_end,
                         input.iz_end)

# Calculate W
w_half = prog_var.calc_w(input.data_file1,
                         input.data_file2,
                         input.nx,
                         input.ny,
                         input.nz,
                         input.ix_start,
                         input.iy_start,
                         input.iz_start,
                         input.ix_end,
                         input.iy_end,
                         input.iz_end)

# Calculate progress variable
prog_var = prog_var.calc_prog_var(input.data_file1,
                                  input.data_file2,
                                  input.nx,
                                  input.ny,
                                  input.nz,
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

plot.plot_prog_var(c_half)

# # Calculate displacement speed
# print('Calculating displacement speed...')
# disp_speed = disp_speed.calc_disp_speed(input.nx_c,
#                                         input.ny_c,
#                                         input.nz_c,
#                                         u_half,
#                                         v_half,
#                                         w_half,
#                                         c_half,
#                                         input.dx,
#                                         dc)

# # Calculate strain rate tensor eigenvalues
# print('Calculating strain rate tensor eigenvalues...')
# lambda_eig = strain_rate_tensor.calc_strain_rate_tensor_eig(input.if_save,
#                                                             input.nx_c,
#                                                             input.ny_c,
#                                                             input.nz_c,
#                                                             input.dx,
#                                                             u_half,
#                                                             v_half,
#                                                             w_half,
#                                                             c_half,
#                                                             disp_speed)

# # Plot displacement speed
# plot.plot_disp_speed(disp_speed)

# # Plot displacement speed probability density function
# plot.plot_disp_speed_pdf(lambda_eig[1], lambda_eig[2])
#
# # Plot compressive strain rate tensor joint probability density function
# plot.plot_comp_strain_tensor_jpdf(lambda_eig[4], lambda_eig[5],
#                                   lambda_eig[6], lambda_eig[7],
#                                   lambda_eig[3])
#
# # Plot intermediate strain rate tensor joint probability density function
# plot.plot_int_strain_tensor_jpdf(lambda_eig[8], lambda_eig[9],
#                                  lambda_eig[10], lambda_eig[11],
#                                  lambda_eig[3])
#
# # Plot extensive strain rate tensor joint probability density function
# plot.plot_ext_strain_tensor_jpdf(lambda_eig[12], lambda_eig[13],
#                                  lambda_eig[14], lambda_eig[15],
#                                  lambda_eig[3])

# Print finish
print("\nFinished!\n")
print("\r----\n")
