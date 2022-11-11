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
    [lambda1, lambda2, lambda3] = files.read_lambda(input.data_file1)

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

print("Saved strain rate tensor PDF!")

print("\nFinished!")
print("\r----\n")
