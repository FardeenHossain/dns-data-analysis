import input
import files

print("\nDNS Data Analysis")
print("\r----\n")

if input.write_reduced_data == 1:
    print("Writing reduced data...")
    files.write_reduced_data()

if input.write_plot_data == 1:
    print("Writing plot data...")
    files.write_plot_data()

if input.write_reduced_data == 0 & input.write_plot_data == 0:
    print("No input arguments!")

print("\nFinished!")
print("\r----\n")
