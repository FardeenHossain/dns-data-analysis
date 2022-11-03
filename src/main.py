import input
import plot
import prog_var
import disp_speed
import strain_rate

# Print title
print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

# Calculate U
u_half = prog_var.calc_u(input.data_file1_path, input.data_file2_path,
                         input.ix_start, input.iy_start, input.iz_start,
                         input.ix_end, input.iy_end, input.iz_end)

# Calculate V
v_half = prog_var.calc_v(input.data_file1_path, input.data_file2_path,
                         input.ix_start, input.iy_start, input.iz_start,
                         input.ix_end, input.iy_end, input.iz_end)

# Calculate W
w_half = prog_var.calc_w(input.data_file1_path, input.data_file2_path,
                         input.ix_start, input.iy_start, input.iz_start,
                         input.ix_end, input.iy_end, input.iz_end)

# Calculate progress variable
c = prog_var.calc_prog_var(input.data_file1_path, input.data_file2_path,
                           input.ix_start, input.iy_start,
                           input.iz_start, input.ix_end,
                           input.iy_end, input.iz_end)

c_half = c[0]
dc = c[1]

# Calculate displacement speed
print('Calculating displacement speed...')
s_d = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

# Calculate strain rate tensor eigenvalues
print('Calculating strain rate tensor eigenvalues...')
lambda_eig = strain_rate.calc_strain_rate_eig(input.if_save, u_half,
                                              v_half, w_half)

lambda1 = lambda_eig[0]
lambda2 = lambda_eig[1]
lambda3 = lambda_eig[2]

rr1 = lambda_eig[3]
rr2 = lambda_eig[4]
rr3 = lambda_eig[5]

# Calculate strain rate tensor joint probability density function
lambda_jpdf = strain_rate.calc_strain_rate_jpdf(lambda1, lambda2,
                                                lambda3, c_half,
                                                disp_speed)

# Plot progress variable
plot.plot_prog_var(c_half)

# Plot displacement speed
plot.plot_disp_speed(s_d)

# Plot displacement speed probability density function
plot.plot_disp_speed_pdf(lambda_jpdf[0], lambda_jpdf[1])

# Plot compressive strain rate tensor joint probability density function
plot.plot_comp_strain_tensor_jpdf(lambda_jpdf[3], lambda_jpdf[4],
                                  lambda_jpdf[5], lambda_jpdf[6],
                                  lambda_jpdf[2])

# Plot intermediate strain rate tensor joint probability density function
plot.plot_int_strain_tensor_jpdf(lambda_jpdf[7], lambda_jpdf[8],
                                 lambda_jpdf[9], lambda_jpdf[10],
                                 lambda_jpdf[2])

# Plot extensive strain rate tensor joint probability density function
plot.plot_ext_strain_tensor_jpdf(lambda_jpdf[11], lambda_jpdf[12],
                                 lambda_jpdf[13], lambda_jpdf[14],
                                 lambda_jpdf[2])

# Print finish
print("\nFinished!\n")
print("\r----\n")
