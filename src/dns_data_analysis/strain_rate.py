import numpy as np
import myeig
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
    [lambda1, lambda2, lambda3, rr1, rr2, rr3] = myeig.vec_val(
        center_u[:, :, :], center_v[:, :, :], center_w[:, :, :], dx)

    print("Finished strain rate tensor eigenvalues!")

    return [lambda1, lambda2, lambda3, rr1, rr2, rr3]
