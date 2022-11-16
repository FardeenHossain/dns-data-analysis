import input
import files
import calc_var

print("\nDNS Data Analysis")
print("\r----\n")

if input.write_reduced_data == 1:
    files.write_reduced_data()

if input.write_plot_data == 1:
    [c_half, s_d, lambda1, lambda2, lambda3] = files.read_reduced_data()


print("\nFinished!")
print("\r----\n")
