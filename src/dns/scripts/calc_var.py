import prog_var
import disp_speed
import strain_rate

from input import ix_start, iy_start, iz_start, ix_end, iy_end, iz_end


def calculate_variables(data_file1_path, data_file2_path):
    # Calculate U
    u_half = prog_var.calc_u(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    # Calculate V
    v_half = prog_var.calc_v(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    # Calculate W
    w_half = prog_var.calc_w(data_file1_path, data_file2_path, ix_start,
                             iy_start, iz_start, ix_end, iy_end, iz_end)

    # Calculate progress variable
    c = prog_var.calc_prog_var(data_file1_path, data_file2_path, ix_start,
                               iy_start, iz_start, ix_end, iy_end, iz_end)

    c_half = c[0]
    dc = c[1]

    # Calculate displacement speed
    s_d = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

    # Calculate strain rate tensor eigenvalues
    lambda_eig = strain_rate.calc_strain_rate_eig(u_half, v_half, w_half)

    lambda1 = lambda_eig[0]
    lambda2 = lambda_eig[1]
    lambda3 = lambda_eig[2]

    rr1 = lambda_eig[3]
    rr2 = lambda_eig[4]
    rr3 = lambda_eig[5]

    return [c_half, s_d, lambda1, lambda2, lambda3, rr1, rr2, rr3]
