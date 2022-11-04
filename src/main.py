import input
import plot
import files
import reduced_data
import calc_var

import strain_rate

# Print title
print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

if input.write_data == 1:
    # Write reduced data files
    reduced_data.write_reduced_data_files()

if input.import_data == 1:
    # Read reduced data files
    c_half, s_d = files.read_disp_speed(input.data_file1)
    lambda1, lambda2, lambda3 = files.read_lambda(input.data_file1)

else:
    # Calculate data
    c_half, s_d, lambda1, lambda2, lambda3 = calc_var.calculate_variables(
        input.data_file1_path, input.data_file2_path)

# Calculate strain rate tensor joint probability density function
lambda_jpdf = strain_rate.calc_strain_rate_jpdf(lambda1, lambda2,
                                                lambda3, c_half,
                                                s_d)

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
print("\nFinished!")
print("\r----\n")
