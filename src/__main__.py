import input
import files
import calc_var

print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

if input.write_data == 1:
    files.write_data_files()

if input.import_data == 1:
    reduced_data1 = files.read_disp_speed(input.data_file1)
    reduced_data2 = files.read_lambda(input.data_file1)

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

print("\nFinished!")
print("\r----\n")
