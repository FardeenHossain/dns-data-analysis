import input
import files
import calc_var

print("\nDNS Data Analysis")
print("\r----\n")

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

print("\nFinished!")
print("\r----\n")
