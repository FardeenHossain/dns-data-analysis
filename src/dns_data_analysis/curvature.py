import numpy as np


def hessian(F, dx):
    [DF_x, DF_y, DF_z] = np.gradient(F, dx)

    # First row
    [H11, H12, H13] = np.gradient(DF_x, dx)

    # Second row
    [H21, H22, H23] = np.gradient(DF_y, dx)

    # Third row
    [H31, H32, H33] = np.gradient(DF_z, dx)

    print('Hessian computed')

    return [DF_x, DF_y, DF_z, H11, H12, H13, H21, H22, H23, H31, H32, H33]


def adj(H11, H12, H13, H21, H22, H23, H31, H32, H33):
    A11 = H22 * H33 - H23 * H32
    A12 = H23 * H31 - H21 * H33
    A13 = H21 * H32 - H22 * H31
    A21 = H13 * H32 - H12 * H33
    A22 = H11 * H33 - H13 * H31
    A23 = H12 * H31 - H22 * H32
    A31 = H12 * H23 - H13 * H22
    A32 = H21 * H13 - H11 * H23
    A33 = H11 * H22 - H12 * H21

    return [A11, A12, A13, A21, A22, A23, A31, A32, A33]


def mean_curv(F, dx):
    # Gradient and hessian components
    [DF_x, DF_y, DF_z, H11, H12, H13, H21, H22, H23, H31, H32, H33] = hessian(
        F, dx)

    # Gradient modulus
    mod_DF = (DF_x ^ 2 + DF_y ^ 2 + DF_z ^ 2) ^ 0.5

    int1 = H11 * DF_x + H12 * DF_y + H13 * DF_z
    int2 = H21 * DF_x + H22 * DF_y + H23 * DF_z
    int3 = H31 * DF_x + H32 * DF_y + H33 * DF_z

    T1 = int1 * DF_x + int2 * DF_y + int3 * DF_z

    # NB il meno va messo a causa della scelta del meno nelle normali
    KM = -(T1 - (mod_DF ^ 2) * (H11 + H22 + H33)) / (2 * (mod_DF ^ 3))

    print('Mean curvature computed')

    return KM


def gauss_curv(F, dx):
    # Gradient and hessian matrix
    [DF_x, DF_y, DF_z, H11, H12, H13, H21, H22, H23, H31, H32, H33] = hessian(
        F, dx)

    # Adjoint matrix
    [A11, A12, A13, A21, A22, A23, A31, A32, A33] = adj(H11, H12, H13, H21,
                                                        H22, H23, H31, H32,
                                                        H33)

    # Gradient modulus
    mod_DF = (DF_x ^ 2 + DF_y ^ 2 + DF_z ^ 2) ^ 0.5

    int1 = A11 * DF_x + A12 * DF_y + A13 * DF_z
    int2 = A21 * DF_x + A22 * DF_y + A23 * DF_z
    int3 = A31 * DF_x + A32 * DF_y + A33 * DF_z

    T1 = int1 * DF_x + int2 * DF_y + int3 * DF_z

    KG = T1 / (mod_DF ^ 4)

    print('Gaussian curvature computed')

    return KG
