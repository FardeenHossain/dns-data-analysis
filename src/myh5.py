import h5py
import numpy as np


def read_var(filename, group_name, var, ijk, nx, ny, nz):
    """
    Function to read data from file.
    It reads the variable var and return an array with one extra point around
    in each direction.
    Size of the output is then: nz_loc+2, ny_loc+2, nx_loc+2
    """

    # Unpack
    i1 = ijk[0][0]
    j1 = ijk[0][1]
    k1 = ijk[0][2]

    i2 = ijk[1][0]
    j2 = ijk[1][1]
    k2 = ijk[1][2]

    nx_loc = i2 - i1
    ny_loc = j2 - j1
    nz_loc = k2 - k1

    # -------------------------------------------------------------------------

    # Open HDF5 file
    f = h5py.File(filename, 'r')

    # Link group
    group = f[group_name]

    # # Overall size
    # Nx = group.attrs['dimensions'][0]
    # Ny = group.attrs['dimensions'][1]
    # Nz = group.attrs['dimensions'][2]

    # Link dataset 
    # This does not read the data
    # Data is still on disk only
    dset = f[var]

    # Define a dummy array
    q = np.zeros([nz_loc, ny_loc, nx_loc])

    # Actual read of the data from disc to memory
    q = dset[k1:k2, j1:j2, i1:i2]

    # Assign data to array
    # This array has (nx_loc+2)*(ny_loc+2)*(nz_loc+2) elements and can be used
    # to compute derivatives and obtain an array of derivatives with #
    # (nx_loc)*(ny_loc)*(nz_loc) elements
    variable = np.transpose(q)

    # Close HDF5 file
    f.close()

    return variable


def read_vel_center(filename, group_name, ijk, nx, ny, nz):
    # Unpack
    i1 = ijk[0][0]
    j1 = ijk[0][1]
    k1 = ijk[0][2]

    i2 = ijk[1][0]
    j2 = ijk[1][1]
    k2 = ijk[1][2]

    nx_loc = i2 - i1
    ny_loc = j2 - j1
    nz_loc = k2 - k1

    # -------------------------------------------------------------------------

    # Open HDF5 file
    f = h5py.File(filename, 'r')

    # Link group
    group = f[group_name]

    # # Overall size
    # Nx = group.attrs['dimensions'][0]
    # Ny = group.attrs['dimensions'][1]
    # Nz = group.attrs['dimensions'][2]

    # -------------------------------------------------------------------------

    # U
    # Link dataset 
    var = '/data/u'
    dset = f[var]

    # Define a dummy array
    q = np.zeros([nz_loc, ny_loc, nx_loc + 1])

    # Actual read of the data from disc to memory
    q = dset[k1:k2, j1:j2, i1:i2 + 1]
    q2 = np.transpose(q)

    # Assign data to array
    # This array has (nx_loc+2)*(ny_loc+2)*(nz_loc+2) elements and can be used
    # to compute derivatives and obtain an array of derivatives with
    # (nx_loc)*(ny_loc)*(nz_loc) elements
    u = 0.5 * (q2[:-1, :, :] + q2[1:, :, :])

    # -------------------------------------------------------------------------

    # V
    # Link dataset 
    var = '/data/V'
    dset = f[var]

    # Define a dummy array
    q = np.zeros([nz_loc, ny_loc + 1, nx_loc])

    # Actual read of the data from disc to memory
    q = dset[k1:k2, j1:j2 + 1, i1:i2]

    q2 = np.transpose(q)

    # Assign data to array
    # This array has (nx_loc+2)*(ny_loc+2)*(nz_loc+2) elements and can be used
    # to compute derivatives and obtain an array of derivatives with
    # (nx_loc)*(ny_loc)*(nz_loc) elements
    v = 0.5 * (q2[:, :-1, :] + q2[:, 1:, :])

    # -------------------------------------------------------------------------

    # W
    # Link dataset 
    var = '/data/W'
    dset = f[var]

    # Define a dummy array
    q = np.zeros([nz_loc + 1, ny_loc, nx_loc])

    # Actual read of the data from disc to memory
    q[0:nz_loc, 0:ny_loc, 0:nx_loc] = dset[k1:k2, j1:j2, i1:i2]

    if k2 == nz:
        q[nz_loc, :, :] = dset[0, j1:j2, i1:i2]
    else:
        q[nz_loc, :, :] = dset[k2, j1:j2, i1:i2]

    q2 = np.transpose(q)

    # Assign data to array
    # This array has (nx_loc+2)*(ny_loc+2)*(nz_loc+2) elements and can be
    # used to compute derivatives and obtain an array of derivatives with
    # (nx_loc)*(ny_loc)*(nz_loc) elements
    w = 0.5 * (q2[:, :, :-1] + q2[:, :, 1:])

    # Close HDF5 file
    f.close()

    return [u, v, w]
