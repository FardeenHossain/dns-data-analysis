import input
import files
import calc_var
import matplotlib.pyplot as plt

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

plt.plot(s_d_pdf_bin, s_d_pdf[0, :])
plt.ylabel('Probability Density Function, PDF')
plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
plt.xlim(-15, 15)
plt.ylim(0.0, 0.1)
plt.show()

plt.plot(lambda1_pdf_bin, lambda1_pdf_bin[0, :])
plt.ylabel('Probability Density Function, PDF')
plt.xlabel(r'Compressive Strain Rate Tensor, $\rm\gamma$')
plt.xlim(-5e5, 5e5)
plt.ylim(0.0, 2e-5)
plt.show()

plt.contourf(lambda1_jpdf_bin_y, lambda1_jpdf_bin_x, lambda1_jpdf,
             cmap='inferno')
plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
plt.ylabel(r'Compressive Strain Rate Tensor, $\rm\gamma$')
plt.colorbar(label='Joint Probability Density Function, JPDF')
plt.legend(loc='upper right', labelcolor='white')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.xlim(-15, 15)
plt.ylim(-1.5e5, 1.5e5)
plt.show()

print("\nFinished!")
print("\r----\n")
