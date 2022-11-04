import input
import files
import calc_var
import plot
import strain_rate

# Print title
print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

if input.write_data == 1:
    # Write reduced data files
    files.write_reduced_data_files()

if input.import_data == 1:
    # Read reduced data files
    reduced_data1 = files.read_disp_speed(input.data_file1)
    reduced_data2 = files.read_lambda(input.data_file1)

    c_half = reduced_data1[0]
    s_d = reduced_data1[1]

    lambda1 = reduced_data2[0]
    lambda2 = reduced_data2[1]
    lambda3 = reduced_data2[2]

else:
    # Calculate data
    data = calc_var.calculate_variables(input.data_file1_path,
                                        input.data_file2_path)

    c_half = data[0]
    s_d = data[1]

    lambda1 = data[2]
    lambda2 = data[3]
    lambda3 = data[4]

# Calculate strain rate tensor joint probability density function
lambda_jpdf = strain_rate.calc_strain_rate_jpdf(lambda1, lambda2, lambda3,
                                                c_half, s_d)

# Plot graphs
plot.plot_all(c_half, s_d, lambda_jpdf[0], lambda_jpdf[1], lambda_jpdf[2],
              lambda_jpdf[3], lambda_jpdf[4], lambda_jpdf[5], lambda_jpdf[6],
              lambda_jpdf[7], lambda_jpdf[8], lambda_jpdf[9], lambda_jpdf[10],
              lambda_jpdf[11], lambda_jpdf[12], lambda_jpdf[13],
              lambda_jpdf[14])

# Print finish
print("\nFinished!")
print("\r----\n")
