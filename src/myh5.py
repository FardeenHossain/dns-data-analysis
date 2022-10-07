import h5py
import numpy as np
import math


# ------------------------------------------------------
# Function to read data from file
# It reads the variable var and return an array with 
# one extra point around in each direction 
# size of the output is then: Nz_loc+2,Ny_loc+2,Nx_loc+2

def read_var(filename,group_name,var, ijk,Nx,Ny,Nz):

    # ------------------------------------------------------
    # unpack 
    i1 =ijk[0][0]
    j1 =ijk[0][1]
    k1 =ijk[0][2]

    i2 =ijk[1][0]
    j2 =ijk[1][1]
    k2 =ijk[1][2]

    Nx_loc = i2-i1
    Ny_loc = j2-j1
    Nz_loc = k2-k1
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Open HDF5 file
    #f = h5py.File('reduced_data2_5.500E-03.h5', 'r')
    f = h5py.File(filename, 'r')
    
    # Link group
    group = f[group_name]
    
    # Link dataset 
    # This does not read the data
    # Data are still on disk only
    dset = f[var]

#    # Overall size
#    Nx = group.attrs['dimensions'][0]
#    Ny = group.attrs['dimensions'][1]
#    Nz = group.attrs['dimensions'][2]
    
    # Define a dummy array
    q = np.zeros([Nz_loc,Ny_loc,Nx_loc])
    
    #   # Actual read of the data from disc to memory
    q = dset[k1:k2,j1:j2,i1:i2]
    
    # Assign data to array
    # This array has (Nx_loc+2)*(Ny_loc+2)*(Nz_loc+2)
    # elements 
    # and can be used to compute derivatives
    # and obtain an array of derivatives 
    # with (Nx_loc)*(Ny_loc)*(Nz_loc) elements
    variable = np.transpose(q)
    
    # Close HDF5 file
    f.close()

    return variable
    # ------------------------------------------------------



def read_vel_center(filename,group_name, ijk,Nx,Ny,Nz):

    # ------------------------------------------------------
    # unpack 
    i1 =ijk[0][0]
    j1 =ijk[0][1]
    k1 =ijk[0][2]

    i2 =ijk[1][0]
    j2 =ijk[1][1]
    k2 =ijk[1][2]

    Nx_loc = i2-i1
    Ny_loc = j2-j1
    Nz_loc = k2-k1
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Open HDF5 file
    f = h5py.File(filename, 'r')

    # Link group
    group = f[group_name]

#    # Overall size
#    Nx = group.attrs['dimensions'][0]
#    Ny = group.attrs['dimensions'][1]
#    Nz = group.attrs['dimensions'][2]
    
    # U -------
    # Link dataset 
    var = '/data/U'
    dset = f[var]
    
    # Define a dummy array
    q = np.zeros([Nz_loc,Ny_loc,Nx_loc+1])
    
    #   # Actual read of the data from disc to memory
    q = dset[k1:k2,j1:j2,i1:i2+1]

    q2 = np.transpose(q)
    
    # Assign data to array
    # This array has (Nx_loc+2)*(Ny_loc+2)*(Nz_loc+2) elements 
    # and can be used to compute derivatives
    # and obtain an array of derivatives with (Nx_loc)*(Ny_loc)*(Nz_loc) elements
    U = 0.5*(q2[:-1,:,:] + q2[1:,:,:])

    # V -------
    # Link dataset 
    var = '/data/V'
    dset = f[var]
    
    # Define a dummy array
    q = np.zeros([Nz_loc,Ny_loc+1,Nx_loc])
    
    #   # Actual read of the data from disc to memory
    q = dset[k1:k2,j1:j2+1,i1:i2]

    q2 = np.transpose(q)
    
    # Assign data to array
    # This array has (Nx_loc+2)*(Ny_loc+2)*(Nz_loc+2) elements 
    # and can be used to compute derivatives
    # and obtain an array of derivatives with (Nx_loc)*(Ny_loc)*(Nz_loc) elements
    V = 0.5*(q2[:,:-1,:] + q2[:,1:,:])

    # W -------
    # Link dataset 
    var = '/data/W'
    dset = f[var]
    
    # Define a dummy array
    q = np.zeros([Nz_loc+1,Ny_loc,Nx_loc])
    
    #   # Actual read of the data from disc to memory
    q[0:Nz_loc,0:Ny_loc,0:Nx_loc] = dset[k1:k2,j1:j2,i1:i2]

    if k2 == Nz:
        q[Nz_loc,:,:] = dset[0,j1:j2,i1:i2]
    else:
        q[Nz_loc,:,:] = dset[k2,j1:j2,i1:i2]

    q2 = np.transpose(q)
    
    # Assign data to array
    # This array has (Nx_loc+2)*(Ny_loc+2)*(Nz_loc+2) elements 
    # and can be used to compute derivatives
    # and obtain an array of derivatives with (Nx_loc)*(Ny_loc)*(Nz_loc) elements
    W = 0.5*(q2[:,:,:-1] + q2[:,:,1:])



    # Close HDF5 file
    f.close()

    return [U,V,W]
    # ------------------------------------------------------
    # ------------------------------------------------------
