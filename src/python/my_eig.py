import my_grad
import numpy as np


def vec_val(u, v, w, dx):
    [g_ux, g_uy, g_uz, g_vx, g_vy, g_vz, g_wx, g_wy, g_wz] = my_grad.vel_grad(
        u, v, w, dx
    )

    nx = len(u[:, 1, 1])
    ny = len(v[1, :, 1])
    nz = len(w[1, 1, :])

    lam1 = np.zeros([nx, ny, nz])
    lam2 = np.zeros([nx, ny, nz])
    lam3 = np.zeros([nx, ny, nz])

    rr1 = np.zeros([nx, ny, nz, 3])
    rr2 = np.zeros([nx, ny, nz, 3])
    rr3 = np.zeros([nx, ny, nz, 3])
    bb = np.zeros([4, 3])

    for i in range(0, nx):
        for j in range(0, ny):
            for k in range(0, nz):
                # mm is the velocity gradient A
                mm = [
                    [g_ux[i, j, k], g_uy[i, j, k], g_uz[i, j, k]],
                    [g_vx[i, j, k], g_vy[i, j, k], g_vz[i, j, k]],
                    [g_wx[i, j, k], g_wy[i, j, k], g_wz[i, j, k]],
                ]

                # mm2 is the strain tensor S = 0.5(A + A_transpose)
                mm2 = 0.5 * (mm + np.transpose(mm))
                lam, rr = np.linalg.eig(mm2)

                bb[0, 0] = lam[0]
                bb[0, 1] = lam[1]
                bb[0, 2] = lam[2]

                bb[1:, 0] = rr[:, 0]
                bb[1:, 1] = rr[:, 1]
                bb[1:, 2] = rr[:, 2]

                bb2 = np.transpose(bb)

                bb_sort = bb2[bb2[:, 0].argsort()]

                r1 = bb_sort[0, 1:]
                r2 = bb_sort[1, 1:]
                r3 = bb_sort[2, 1:]

                rr1[i, j, k, :] = r1
                rr2[i, j, k, :] = r2
                rr3[i, j, k, :] = r3

                lam1[i, j, k] = bb_sort[0, 0]
                lam2[i, j, k] = bb_sort[1, 0]
                lam3[i, j, k] = bb_sort[2, 0]

    return [lam1, lam2, lam3, rr1, rr2, rr3]
