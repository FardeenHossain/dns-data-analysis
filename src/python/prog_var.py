import h5py
import my_h5
from config import nx, ny, nz, o2_b, o2_u


def calc_u(
    data_file1, data_file2, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end
):
    # Read U
    u_old = my_h5.read_var(
        data_file1,
        "/data",
        "/data/U",
        [[ix_start, iy_start, iz_start], [ix_end + 1, iy_end + 1, iz_end + 1]],
        nx,
        ny,
        nz,
    )

    u_new = my_h5.read_var(
        data_file2,
        "/data",
        "/data/U",
        [[ix_start, iy_start, iz_start], [ix_end + 1, iy_end + 1, iz_end + 1]],
        nx,
        ny,
        nz,
    )

    u_half = (u_old + u_new) / 2

    return u_half


def calc_v(
    data_file1, data_file2, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end
):
    # Read V
    v_old = my_h5.read_var(
        data_file1,
        "/data",
        "/data/V",
        [[ix_start, iy_start, iz_start], [ix_end + 1, iy_end + 1, iz_end + 1]],
        nx,
        ny,
        nz,
    )

    v_new = my_h5.read_var(
        data_file2,
        "/data",
        "/data/V",
        [[ix_start, iy_start, iz_start], [ix_end + 1, iy_end + 1, iz_end + 1]],
        nx,
        ny,
        nz,
    )

    v_half = (v_old + v_new) / 2

    return v_half


def calc_w(
    data_file1, data_file2, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end
):
    # Read W
    w_old = my_h5.read_var(
        data_file1,
        "/data",
        "/data/W",
        [[ix_start, iy_start, iz_start], [ix_end + 1, iy_end + 1, iz_end + 1]],
        nx,
        ny,
        nz,
    )

    w_new = my_h5.read_var(
        data_file2,
        "/data",
        "/data/W",
        [[ix_start, iy_start, iz_start], [ix_end + 1, iy_end + 1, iz_end + 1]],
        nx,
        ny,
        nz,
    )

    w_half = (w_old + w_new) / 2

    return w_half


def calc_rho(
    data_file1, data_file2, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end
):
    # Read W
    rho_old = my_h5.read_var(
        data_file1,
        "/data",
        "/data/RHO",
        [[ix_start, iy_start, iz_start], [ix_end, iy_end, iz_end]],
        nx,
        ny,
        nz,
    )

    rho_new = my_h5.read_var(
        data_file2,
        "/data",
        "/data/RHO",
        [[ix_start, iy_start, iz_start], [ix_end, iy_end, iz_end]],
        nx,
        ny,
        nz,
    )

    rho_half = (rho_old + rho_new) / 2

    return rho_half


def calc_prog_var(
    data_file1, data_file2, ix_start, iy_start, iz_start, ix_end, iy_end, iz_end
):
    # Read O2
    o2_old = my_h5.read_var(
        data_file1,
        "/data",
        "/data/O2",
        [[ix_start, iy_start, iz_start], [ix_end, iy_end, iz_end]],
        nx,
        ny,
        nz,
    )

    o2_new = my_h5.read_var(
        data_file2,
        "/data",
        "/data/O2",
        [[ix_start, iy_start, iz_start], [ix_end, iy_end, iz_end]],
        nx,
        ny,
        nz,
    )

    # Read dt
    f = h5py.File(data_file2, "r")
    dt = f["/data"].attrs["time_variables"][0]

    # Compute C from O2
    c_new = 1 - ((o2_new - o2_b) / (o2_u - o2_b))
    c_old = 1 - ((o2_old - o2_b) / (o2_u - o2_b))

    c_half = (c_old + c_new) / 2
    dc = (c_new - c_old) / dt

    return [c_half, dc]
