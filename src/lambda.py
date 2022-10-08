import numpy as np
import h5py

import mystat
import myeig


def calc_gamma(if_save, nx_c, ny_c, nz_c, dx, u_half, v_half, w_half, c_half,
               disp_speed):
    cond = np.absolute(c_half - 0.73) < (0.2 / 2.0)
    disp_speed_cond = np.extract(cond, disp_speed)

    lam1 = np.zeros([nx_c, ny_c, nz_c])
    lam2 = np.zeros([nx_c, ny_c, nz_c])
    lam3 = np.zeros([nx_c, ny_c, nz_c])

    rr1 = np.zeros([nx_c, ny_c, nz_c, 3])
    rr2 = np.zeros([nx_c, ny_c, nz_c, 3])
    rr3 = np.zeros([nx_c, ny_c, nz_c, 3])

    center_u = np.zeros([nx_c, ny_c, nz_c])
    center_v = np.zeros([nx_c, ny_c, nz_c])
    center_w = np.zeros([nx_c, ny_c, nz_c])

    for i in range(0, nx_c):
        for j in range(0, ny_c):
            for k in range(0, nz_c):
                center_u[i, j, k] = (u_half[i + 1, j, k] + u_half[i, j, k]) / 2
                center_v[i, j, k] = (v_half[i, j + 1, k] + v_half[i, j, k]) / 2
                center_w[i, j, k] = (w_half[i, j, k + 1] + w_half[i, j, k]) / 2

    print(f"center_U: {center_u.shape}")
    print(f"lambda_1: {lam1.shape}\n")

    if if_save == 1:
        lam1[:, :, :], lam2[:, :, :], lam3[:, :, :], rr1[:, :, :, :], \
        rr2[:, :, :, :], rr3[:, :, :, :] = myeig.vec_val(
            center_u[:, :, :], center_v[:, :, :], center_w[:, :, :], dx)

        f1 = h5py.File("data_disp_sp.hdf5", "w")

        dset1 = f1.create_dataset("lam1", (nx_c, ny_c, nz_c), data=lam1)
        dset2 = f1.create_dataset("lam2", (nx_c, ny_c, nz_c), data=lam2)
        dset3 = f1.create_dataset("lam3", (nx_c, ny_c, nz_c), data=lam3)

        dset4 = f1.create_dataset("rr1", (nx_c, ny_c, nz_c, 3), data=rr1)
        dset5 = f1.create_dataset("rr2", (nx_c, ny_c, nz_c, 3), data=rr2)
        dset6 = f1.create_dataset("rr3", (nx_c, ny_c, nz_c, 3), data=rr3)

        print("Calculated and saved Lambda!\n")

    elif if_save == 0:
        f1 = h5py.File('data_disp_sp.hdf5', 'r')

        lam1 = np.array(f1['lam1'])
        lam2 = np.array(f1['lam2'])
        lam3 = np.array(f1['lam3'])

        rr1 = np.array(f1['rr1'])
        rr2 = np.array(f1['rr2'])
        rr3 = np.array(f1['rr3'])

        print("Imported Lambda!\n")

    lam1_cond = np.extract(cond, lam1)
    lam2_cond = np.extract(cond, lam2)
    lam3_cond = np.extract(cond, lam3)

    lam1_cond_flat = np.ndarray.flatten(lam1_cond)
    lam2_cond_flat = np.ndarray.flatten(lam2_cond)
    lam3_cond_flat = np.ndarray.flatten(lam3_cond)

    # disp_sp_PROG_flat = np.ndarray.flatten(disp_sp_PROG)
    disp_PROG_cond_flat = np.ndarray.flatten(disp_speed_cond)
    print(f"lambda_1 cond flat: {lam1_cond_flat.shape}")
    print(f"disp_PROG cond flat: {disp_PROG_cond_flat.shape}\n")

    bin_edges_jpdf_lam = np.linspace(-15e4, 15e4, 60)
    bin_edges_jpdf_disp_sp_PROG = np.linspace(-15, 15, 60)

    lam1_disp_sp_PROG_jpdf, lam1_bin_edges, disp_bin_edges = np.histogram2d(
        lam1_cond_flat, disp_PROG_cond_flat, bins=(
            bin_edges_jpdf_lam, bin_edges_jpdf_disp_sp_PROG), density=True)

    lam1_jpdf_bin = 0.5 * (lam1_bin_edges[:-1] + lam1_bin_edges[1:])
    disp1_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    lam2_disp_sp_PROG_jpdf, lam2_bin_edges, disp_bin_edges = np.histogram2d(
        lam2_cond_flat, disp_PROG_cond_flat, bins=(
            bin_edges_jpdf_lam, bin_edges_jpdf_disp_sp_PROG), density=True)

    lam2_jpdf_bin = 0.5 * (lam2_bin_edges[:-1] + lam2_bin_edges[1:])
    disp2_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    lam3_disp_sp_PROG_jpdf, lam3_bin_edges, disp_bin_edges = np.histogram2d(
        lam3_cond_flat, disp_PROG_cond_flat,
        bins=(bin_edges_jpdf_lam, bin_edges_jpdf_disp_sp_PROG), density=True)

    lam3_jpdf_bin = 0.5 * (lam3_bin_edges[:-1] + lam3_bin_edges[1:])
    disp3_jpdf_bin = 0.5 * (disp_bin_edges[:-1] + disp_bin_edges[1:])

    f1 = h5py.File("data_disp_speed.hdf5", "w")
    dset = f1.create_dataset("dataset_disp_sp_PROG", (nx_c, ny_c, nz_c),
                             dtype='i', data=disp_speed)

    bin_edges_pdf = np.linspace(-1e2, 1e2, 60)
    bin_c_cond = np.linspace(0.725, 0.735, 1)

    d_bin_c_cond = 0.01
    [pdf_disp_sp_cond, bin_pdf_disp_sp_cond] = mystat.cond_pdf(
        disp_speed[:, :, :],
        c_half[:, :, :], bin_edges_pdf, bin_c_cond, d_bin_c_cond)

    bin_edges_pdf_lam = np.linspace(-1e6, 1e6, 400)
    [pdf_lam1_cond, bin_pdf_lam1_cond] = mystat.cond_pdf(lam1[:, :, :],
                                                         c_half[:, :, :],
                                                         bin_edges_pdf_lam,
                                                         bin_c_cond,
                                                         d_bin_c_cond)

    bin_disp_sp = np.linspace(-9, 14, 20)
    d_bin_disp_sp = 1 / 20

    NC = len(bin_disp_sp)

    lam1_cond_mean = np.zeros([NC])
    lam2_cond_mean = np.zeros([NC])
    lam3_cond_mean = np.zeros([NC])

    for i in range(0, NC):
        print(f"iteration: {i}, bin displacement speed: {bin_disp_sp[i]}")

        cond = np.absolute(disp_PROG_cond_flat -
                           bin_disp_sp[i]) < d_bin_disp_sp / 2.0

        ext = np.extract(cond, lam1_cond_flat)
        mean = np.mean(ext)
        lam1_cond_mean[i] = mean

        ext = np.extract(cond, lam2_cond_flat)
        mean = np.mean(ext)
        lam2_cond_mean[i] = mean

        ext = np.extract(cond, lam3_cond_flat)
        mean = np.mean(ext)
        lam3_cond_mean[i] = mean
