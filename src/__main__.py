import input
import files
import calc_var

print('\nDirect Numerical Simulation (DNS) Premixed')
print('\r----\n')

if input.write_data == 1:
    files.write_data_files()

if input.import_data == 1:
    # Import reduced data
    [c_half, s_d] = files.read_disp_speed(input.data_file1)
    [lambda1, lambda2, lambda3, rr1, rr2, rr3] = files.read_lambda(
        input.data_file1)

else:
    # Calculate data
    [c_half, s_d, lambda1, lambda2, lambda3] = calc_var.calculate_data(
        input.data_file1_path, input.data_file2_path)

# TEST FUNCTION
[s_d_pdf, s_d_pdf_bin, lambda1_pdf, lambda1_pdf_bin, lambda2_pdf,
 lambda2_pdf_bin, lambda3_pdf, lambda3_pdf_bin] = calc_var.calculate_pdf(
    c_half, s_d, lambda1, lambda2, lambda3)
files.write_pdf(input.data_file1, lambda1_pdf, lambda1_pdf_bin, lambda2_pdf,
                lambda2_pdf_bin, lambda3_pdf, lambda3_pdf_bin)

[lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, lambda2_jpdf,
 lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, lambda3_jpdf,
 lambda3_jpdf_bin_x, lambda3_jpdf_bin_y] = calc_var.calculate_jpdf(
    c_half, s_d, lambda1, lambda2, lambda3)

print(s_d_pdf)
print(lambda1_pdf)
print(lambda1_jpdf)

print("\nFinished!")
print("\r----\n")
