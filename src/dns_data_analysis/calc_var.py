import curvature
import disp_speed
import pdf
import prog_var
import strain_rate
from input import ix_start, iy_start, iz_start, ix_end, iy_end, iz_end, dx


def calc_data(data_file1_path, data_file2_path):
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

    # Calculate density
    rho_half = prog_var.calc_rho(data_file1_path, data_file2_path, ix_start,
                                 iy_start, iz_start, ix_end, iy_end, iz_end)

    # Calculate progress variable
    [c_half, dc] = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                          ix_start, iy_start, iz_start, ix_end,
                                          iy_end, iz_end)

    # Calculate displacement speed
    [s_d, mag_g_c] = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half,
                                                dc)

    # Calculate curvature
    k_m = curvature.mean_curv(c_half, dx)

    # Calculate strain rate tensor eigenvalues
    [lambda1, lambda2, lambda3, rr1, rr2,
     rr3] = strain_rate.calc_strain_rate_eig(u_half, v_half, w_half)

    return [c_half, s_d, lambda1, lambda2, lambda3, rr1, rr2, rr3, mag_g_c,
            rho_half, k_m]


def calc_pdf(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate probability density functions."""

    [s_d_pdf, s_d_pdf_bin] = pdf.calc_disp_speed_pdf(c_half, s_d)

    [lambda1_pdf, lambda1_pdf_bin, lambda2_pdf, lambda2_pdf_bin, lambda3_pdf,
     lambda3_pdf_bin] = pdf.calc_strain_rate_pdf(c_half, lambda1, lambda2,
                                                 lambda3)

    return [s_d_pdf, s_d_pdf_bin, lambda1_pdf, lambda1_pdf_bin, lambda2_pdf,
            lambda2_pdf_bin, lambda3_pdf, lambda3_pdf_bin]


def calc_jpdf(c_half, s_d, lambda1, lambda2, lambda3, k):
    """Calculate joint probability density functions."""

    [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, lambda2_jpdf,
     lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, lambda3_jpdf, lambda3_jpdf_bin_x,
     lambda3_jpdf_bin_y] = pdf.calc_strain_rate_jpdf(
        c_half, s_d, lambda1, lambda2, lambda3)

    [s_d_c_half_jpdf, s_d_c_half_jpdf_bin_x,
     s_d_c_half_jpdf_bin_y] = pdf.calc_disp_speed_prog_var_jpdf(c_half, s_d)

    [s_d_k_jpdf, s_d_k_jpdf_bin_x,
     s_d_k_jpdf_bin_y] = pdf.calc_disp_speed_curvature_jpdf(c_half, s_d, k)

    return [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, lambda2_jpdf,
            lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, lambda3_jpdf,
            lambda3_jpdf_bin_x, lambda3_jpdf_bin_y, s_d_c_half_jpdf,
            s_d_c_half_jpdf_bin_x, s_d_c_half_jpdf_bin_y, s_d_k_jpdf,
            s_d_k_jpdf_bin_x, s_d_k_jpdf_bin_y]


def calc_cond_mean(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate conditional means."""

    [bin_c, s_d_cond_mean] = pdf.calc_disp_speed_cond_mean(c_half, s_d)

    [bin_s_d, lambda1_cond_mean, lambda2_cond_mean,
     lambda3_cond_mean] = pdf.calc_lambda_c_cond_mean(c_half, s_d, lambda1,
                                                      lambda2,
                                                      lambda3)

    return [bin_c, s_d_cond_mean, bin_s_d, lambda1_cond_mean,
            lambda2_cond_mean, lambda3_cond_mean]
