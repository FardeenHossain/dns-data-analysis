import os
import input
import files
import calc_var


def write_reduced_data_files():
    """
    Writes reduced data files storing progress variable, displacement speed,
    and strain rate tensor eigenvalues.
    """

    # List of data files
    data_files = files.list_data_files()
    data_files1 = data_files[0]
    data_files2 = data_files[1]

    for i in range(0, len(data_files1)):
        # Print current data file
        data_file = data_files1[i]
        print('\nCalculating: %s ' % data_file)
        print('\r----\n')

        # Set data file path
        data_file1_path = os.path.join(input.in_path, data_files1[i])
        data_file2_path = os.path.join(input.in_path, data_files2[i])

        # Calculate data
        c_half, s_d, lambda1, lambda2, lambda3, rr1, rr2, rr3 \
            = calc_var.calculate_variables(data_file1_path, data_file2_path)

        # Write reduced data file
        print('\nWriting file...')
        files.write_disp_speed(data_file, c_half, s_d)
        files.write_lambda(data_file, lambda1, lambda2, lambda3, rr1, rr2, rr3)
