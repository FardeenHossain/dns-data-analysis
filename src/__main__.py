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
    plot_data = files.read_plot_data(input.data_file1)

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

    plot_data = calc_var.calculate_plot_data(lambda1, lambda2, lambda3,
                                             c_half, s_d)

# Plot graphs
plot.plot_all(c_half, s_d, plot_data[0], plot_data[1], plot_data[2],
              plot_data[3], plot_data[4], plot_data[5], plot_data[6],
              plot_data[7], plot_data[8], plot_data[9], plot_data[10],
              plot_data[11], plot_data[12], plot_data[13], plot_data[14])

# Print finish
print("\nFinished!")
print("\r----\n")
