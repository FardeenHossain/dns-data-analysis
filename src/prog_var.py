import utils
from input import nx, ny, nz, o2_u, o2_b, dt


def calc_u(data_file1, data_file2, ix_start, iy_start, iz_start, ix_end,
           iy_end, iz_end):
    """Calculate U."""

    # Read U
    u_old = utils.read_var(data_file1, "/data", "/data/U",
                           [[ix_start, iy_start, iz_start],
                            [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    u_new = utils.read_var(data_file2, "/data", "/data/U",
                           [[ix_start, iy_start, iz_start],
                            [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    u_half = (u_old + u_new) / 2

    return u_half


def calc_v(data_file1, data_file2, ix_start, iy_start, iz_start, ix_end,
           iy_end, iz_end):
    """Calculate V."""

    # Read V
    v_old = utils.read_var(data_file1, "/data", "/data/V",
                           [[ix_start, iy_start, iz_start],
                            [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    v_new = utils.read_var(data_file2, "/data", "/data/V",
                           [[ix_start, iy_start, iz_start],
                            [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    v_half = (v_old + v_new) / 2

    return v_half


def calc_w(data_file1, data_file2, ix_start, iy_start, iz_start, ix_end,
           iy_end, iz_end):
    """Calculate W."""

    # Read W
    w_old = utils.read_var(data_file1, "/data", "/data/W",
                           [[ix_start, iy_start, iz_start],
                            [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    w_new = utils.read_var(data_file2, "/data", "/data/W",
                           [[ix_start, iy_start, iz_start],
                            [ix_end + 1, iy_end + 1, iz_end + 1]], nx, ny, nz)

    w_half = (w_old + w_new) / 2

    return w_half


def calc_prog_var(data_file1, data_file2, ix_start, iy_start, iz_start,
                  ix_end, iy_end, iz_end):
    """Calculate progress variable."""

    # Read O2
    o2_old = utils.read_var(data_file1, "/data", "/data/O2",
                            [[ix_start, iy_start, iz_start],
                             [ix_end, iy_end, iz_end]], nx, ny, nz)

    o2_new = utils.read_var(data_file2, "/data", "/data/O2",
                            [[ix_start, iy_start, iz_start],
                             [ix_end, iy_end, iz_end]], nx, ny, nz)

    # Compute C from O2
    c_new = 1 - ((o2_new - o2_b) / (o2_u - o2_b))
    c_old = 1 - ((o2_old - o2_b) / (o2_u - o2_b))

    c_half = (c_old + c_new) / 2
    dc = (c_new - c_old) / dt

    print("Finished progress variable!")

    return [c_half, dc]
