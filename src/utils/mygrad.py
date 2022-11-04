import numpy as np


def vel_grad(u, v, w, dx):
    # Compute gradient of U
    g_c = np.gradient(u, dx)
    g_ux = g_c[0]
    g_uy = g_c[1]
    g_uz = g_c[2]

    # Compute gradient of V
    g_c = np.gradient(v, dx)
    g_vx = g_c[0]
    g_vy = g_c[1]
    g_vz = g_c[2]

    # Compute gradient of W
    g_c = np.gradient(w, dx)
    g_wx = g_c[0]
    g_wy = g_c[1]
    g_wz = g_c[2]

    return [g_ux, g_uy, g_uz, g_vx, g_vy, g_vz, g_wx, g_wy, g_wz]
