import input
import files

print("\nDNS Data Analysis")
print("\r----\n")

if input.write_reduced_data == 1:
    print("\nWriting reduced data...")
    print("\r----\n")
    files.write_reduced_data()

if input.write_plot_data == 1:
    print("\nWriting plot data...")
    print("\r----\n")
    files.write_plot_data()

if input.write_reduced_data == 0 & input.write_plot_data == 0:
    print("No input arguments!")

print("\nFinished!")
print("\r----\n")
