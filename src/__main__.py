import input
import files
import calc_var
import strain_rate

print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

if input.write_data == 1:
    files.write_data_files()

if input.import_data == 1:
    # Import reduced data
    [c_half, s_d] = files.read_disp_speed(input.data_file1)
    [lambda1, lambda2, lambda3] = files.read_lambda(input.data_file1)

else:
    # Calculate data
    [c_half, s_d, lambda1, lambda2, lambda3] = calc_var.calculate_variables(
        input.data_file1_path, input.data_file2_path)

# TEST FUNCTION

# Calculate PDF values
lambda_pdf = strain_rate.calc_strain_rate_pdf(c_half, lambda1, lambda2,
                                              lambda3)

# Assign variables
lambda1_pdf = lambda_pdf[0]
lambda1_pdf_bin = lambda_pdf[1]
lambda2_pdf = lambda_pdf[2]
lambda2_pdf_bin = lambda_pdf[3]
lambda3_pdf = lambda_pdf[4]
lambda3_pdf_bin = lambda_pdf[5]

# Set file path
data_file = input.data_file1
data_file = data_file.replace(".h5", "")

file_path = "./data/%s/%s_plot.txt" % (input.flame, data_file)
file = open(file_path, "w+")

file.write("lambda_1_pdf lambda1_pdf_bin\n")

# Write data
for i in range(0, len(lambda1_pdf[:, 0])):
    for j in range(0, len(lambda1_pdf[0, :])):
        file.write("%d %d\n" % (lambda1_pdf[i, j], lambda1_pdf_bin[j]))

file.close()

print("Saved strain rate tensor PDF!")

print("\nFinished!")
print("\r----\n")
