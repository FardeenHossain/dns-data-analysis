import input
import files
import plot

print("\nDNS Data Analysis")
print("\r----\n")

if input.write_reduced_data == 1:
    print("Writing reduced data...\n")
    files.write_reduced_data()

if input.write_plot_data == 1:
    print("Writing plot data...\n")
    files.write_plot_data()

if input.plot_flame == 1:
    print("Plotting flame...\n")
    plot.plot_flame()

print("\nFinished!")
print("\r----\n")
