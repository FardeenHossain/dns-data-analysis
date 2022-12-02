import prog_var
import disp_speed
import strain_rate
import pdf

from input import ix_start, iy_start, iz_start, ix_end, iy_end, iz_end


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

    # Calculate progress variable
    [c_half, dc] = prog_var.calc_prog_var(data_file1_path, data_file2_path,
                                          ix_start, iy_start, iz_start, ix_end,
                                          iy_end, iz_end)

    # Calculate displacement speed
    s_d = disp_speed.calc_disp_speed(u_half, v_half, w_half, c_half, dc)

    # Calculate strain rate tensor eigenvalues
    [lambda1, lambda2, lambda3, rr1, rr2,
     rr3] = strain_rate.calc_strain_rate_eig(u_half, v_half, w_half)

    return [c_half, s_d, lambda1, lambda2, lambda3, rr1, rr2, rr3]


def calc_pdf(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate displacement speed and strain rate tensor eigenvalues
    probability density function."""

    # Calculate displacement speed PDF
    [s_d_pdf, s_d_pdf_bin] = pdf.calc_disp_speed_pdf(c_half, s_d)

    # Calculate lambda PDF
    [lambda1_pdf, lambda1_pdf_bin, lambda2_pdf, lambda2_pdf_bin, lambda3_pdf,
     lambda3_pdf_bin] = pdf.calc_strain_rate_pdf(c_half, lambda1, lambda2,
                                                 lambda3)

    return [s_d_pdf, s_d_pdf_bin, lambda1_pdf, lambda1_pdf_bin, lambda2_pdf,
            lambda2_pdf_bin, lambda3_pdf, lambda3_pdf_bin]


def calc_jpdf(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate strain rate tensor eigenvalues joint probability density
     function."""

    # Calculate lambda JPDF
    [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, lambda2_jpdf,
     lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, lambda3_jpdf, lambda3_jpdf_bin_x,
     lambda3_jpdf_bin_y] = pdf.calc_strain_rate_jpdf(
        c_half, s_d, lambda1, lambda2, lambda3)

    return [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, lambda2_jpdf,
            lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, lambda3_jpdf,
            lambda3_jpdf_bin_x, lambda3_jpdf_bin_y]


def calc_cond_mean(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate conditional mean."""

    # Calculate conditional mean
    [bin_s_d, lambda1_cond_mean, lambda2_cond_mean,
     lambda3_cond_mean] = pdf.calc_cond_mean(c_half, s_d, lambda1, lambda2,
                                             lambda3)

    return [bin_s_d, lambda1_cond_mean, lambda2_cond_mean, lambda3_cond_mean]
