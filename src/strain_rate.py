import numpy as np
import utils

from input import nx_c, ny_c, nz_c, dx


def calc_strain_rate_eig(u_half, v_half, w_half):
    """Calculate strain rate tensor eigenvalues."""

    # Prefill arrays with zeroes
    center_u = np.zeros([nx_c, ny_c, nz_c])
    center_v = np.zeros([nx_c, ny_c, nz_c])
    center_w = np.zeros([nx_c, ny_c, nz_c])

    # Compute vorticity
    for i in range(0, nx_c):
        for j in range(0, ny_c):
            for k in range(0, nz_c):
                center_u[i, j, k] = (u_half[i + 1, j, k] + u_half[i, j, k]) / 2
                center_v[i, j, k] = (v_half[i, j + 1, k] + v_half[i, j, k]) / 2
                center_w[i, j, k] = (w_half[i, j, k + 1] + w_half[i, j, k]) / 2

    # Calculate eigenvalues
    [lambda1, lambda2, lambda3, rr1, rr2, rr3] = utils.vec_val(
        center_u[:, :, :], center_v[:, :, :], center_w[:, :, :], dx)

    print("Finished strain rate tensor eigenvalues!")

    return [lambda1, lambda2, lambda3, rr1, rr2, rr3]


def calc_disp_speed_pdf(c_half, s_d):
    """Calculate displacement speed probability density function."""

    # Bin spacing
    bin_edges_pdf = np.linspace(-1e2, 1e2, 100)
    bin_c_cond = np.linspace(0.1, 0.9, 5)
    d_bin_c_cond = 0.01

    # Calculate displacement speed PDF
    s_d_pdf, s_d_bin_pdf = utils.cond_pdf(s_d, c_half, bin_edges_pdf,
                                          bin_c_cond, d_bin_c_cond)

    print("Finished displacement speed PDF!")

    return [s_d_pdf, s_d_bin_pdf]


def calc_strain_rate_pdf(c_half, lambda1, lambda2, lambda3):
    """Calculate strain rate tensor eigenvalues probability density
    function."""

    # Bin spacing
    bin_edges_pdf = np.linspace(-1e6, 1e6, 100)
    bin_c_cond = np.linspace(0.1, 0.9, 5)
    d_bin_c_cond = 0.01

    # Calculate compressive strain rate tensor PDF
    lambda1_pdf, lambda1_pdf_bin = utils.cond_pdf(lambda1, c_half,
                                                  bin_edges_pdf,
                                                  bin_c_cond,
                                                  d_bin_c_cond)

    # Calculate intermediate strain rate tensor PDF
    lambda2_pdf, lambda2_pdf_bin = utils.cond_pdf(lambda2, c_half,
                                                  bin_edges_pdf,
                                                  bin_c_cond,
                                                  d_bin_c_cond)

    # Calculate extensive strain rate tensor PDF
    lambda3_pdf, lambda3_pdf_bin = utils.cond_pdf(lambda3, c_half,
                                                  bin_edges_pdf,
                                                  bin_c_cond,
                                                  d_bin_c_cond)

    print("Finished strain rate tensor PDF!")

    return [lambda1_pdf, lambda1_pdf_bin, lambda2_pdf, lambda2_pdf_bin,
            lambda3_pdf, lambda3_pdf_bin]


def calc_strain_rate_jpdf(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate strain rate tensor eigenvalues joint probability density
    function."""

    # Bin spacing
    lambda_bin_edges_pdf = np.linspace(-1.5e5, 1.5e5, 100)
    s_d_bin_edges_pdf = np.linspace(-15, 15, 100)
    bin_c_cond = np.linspace(0.1, 0.9, 5)
    d_bin_c_cond = 0.2

    # Calculate compressive strain rate tensor PDF
    [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y] = utils.cond_pdf2d(
        lambda1, s_d, c_half, lambda_bin_edges_pdf, s_d_bin_edges_pdf,
        bin_c_cond, d_bin_c_cond)

    # Calculate intermediate strain rate tensor PDF
    [lambda2_jpdf, lambda2_jpdf_bin_x, lambda2_jpdf_bin_y] = utils.cond_pdf2d(
        lambda2, s_d, c_half, lambda_bin_edges_pdf, s_d_bin_edges_pdf,
        bin_c_cond, d_bin_c_cond)

    # Calculate extensive strain rate tensor PDF
    [lambda3_jpdf, lambda3_jpdf_bin_x, lambda3_jpdf_bin_y] = utils.cond_pdf2d(
        lambda3, s_d, c_half, lambda_bin_edges_pdf, s_d_bin_edges_pdf,
        bin_c_cond, d_bin_c_cond)

    print("Finished strain rate tensor JPDF!")

    return [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, lambda2_jpdf,
            lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, lambda3_jpdf,
            lambda3_jpdf_bin_x, lambda3_jpdf_bin_y]
