import input
import files
import calc_var
import plot

# Print title
print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

if input.write_data == 1:
    # Write data files
    files.write_data_files()

if input.import_data == 1:
    # Read data files
    reduced_data1 = files.read_disp_speed(input.data_file1)
    reduced_data2 = files.read_lambda(input.data_file1)
    # plot_data = files.read_plot_data(input.data_file1)

    # Assign variables
    c_half = reduced_data1[0]
    s_d = reduced_data1[1]
    lambda1 = reduced_data2[0]
    lambda2 = reduced_data2[1]
    lambda3 = reduced_data2[2]

else:
    # Calculate variables
    var = calc_var.calculate_variables(input.data_file1_path,
                                       input.data_file2_path)

    # Assign variables
    c_half = var[0]
    s_d = var[1]
    lambda1 = var[2]
    lambda2 = var[3]
    lambda3 = var[4]

    # Calculate PDF values
    pdf = calc_var.calculate_pdf(c_half, s_d, lambda1, lambda2, lambda3)

    # Assign variables
    s_d_pdf = pdf[0]
    s_d_bin_pdf = pdf[1]
    lambda1_pdf = pdf[2]
    lambda1_bin_pdf = pdf[3]
    lambda2_pdf = pdf[4]
    lambda2_bin_pdf = pdf[5]
    lambda3_pdf = pdf[6]
    lambda3_bin_pdf = pdf[7]

    # # Calculate plot data
    # plot_data = calc_var.calculate_plot_data(lambda1, lambda2, lambda3,
    #                                          c_half, s_d)

# # Plot graphs
# plot.plot_all(c_half, s_d, plot_data[0], plot_data[1], plot_data[2],
#               plot_data[3], plot_data[4], plot_data[5], plot_data[6],
#               plot_data[7], plot_data[8], plot_data[9], plot_data[10],
#               plot_data[11], plot_data[12], plot_data[13], plot_data[14])

# Print finish
print("\nFinished!")
print("\r----\n")
