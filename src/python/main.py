import files
import config as config


def main():
    print("\nDNS Data Analysis")
    print("\r----\n")

    print(f"Flame: {config.flame}")
    print(f"Position: {config.position}\n")

    if config.write_reduced_data:
        print("Writing reduced data...\n")
        files.write_reduced_data()

    if config.write_plot_data:
        print("Writing plot data...\n")
        files.write_plot_data()

    print("\nFinished!")
    print("\r----\n")


if __name__ == "__main__":
    main()
