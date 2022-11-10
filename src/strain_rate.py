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
    lambda_eig = utils.vec_val(center_u[:, :, :], center_v[:, :, :],
                               center_w[:, :, :], dx)

    # Assign variables
    lambda1 = lambda_eig[0]
    lambda2 = lambda_eig[1]
    lambda3 = lambda_eig[2]
    rr1 = lambda_eig[3]
    rr2 = lambda_eig[4]
    rr3 = lambda_eig[5]

    print('Finished strain rate tensor eigenvalues!')

    return [lambda1, lambda2, lambda3, rr1, rr2, rr3]


def calc_disp_speed_pdf(c_half, s_d):
    """Calculate displacement speed probability density function."""

    # Bin spacing
    bin_edges_pdf = np.linspace(-1e2, 1e2, 60)
    bin_c_cond = np.linspace(0.725, 0.735, 1)
    d_bin_c_cond = 0.01

    # Calculate displacement speed PDF
    s_d_pdf, s_d_bin_pdf = utils.cond_pdf(s_d, c_half, bin_edges_pdf,
                                          bin_c_cond, d_bin_c_cond)

    print('Finished displacement speed PDF!')

    return [s_d_pdf, s_d_bin_pdf]


def calc_strain_rate_pdf(c_half, s_d, lambda1, lambda2, lambda3):
    """
    Calculate strain rate tensor eigenvalues probability density function.
    """

    # Bin spacing
    bin_edges_pdf = np.linspace(-15e4, 15e4, 60)
    bin_c_cond = np.linspace(0.725, 0.735, 1)
    d_bin_c_cond = 0.01

    # Calculate compressive strain rate tensor PDF
    lambda1_pdf, lambda1_bin_pdf = utils.cond_pdf2d(lambda1, s_d, c_half,
                                                    bin_edges_pdf, bin_c_cond,
                                                    d_bin_c_cond)

    # Calculate intermediate strain rate tensor PDF
    lambda2_pdf, lambda2_bin_pdf = utils.cond_pdf2d(lambda2, s_d, c_half,
                                                    bin_edges_pdf, bin_c_cond,
                                                    d_bin_c_cond)

    # Calculate extensive strain rate tensor PDF
    lambda3_pdf, lambda3_bin_pdf = utils.cond_pdf2d(lambda3, s_d, c_half,
                                                    bin_edges_pdf, bin_c_cond,
                                                    d_bin_c_cond)

    print('Finished strain rate tensor PDF!')

    return [lambda1_pdf, lambda1_bin_pdf, lambda2_pdf, lambda2_bin_pdf,
            lambda3_pdf, lambda3_bin_pdf]


def calc_strain_rate_jpdf(lambda1, lambda2, lambda3, c_half, s_d):
    """Calculate strain rate tensor eigenvalues."""

    # Condition
    cond = np.absolute(c_half - 0.73) < (0.2 / 2.0)

    # Extract conditional array
    s_d_cond = np.extract(cond, s_d)
    lambda1_cond = np.extract(cond, lambda1)
    lambda2_cond = np.extract(cond, lambda2)
    lambda3_cond = np.extract(cond, lambda3)

    # Flatten arrays
    s_d_cond_flat = np.ndarray.flatten(s_d_cond)
    lambda1_cond_flat = np.ndarray.flatten(lambda1_cond)
    lambda2_cond_flat = np.ndarray.flatten(lambda2_cond)
    lambda3_cond_flat = np.ndarray.flatten(lambda3_cond)

    # Bin spacing
    lambda_bin_pdf = np.linspace(-15e4, 15e4, 60)
    s_d_bin_pdf = np.linspace(-15, 15, 60)

    # Calculate compressive strain rate tensor PDF
    lambda1_pdf, lambda1_bin_edges, s_d_bin_edges = \
        np.histogram2d(lambda1_cond_flat, s_d_cond_flat, bins=(
            lambda_bin_pdf, s_d_bin_pdf), density=True)
    lambda1_pdf_bin = 0.5 * (lambda1_bin_edges[:-1] + lambda1_bin_edges[1:])
    s_d_bin_pdf1 = 0.5 * (s_d_bin_edges[:-1] + s_d_bin_edges[1:])

    # Calculate intermediate strain rate tensor PDF
    lambda2_pdf, lambda2_bin_edges, s_d_bin_edges = \
        np.histogram2d(lambda2_cond_flat, s_d_cond_flat, bins=(
            lambda_bin_pdf, s_d_bin_pdf), density=True)
    lambda2_jpdf_bin = 0.5 * (lambda2_bin_edges[:-1] + lambda2_bin_edges[1:])
    s_d_bin_pdf2 = 0.5 * (s_d_bin_edges[:-1] + s_d_bin_edges[1:])

    # Calculate extensive strain rate tensor PDF
    lambda3_pdf, lambda3_bin_edges, s_d_bin_edges = \
        np.histogram2d(lambda3_cond_flat, s_d_cond_flat, bins=(
            lambda_bin_pdf, s_d_bin_pdf), density=True)
    lambda3_bin_pdf = 0.5 * (lambda3_bin_edges[:-1] + lambda3_bin_edges[1:])
    s_d_bin_pdf3 = 0.5 * (s_d_bin_edges[:-1] + s_d_bin_edges[1:])

    # Bin spacing
    bin_edges_pdf = np.linspace(-1e2, 1e2, 60)
    bin_c_cond = np.linspace(0.725, 0.735, 1)
    d_bin_c_cond = 0.01

    # Calculate displacement speed PDF
    s_d_pdf, s_d_bin_edges_cond = utils.cond_pdf(
        s_d[:, :, :],
        c_half[:, :, :], bin_edges_pdf, bin_c_cond, d_bin_c_cond)
    s_d_bin_pdf = np.linspace(-9, 14, 20)
    d_bin_disp_speed = 1 / 20

    nc = len(s_d_bin_pdf)

    # Pre-fill arrays with zeroes
    lambda1_cond_mean = np.zeros([nc])
    lambda2_cond_mean = np.zeros([nc])
    lambda3_cond_mean = np.zeros([nc])

    for i in range(0, nc):
        # Condition
        cond = np.absolute(s_d_cond_flat -
                           s_d_bin_pdf[i]) < d_bin_disp_speed / 2.0

        # Calculate compressive strain rate tensor conditional mean
        ext = np.extract(cond, lambda1_cond_flat)
        mean = np.mean(ext)
        lambda1_cond_mean[i] = mean

        # Calculate intermediate strain rate tensor conditional mean
        ext = np.extract(cond, lambda2_cond_flat)
        mean = np.mean(ext)
        lambda2_cond_mean[i] = mean

        # Calculate extensive strain rate tensor conditional mean
        ext = np.extract(cond, lambda3_cond_flat)
        mean = np.mean(ext)
        lambda3_cond_mean[i] = mean

    print('Finished strain rate tensor JPDF!')

    return [s_d_pdf,
            s_d_bin_edges_cond,
            s_d_bin_pdf,
            lambda1_pdf_bin,
            lambda1_pdf,
            lambda1_cond_mean,
            s_d_bin_pdf1,
            lambda2_jpdf_bin,
            lambda2_pdf,
            lambda2_cond_mean,
            s_d_bin_pdf2,
            lambda3_bin_pdf,
            lambda3_pdf,
            lambda3_cond_mean,
            s_d_bin_pdf3]
