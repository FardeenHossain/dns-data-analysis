import numpy as np


def hessian(f, dx):
    [df_x, df_y, df_z] = np.gradient(f, dx)

    # First row
    [h11, h12, h13] = np.gradient(df_x, dx)

    # Second row
    [h21, h22, h23] = np.gradient(df_y, dx)

    # Third row
    [h31, h32, h33] = np.gradient(df_z, dx)

    print('Hessian computed!')

    return [df_x, df_y, df_z, h11, h12, h13, h21, h22, h23, h31, h32, h33]


def adj(h11, h12, h13, h21, h22, h23, h31, h32, h33):
    a11 = h22 * h33 - h23 * h32
    a12 = h23 * h31 - h21 * h33
    a13 = h21 * h32 - h22 * h31
    a21 = h13 * h32 - h12 * h33
    a22 = h11 * h33 - h13 * h31
    a23 = h12 * h31 - h22 * h32
    a31 = h12 * h23 - h13 * h22
    a32 = h21 * h13 - h11 * h23
    a33 = h11 * h22 - h12 * h21

    return [a11, a12, a13, a21, a22, a23, a31, a32, a33]


def mean_curv(f, dx):
    # Gradient and hessian components
    [df_x, df_y, df_z, h11, h12, h13, h21, h22, h23, h31, h32, h33] = hessian(
        f, dx)

    # Gradient modulus
    mod_df = (df_x ** 2 + df_y ** 2 + df_z ** 2) ** 0.5

    int1 = h11 * df_x + h12 * df_y + h13 * df_z
    int2 = h21 * df_x + h22 * df_y + h23 * df_z
    int3 = h31 * df_x + h32 * df_y + h33 * df_z

    t1 = int1 * df_x + int2 * df_y + int3 * df_z

    k_m = -(t1 - (mod_df ** 2) * (h11 + h22 + h33)) / (2 * (mod_df ** 3))

    print('Mean curvature computed')

    return k_m


def gauss_curv(f, dx):
    # Gradient and hessian matrix
    [df_x, df_y, df_z, h11, h12, h13, h21, h22, h23, h31, h32, h33] = hessian(
        f, dx)

    # Adjoint matrix
    [a11, a12, a13, a21, a22, a23, a31, a32, a33] = adj(h11, h12, h13, h21,
                                                        h22, h23, h31, h32,
                                                        h33)

    # Gradient modulus
    mod_df = (df_x ** 2 + df_y ** 2 + df_z ** 2) ** 0.5

    int1 = a11 * df_x + a12 * df_y + a13 * df_z
    int2 = a21 * df_x + a22 * df_y + a23 * df_z
    int3 = a31 * df_x + a32 * df_y + a33 * df_z

    t1 = int1 * df_x + int2 * df_y + int3 * df_z

    k_g = t1 / (mod_df ** 4)

    print('Gaussian curvature computed')

    return k_g
