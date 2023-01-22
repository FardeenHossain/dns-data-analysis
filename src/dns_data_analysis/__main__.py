import input
import files
import plot

print("\nDNS Data Analysis")
print("\r----\n")

print(f"Flame: {input.flame}")
print(f"Position: {input.position}\n")


def main():
    if input.write_reduced_data:
        print("Writing reduced data...\n")
        files.write_reduced_data()

    if input.write_plot_data:
        print("Writing plot data...\n")
        files.write_plot_data()

    if input.plot_flame:
        print("Plotting flame...\n")
        plot.plot_flame()


if input.flames_all:
    for i in input.flames:
        for j in input.positions:
            input.flame = input.flames[i]
            input.position = input.positions[j]
            main()
else:
    main()

print("\nFinished!")
print("\r----\n")
