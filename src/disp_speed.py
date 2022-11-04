import numpy as np
from input import nx_c, ny_c, nz_c, dx


def calc_disp_speed(u_half, v_half, w_half, c_half, dc):
    """Calculate displacement speed."""

    # Compute C gradient
    g_c = np.gradient(c_half, dx)
    g_cx = g_c[0]
    g_cy = g_c[1]
    g_cz = g_c[2]

    # Prefill arrays with zeros
    conv_u = np.zeros([nx_c, ny_c, nz_c])
    conv_v = np.zeros([nx_c, ny_c, nz_c])
    conv_w = np.zeros([nx_c, ny_c, nz_c])
    disp_speed = np.zeros([nx_c, ny_c, nz_c])

    # Calculate convective coefficients
    for i in range(0, nx_c):
        for j in range(0, ny_c):
            for k in range(0, nz_c):
                conv_u[i, j, k] = (u_half[i + 1, j, k] +
                                   u_half[i, j, k]) / 2 * g_cx[i, j, k]
                conv_v[i, j, k] = (v_half[i, j + 1, k] +
                                   v_half[i, j, k]) / 2 * g_cy[i, j, k]
                conv_w[i, j, k] = (w_half[i, j, k + 1] +
                                   w_half[i, j, k]) / 2 * g_cz[i, j, k]

    mag_g_c = (g_cx ** 2.0 + g_cy ** 2.0 + g_cz ** 2.0) ** 0.5

    # Calculate displacement speed
    disp_speed[:, :, :] = (dc[:, :, :] + conv_u[:, :, :] + conv_v[:, :, :] +
                           conv_w[:, :, :]) / mag_g_c[:, :, :]

    print('Finished displacement speed!')

    return disp_speed
