import numpy as np
import h5py

from input import nx_c, ny_c, nz_c, dx

import mystat
import myeig


def calc_strain_rate_tensor_eig(if_save, u_half, v_half, w_half, c_half,
                                disp_speed):
    """Calculate strain rate tensor eigenvalues."""

    cond = np.absolute(c_half - 0.73) < (0.2 / 2.0)
    disp_speed_cond = np.extract(cond, disp_speed)

    # Prefill arrays with zeroes
    lambda1 = np.zeros([nx_c, ny_c, nz_c])
    lambda2 = np.zeros([nx_c, ny_c, nz_c])
    lambda3 = np.zeros([nx_c, ny_c, nz_c])

    rr1 = np.zeros([nx_c, ny_c, nz_c, 3])
    rr2 = np.zeros([nx_c, ny_c, nz_c, 3])
    rr3 = np.zeros([nx_c, ny_c, nz_c, 3])

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

    # Compute eigenvalues and eigenvectors
    if if_save == 1:
        lambda1[:, :, :], lambda2[:, :, :], lambda3[:, :, :], \
        rr1[:, :, :, :], rr2[:, :, :, :], rr3[:, :, :, :] = myeig.vec_val(
            center_u[:, :, :], center_v[:, :, :], center_w[:, :, :], dx)

        f1 = h5py.File("./data/data_disp_speed.hdf5", "w")

        f1.create_dataset("lambda1", (nx_c, ny_c, nz_c), data=lambda1)
        f1.create_dataset("lambda2", (nx_c, ny_c, nz_c), data=lambda2)
        f1.create_dataset("lambda3", (nx_c, ny_c, nz_c), data=lambda3)
        f1.create_dataset("rr1", (nx_c, ny_c, nz_c, 3), data=rr1)
        f1.create_dataset("rr2", (nx_c, ny_c, nz_c, 3), data=rr2)
        f1.create_dataset("rr3", (nx_c, ny_c, nz_c, 3), data=rr3)

        print("\nCalculated and saved lambda!\n")

    elif if_save == 0:
        f1 = h5py.File('./data/data_disp_speed.hdf5', 'r')

        lambda1 = np.array(f1['lambda1'])
        lambda2 = np.array(f1['lambda2'])
        lambda3 = np.array(f1['lambda3'])

        print("\nImported lambda!\n")

    lambda1_cond = np.extract(cond, lambda1)
    lambda2_cond = np.extract(cond, lambda2)
    lambda3_cond = np.extract(cond, lambda3)

    lambda1_cond_flat = np.ndarray.flatten(lambda1_cond)
    lambda2_cond_flat = np.ndarray.flatten(lambda2_cond)
    lambda3_cond_flat = np.ndarray.flatten(lambda3_cond)

    disp_c_cond_flat = np.ndarray.flatten(disp_speed_cond)

    bin_edges_jpdf_lam = np.linspace(-15e4, 15e4, 60)
    bin_edges_jpdf_disp_speed_c = np.linspace(-15, 15, 60)

    # Compressive strain tensor
    lambda1_disp_speed_c_jpdf, lambda1_bin_edges, disp_bin_edges = \
        np.histogram2d(lambda1_cond_flat, disp_c_cond_flat, bins=(
            bin_edges_jpdf_lam, bin_edges_jpdf_disp_speed_c), density=True)

    lambda1_jpdf_bin = 0.5 * (lambda1_bin_edges[:-1] + lambda1_bin_edges[1:])
    disp1_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    # Intermediate strain tensor
    lambda2_disp_speed_c_jpdf, lambda2_bin_edges, disp_bin_edges = \
        np.histogram2d(lambda2_cond_flat, disp_c_cond_flat, bins=(
            bin_edges_jpdf_lam, bin_edges_jpdf_disp_speed_c), density=True)

    lambda2_jpdf_bin = 0.5 * (lambda2_bin_edges[:-1] + lambda2_bin_edges[1:])
    disp2_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    # Extensive strain tensor
    lambda3_disp_speed_c_jpdf, lambda3_bin_edges, disp_bin_edges = \
        np.histogram2d(lambda3_cond_flat, disp_c_cond_flat, bins=(
            bin_edges_jpdf_lam, bin_edges_jpdf_disp_speed_c), density=True)

    lambda3_jpdf_bin = 0.5 * (lambda3_bin_edges[:-1] + lambda3_bin_edges[1:])
    disp3_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    # Save displacement speed
    if if_save == 1:
        f1.create_dataset("dataset_disp_sp_PROG", (nx_c, ny_c, nz_c),
                          dtype='i', data=disp_speed)

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
        cond = np.absolute(disp_c_cond_flat -
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
