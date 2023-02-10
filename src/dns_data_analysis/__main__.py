import input
import files


def main():
    print("\nDNS Data Analysis")
    print("\r----\n")

    print(f"Flame: {input.flame}")
    print(f"Position: {input.position}\n")

    if input.write_reduced_data:
        print("Writing reduced data...\n")
        files.write_reduced_data()

    if input.write_plot_data:
        print("Writing plot data...\n")
        files.write_plot_data()

    print("\nFinished!")
    print("\r----\n")


if __name__ == "__main__":
    main()
