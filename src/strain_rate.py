import numpy as np

from input import nx_c, ny_c, nz_c, dx, data_file1

import files
import mystat
import myeig


def calc_strain_rate_eig(if_save, u_half, v_half, w_half):
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

    if if_save == 1:
        # Calculate eigenvalues
        lambda_eig = myeig.vec_val(center_u[:, :, :], center_v[:, :, :],
                                   center_w[:, :, :], dx)

    else:
        # Import eigenvalues
        lambda_eig = files.read_lambda(data_file1)

    lambda1 = lambda_eig[0]
    lambda2 = lambda_eig[1]
    lambda3 = lambda_eig[2]

    rr1 = lambda_eig[3]
    rr2 = lambda_eig[4]
    rr3 = lambda_eig[5]

    return [lambda1, lambda2, lambda3, rr1, rr2, rr3]


def calc_strain_rate_jpdf(lambda1, lambda2, lambda3, c_half, disp_speed):
    """Calculate strain rate tensor eigenvalues."""

    # Condition
    cond = np.absolute(c_half - 0.73) < (0.2 / 2.0)

    disp_speed_cond = np.extract(cond, disp_speed)
    lambda1_cond = np.extract(cond, lambda1)
    lambda2_cond = np.extract(cond, lambda2)
    lambda3_cond = np.extract(cond, lambda3)

    disp_speed_cond_flat = np.ndarray.flatten(disp_speed_cond)
    lambda1_cond_flat = np.ndarray.flatten(lambda1_cond)
    lambda2_cond_flat = np.ndarray.flatten(lambda2_cond)
    lambda3_cond_flat = np.ndarray.flatten(lambda3_cond)

    # Bin spacing
    bin_edges_jpdf_lam = np.linspace(-15e4, 15e4, 60)
    bin_edges_jpdf_disp_speed_c = np.linspace(-15, 15, 60)

    # Compressive strain tensor
    lambda1_disp_speed_c_jpdf, lambda1_bin_edges, disp_bin_edges = \
        np.histogram2d(lambda1_cond_flat, disp_speed_cond_flat, bins=(
            bin_edges_jpdf_lam, bin_edges_jpdf_disp_speed_c), density=True)

    lambda1_jpdf_bin = 0.5 * (lambda1_bin_edges[:-1] + lambda1_bin_edges[1:])
    disp1_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    # Intermediate strain tensor
    lambda2_disp_speed_c_jpdf, lambda2_bin_edges, disp_bin_edges = \
        np.histogram2d(lambda2_cond_flat, disp_speed_cond_flat, bins=(
            bin_edges_jpdf_lam, bin_edges_jpdf_disp_speed_c), density=True)

    lambda2_jpdf_bin = 0.5 * (lambda2_bin_edges[:-1] + lambda2_bin_edges[1:])
    disp2_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    # Extensive strain tensor
    lambda3_disp_speed_c_jpdf, lambda3_bin_edges, disp_bin_edges = \
        np.histogram2d(lambda3_cond_flat, disp_speed_cond_flat, bins=(
            bin_edges_jpdf_lam, bin_edges_jpdf_disp_speed_c), density=True)

    lambda3_jpdf_bin = 0.5 * (lambda3_bin_edges[:-1] + lambda3_bin_edges[1:])
    disp3_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    # Bin spacing
    bin_edges_pdf = np.linspace(-1e2, 1e2, 60)
    bin_c_cond = np.linspace(0.725, 0.735, 1)
    d_bin_c_cond = 0.01

    [pdf_disp_speed_cond, bin_pdf_disp_speed_cond] = mystat.cond_pdf(
        disp_speed[:, :, :],
        c_half[:, :, :], bin_edges_pdf, bin_c_cond, d_bin_c_cond)

    bin_edges_pdf_lambda = np.linspace(-1e6, 1e6, 400)
    [pdf_lambda1_cond, bin_pdf_lambda1_cond] = mystat.cond_pdf(
        lambda1[:, :, :], c_half[:, :, :], bin_edges_pdf_lambda, bin_c_cond,
        d_bin_c_cond)

    bin_disp_speed = np.linspace(-9, 14, 20)
    d_bin_disp_speed = 1 / 20

    nc = len(bin_disp_speed)

    lambda1_cond_mean = np.zeros([nc])
    lambda2_cond_mean = np.zeros([nc])
    lambda3_cond_mean = np.zeros([nc])

    for i in range(0, nc):
        cond = np.absolute(disp_speed_cond_flat -
                           bin_disp_speed[i]) < d_bin_disp_speed / 2.0

        ext = np.extract(cond, lambda1_cond_flat)
        mean = np.mean(ext)
        lambda1_cond_mean[i] = mean

        ext = np.extract(cond, lambda2_cond_flat)
        mean = np.mean(ext)
        lambda2_cond_mean[i] = mean

        ext = np.extract(cond, lambda3_cond_flat)
        mean = np.mean(ext)
        lambda3_cond_mean[i] = mean

    return [pdf_disp_speed_cond,
            bin_pdf_disp_speed_cond,
            bin_disp_speed,
            lambda1_jpdf_bin,
            lambda1_disp_speed_c_jpdf,
            lambda1_cond_mean,
            disp1_jpdf_bin,
            lambda2_jpdf_bin,
            lambda2_disp_speed_c_jpdf,
            lambda2_cond_mean,
            disp2_jpdf_bin,
            lambda3_jpdf_bin,
            lambda3_disp_speed_c_jpdf,
            lambda3_cond_mean,
            disp3_jpdf_bin]
