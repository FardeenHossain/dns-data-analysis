import prog_var
import disp_speed
import strain_rate

from input import ix_start, iy_start, iz_start, ix_end, iy_end, iz_end


def calculate_variables(data_file1_path, data_file2_path):
    """ Calculate displacement speed and strain rate tensor eigenvalues."""

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

    # Assign variables
    lambda1 = lambda_eig[0]
    lambda2 = lambda_eig[1]
    lambda3 = lambda_eig[2]
    rr1 = lambda_eig[3]
    rr2 = lambda_eig[4]
    rr3 = lambda_eig[5]

    return [c_half, s_d, lambda1, lambda2, lambda3, rr1, rr2, rr3]


def calculate_pdf(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate displacement speed and strain rate tensor eigenvalues
    probability density function."""

    # Calculate displacement speed PDF
    s_d_pdf, s_d_bin_pdf = strain_rate.calc_disp_speed_pdf(c_half, s_d)

    # Calculate lambda PDF
    lambda_pdf = strain_rate.calc_strain_rate_pdf(c_half, s_d, lambda1,
                                                  lambda2, lambda3)

    # Assign variables
    lambda1_pdf = lambda_pdf[0]
    lambda1_bin_pdf = lambda_pdf[1]
    lambda2_pdf = lambda_pdf[2]
    lambda2_bin_pdf = lambda_pdf[3]
    lambda3_pdf = lambda_pdf[4]
    lambda3_bin_pdf = lambda_pdf[5]

    return [s_d_pdf, s_d_bin_pdf, lambda1_pdf, lambda1_bin_pdf, lambda2_pdf,
            lambda2_bin_pdf, lambda3_pdf, lambda3_bin_pdf]


# def calculate_plot_data(lambda1, lambda2, lambda3, c_half, s_d):
#     """Calculate joint probability density function plot data."""
#
#     plot_data = strain_rate.calc_strain_rate_jpdf(lambda1, lambda2, lambda3,
#                                                   c_half, s_d)
#
#     return (plot_data[0], plot_data[1], plot_data[2], plot_data[3],
#             plot_data[4], plot_data[5], plot_data[6], plot_data[7],
#             plot_data[8], plot_data[9], plot_data[10], plot_data[11],
#             plot_data[12], plot_data[13], plot_data[14])
