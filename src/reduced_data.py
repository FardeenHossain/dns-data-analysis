import os
import input
import prog_var
import disp_speed
import strain_rate
import files


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

        # Calculate U
        u_half = prog_var.calc_u(data_file1_path, data_file2_path,
                                 input.ix_start, input.iy_start,
                                 input.iz_start, input.ix_end, input.iy_end,
                                 input.iz_end)

        # Calculate V
        v_half = prog_var.calc_v(data_file1_path, data_file2_path,
                                 input.ix_start, input.iy_start,
                                 input.iz_start, input.ix_end, input.iy_end,
                                 input.iz_end)

        # Calculate W
        w_half = prog_var.calc_w(data_file1_path, data_file2_path,
                                 input.ix_start, input.iy_start,
                                 input.iz_start, input.ix_end, input.iy_end,
                                 input.iz_end)

        # Calculate progress variable
        c = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                   input.ix_start, input.iy_start,
                                   input.iz_start, input.ix_end,
                                   input.iy_end, input.iz_end)

        c_half = c[0]
        dc = c[1]

        # Calculate displacement speed
        s_d = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

        # Calculate strain rate tensor eigenvalues
        lambda_eig = strain_rate.calc_strain_rate_eig(input.if_save, u_half,
                                                      v_half, w_half)

        lambda1 = lambda_eig[0]
        lambda2 = lambda_eig[1]
        lambda3 = lambda_eig[2]

        rr1 = lambda_eig[3]
        rr2 = lambda_eig[4]
        rr3 = lambda_eig[5]

        # Write reduced data file
        files.write_disp_speed(data_file, c_half, s_d)
        files.write_lambda(data_file, lambda1, lambda2, lambda3, rr1, rr2, rr3)

        # Print finish
        print("\nFinished!")
        print("\r----\n")


write_reduced_data_files()
