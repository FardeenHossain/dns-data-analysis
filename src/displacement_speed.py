import numpy as np
import os

import input
import plot
import myh5


def calculate_displacement_speed(in_path, ix_start, iy_start, iz_start, ix_end,
                                 iy_end, iz_end, nx, ny, nz, nx_c, ny_c, nz_c):
    # Print title
    print('\nCalculating Displacement Speed...\n')

    # Oxygen values
    o2_u = 2.237710e-01     # Unburned
    o2_b = 6.677090e-02     # Burned

    # Data files
    data_file1 = os.path.join(in_path, 'data_1.300E-03.h5')
    data_file2 = os.path.join(in_path, 'data2_1.300E-03.h5')

    # Time derivative
    dt = 1.15577e-07
    # info = hdf5read(['../data_', listfile{i}], 'data', 'time_variables')
    # dt = info(1)

    # Read U
    u_old = myh5.read_var(data_file1, '/data', '/data/U',
                          [[ix_start, iy_start, iz_start],
                           [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    u_new = myh5.read_var(data_file2, '/data', '/data/U',
                          [[ix_start, iy_start, iz_start],
                           [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    u_half = (u_old + u_new) / 2
    print('Finished U!')

    # Read V
    v_old = myh5.read_var(data_file1, '/data', '/data/V',
                          [[ix_start, iy_start, iz_start],
                           [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    v_new = myh5.read_var(data_file2, '/data', '/data/V',
                          [[ix_start, iy_start, iz_start],
                           [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    v_half = (v_old + v_new) / 2
    print('Finished V!')

    # Read W
    w_old = myh5.read_var(data_file1, '/data', '/data/W',
                          [[ix_start, iy_start, iz_start],
                           [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    w_new = myh5.read_var(data_file2, '/data', '/data/W',
                          [[ix_start, iy_start, iz_start],
                           [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    w_half = (w_old + w_new) / 2
    print('Finished W!')

    # Read O2
    o2_old = myh5.read_var(data_file1, '/data', '/data/O2',
                           [[ix_start, iy_start, iz_start],
                            [ix_end, iy_end, iz_end]], nx, ny, nz)

    o2_new = myh5.read_var(data_file2, '/data', '/data/O2',
                           [[ix_start, iy_start, iz_start],
                            [ix_end, iy_end, iz_end]], nx, ny, nz)

    print('Finished O2!')

    # Calculate C
    c_new = 1 - ((o2_new - o2_b) / (o2_u - o2_b))
    c_old = 1 - ((o2_old - o2_b) / (o2_u - o2_b))

    c_half = (c_old + c_new) / 2
    dc = (c_new - c_old) / dt
    print('Finished C!\n')

    # x derivative
    dx = 20e-6

    g_c = np.gradient(c_half, dx)

    g_cx = g_c[0]
    g_cy = g_c[1]
    g_cz = g_c[2]

    # Prefill arrays with zeros
    conv_u = np.zeros([nx_c, ny_c, nz_c])
    conv_v = np.zeros([nx_c, ny_c, nz_c])
    conv_w = np.zeros([nx_c, ny_c, nz_c])

    disp_speed_c = np.zeros([nx_c, ny_c, nz_c])

    print(f"g_c: {g_cx.shape}, {g_cy.shape}, {g_cz.shape}\n")

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

    print(f"mag_g_c: {mag_g_c.shape}")
    print(f"dc: {dc.shape}")
    print(f"conv_u: {conv_u.shape}")

    # Calculate displacement speed
    disp_speed_c[:, :, :] = (dc[:, :, :] + conv_u[:, :, :] + conv_v[:, :, :] +
                             conv_w[:, :, :]) / mag_g_c[:, :, :]

    # Plot graph
    plot.plot_displacement_speed(disp_speed_c)


# Driver function
calculate_displacement_speed(input.in_path,
                             input.ix_start,
                             input.iy_start,
                             input.iz_start,
                             input.ix_end,
                             input.iy_end,
                             input.iz_end,
                             input.Nx,
                             input.Ny,
                             input.Nz,
                             input.Nx_c,
                             input.Ny_c,
                             input.Nz_c)
