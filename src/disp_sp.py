import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import h5py

import math
import random
import sys
import os

import myh5
import mystat
import myeig
import mygrad

from numpy import ndarray
from numpy import linalg as LA
from operator import itemgetter

# File path
in_path = '/hpcwork/itv/Antonio/premixed_jet_flames/R3K1/'
IF_save = 0 

# Data range
Nx = 2880
Ny = 1922
Nz = 512

# Chunk range
Nx_c = 30
Ny_c = 10
Nz_c = 50

# Start point
ix_start = 800
iy_start = 850
iz_start = 1

# End point
ix_end = ix_start + Nx_c
iy_end = iy_start + Ny_c
iz_end = iz_start + Nz_c

# -----------------------------------------------------------------------------

# Print title
print('\nDNS_premix_compute_disp_speed_PROG')
print('\r----\n')

# Oxygen values
O2_u = 2.237710e-01     # Unburned 
O2_b = 6.677090e-02     # Burned

# Data files
data_file1 = os.path.join(in_path, 'data_1.300E-03.h5')
data_file2 = os.path.join(in_path, 'data2_1.300E-03.h5')

# Read HDF5 files
read_df_1 = h5py.File(data_file1, 'r')
read_df_2 = h5py.File(data_file2, 'r')

## Time derivative
#info = hdf5read(['../data_', listfile{i}], 'data', 'time_variables')
# dt = info(1)

# Time derivative
dt = 1.15577e-07 

# Read U
U_old = myh5.read_var(data_file1, '/data', '/data/U', 
                      [[ix_start, iy_start, iz_start], 
                      [ix_end+1, iy_end+1, iz_end+1]], Nx, Ny, Nz)

U_new = myh5.read_var(data_file2, '/data', '/data/U', 
                      [[ix_start, iy_start, iz_start], 
                      [ix_end+1, iy_end+1, iz_end+1]], Nx, Ny, Nz)

Uhalf = (U_old + U_new)/2
print('Finished U!')

# Read V
V_old = myh5.read_var(data_file1, '/data', '/data/V', 
                      [[ix_start,iy_start,iz_start], 
                      [ix_end+1, iy_end+1, iz_end+1]], Nx, Ny, Nz)

V_new = myh5.read_var(data_file2, '/data', '/data/V',
                      [[ix_start,iy_start,iz_start], 
                      [ix_end+1, iy_end+1, iz_end+1]], Nx, Ny, Nz)

Vhalf = (V_old + V_new)/2
print('Finished V!')

# Read W
W_old = myh5.read_var(data_file1, '/data', '/data/W', 
                      [[ix_start,iy_start,iz_start], 
                      [ix_end+1, iy_end+1, iz_end+1]], Nx, Ny, Nz)

W_new = myh5.read_var(data_file2, '/data', '/data/W', 
                      [[ix_start,iy_start,iz_start], 
                      [ix_end+1, iy_end+1, iz_end+1]], Nx, Ny, Nz)

Whalf = (W_old + W_new)/2
print('Finished W!')

# Read O2
O2_old = myh5.read_var(data_file1, '/data', '/data/O2', 
                       [[ix_start,iy_start,iz_start], 
                       [ix_end, iy_end, iz_end]], Nx, Ny, Nz)

O2_new = myh5.read_var(data_file2, '/data', '/data/O2', 
                       [[ix_start,iy_start,iz_start], 
                       [ix_end, iy_end, iz_end]], Nx, Ny, Nz)

O2half = (O2_old + O2_new)/2
print('Finished O2!')

# Calculate PROG
PROG_new = 1 - ((O2_new - O2_b) / (O2_u - O2_b))
PROG_old = 1 - ((O2_old - O2_b) / (O2_u - O2_b))

PROGhalf = (PROG_old + PROG_new)/2
dPROG = (PROG_new - PROG_old)/dt
print('Finished PROG!\n')

# x derivative
dx = 20e-6

gC = np.gradient(PROGhalf, dx)

gCx = gC[0]
gCy = gC[1]
gCz = gC[2]

# Prefill arrays with zeros
convU = np.zeros([Nx_c, Ny_c, Nz_c])
convV = np.zeros([Nx_c, Ny_c, Nz_c])
convW = np.zeros([Nx_c, Ny_c, Nz_c])

magGPROG = np.zeros([Nx_c, Ny_c, Nz_c])
disp_sp_PROG = np.zeros([Nx_c, Ny_c, Nz_c])

print(f"gC: {gCx.shape}, {gCy.shape}, {gCz.shape}\n")

# Calculate convective coefficients
for i in range(0, Nx_c):
    for j in range(0, Ny_c):
        for k in range(0, Nz_c):
            convU[i,j,k] = (Uhalf[i+1, j  , k  ] + Uhalf[i,j,k]) / 2*gCx[i,j,k]
            convV[i,j,k] = (Vhalf[i  , j+1, k  ] + Vhalf[i,j,k]) / 2*gCy[i,j,k]
            convW[i,j,k] = (Whalf[i  , j  , k+1] + Whalf[i,j,k]) / 2*gCz[i,j,k]

magGPROG = (gCx**2.0 + gCy**2.0 + gCz**2.0)**0.5

print(f"magGPROG: {magGPROG.shape}")
print(f"dPROG: {dPROG.shape}")
print(f"convU: {convU.shape}")

# Calculate displacement speed
disp_sp_PROG[:,:,:] = (dPROG[:,:,:] + convU[:,:,:] + convV[:,:,:] + 
                       convW[:,:,:]) / magGPROG[:,:,:]

# -----------------------------------------------------------------------------

condition = np.absolute(PROGhalf - 0.73) < (0.2 / 2.0)
disp_PROG_cond = np.extract(condition,disp_sp_PROG)

lam1= np.zeros([Nx_c, Ny_c, Nz_c])
lam2= np.zeros([Nx_c, Ny_c, Nz_c])
lam3= np.zeros([Nx_c, Ny_c, Nz_c])

rr1 = np.zeros([Nx_c, Ny_c, Nz_c,3])
rr2 = np.zeros([Nx_c, Ny_c, Nz_c,3])
rr3 = np.zeros([Nx_c, Ny_c, Nz_c,3])

centerU = np.zeros([Nx_c, Ny_c, Nz_c])
centerV = np.zeros([Nx_c, Ny_c, Nz_c])
centerW = np.zeros([Nx_c, Ny_c, Nz_c])

for i in range(0, Nx_c):
    for j in range(0, Ny_c):
        for k in range(0, Nz_c):
            centerU[i, j, k] = (Uhalf[i+1, j  , k  ] + Uhalf[i, j, k])/2
            centerV[i, j, k] = (Vhalf[i  , j+1, k  ] + Vhalf[i, j, k])/2
            centerW[i, j, k] = (Whalf[i  , j  , k+1] + Whalf[i, j, k])/2

print(f"center_U: {centerU.shape}")
print(f"lambda_1: {lam1.shape}\n")

if IF_save == 1:
    lam1[:,:,:], lam2[:,:,:], lam3[:,:,:], \
    rr1[:,:,:,:], rr2[:,:,:,:], rr3[:,:,:,:] = myeig.vec_val(centerU[:,:,:], 
         centerV[:,:,:], centerW[:,:,:], dx)

    f1 = h5py.File("data_disp_sp.hdf5", "w")

    dset1 = f1.create_dataset("lam1", (Nx_c,Ny_c,Nz_c), data=lam1)
    dset2 = f1.create_dataset("lam2", (Nx_c,Ny_c,Nz_c), data=lam2)
    dset3 = f1.create_dataset("lam3", (Nx_c,Ny_c,Nz_c), data=lam3)

    dset4 = f1.create_dataset("rr1", (Nx_c,Ny_c,Nz_c,3), data=rr1)
    dset5 = f1.create_dataset("rr2", (Nx_c,Ny_c,Nz_c,3), data=rr2)
    dset6 = f1.create_dataset("rr3", (Nx_c,Ny_c,Nz_c,3), data=rr3)

    print("Calculated and saved Lambda!\n")

elif IF_save == 0:
    f1 = h5py.File('data_disp_sp.hdf5', 'r')

    lam1 = np.array(f1['lam1'])
    lam2 = np.array(f1['lam2'])
    lam3 = np.array(f1['lam3'])

    rr1 = np.array(f1['rr1'])
    rr2 = np.array(f1['rr2'])
    rr3 = np.array(f1['rr3'])

    print("Imported Lambda!\n")

lam1_cond = np.extract(condition, lam1)
lam2_cond = np.extract(condition, lam2)
lam3_cond = np.extract(condition, lam3)

lam1_cond_flat = ndarray.flatten(lam1_cond)
lam2_cond_flat = ndarray.flatten(lam2_cond)
lam3_cond_flat = ndarray.flatten(lam3_cond)

# disp_sp_PROG_flat = ndarray.flatten(disp_sp_PROG)
disp_PROG_cond_flat = ndarray.flatten(disp_PROG_cond)
print(f"lambda_1 cond flat: {lam1_cond_flat.shape}")
print(f"disp_PROG cond flat: {disp_PROG_cond_flat.shape}\n")

bin_edges_jpdf_lam = np.linspace(-15e4, 15e4, 60)
bin_edges_jpdf_disp_sp_PROG = np.linspace(-15, 15, 60)

lam1_disp_sp_PROG_jpdf, lam_bin_edges, disp_bin_edges = np.histogram2d(
    lam1_cond_flat, disp_PROG_cond_flat, bins=(
    bin_edges_jpdf_lam,bin_edges_jpdf_disp_sp_PROG), density=True)

lam_jpdf_bin = 0.5*(lam_bin_edges[:-1] + lam_bin_edges[1:])
disp_jpdf_bin = 0.5*(disp_bin_edges[:-1] + disp_bin_edges[1:])

lam2_disp_sp_PROG_jpdf, lam_bin_edges, disp_bin_edges = np.histogram2d(
    lam2_cond_flat, disp_PROG_cond_flat, bins=(
    bin_edges_jpdf_lam,bin_edges_jpdf_disp_sp_PROG), density=True)

lam_jpdf_bin = 0.5*(lam_bin_edges[:-1] + lam_bin_edges[1:])
disp_jpdf_bin = 0.5*(disp_bin_edges[:-1] + disp_bin_edges[1:])

lam3_disp_sp_PROG_jpdf, lam_bin_edges, disp_bin_edges = np.histogram2d(
    lam3_cond_flat, disp_PROG_cond_flat, 
    bins=(bin_edges_jpdf_lam,bin_edges_jpdf_disp_sp_PROG), density=True)

lam_jpdf_bin = 0.5*(lam_bin_edges[:-1] + lam_bin_edges[1:])
disp_jpdf_bin = 0.5*(disp_bin_edges[:-1] + disp_bin_edges[1:])

f1 = h5py.File("data_disp_speed.hdf5", "w")
dset1 = f1.create_dataset("dataset_disp_sp_PROG", (Nx_c, Ny_c, Nz_c), 
                          dtype='i', data=disp_sp_PROG)

bin_edges_pdf = np.linspace(-1e2, 1e2, 60)
bin_c_cond = np.linspace(0.725, 0.735, 1)

d_bin_c_cond = 0.01
[pdf_disp_sp_cond, bin_pdf_disp_sp_cond] = mystat.cond_pdf(disp_sp_PROG[:,:,:], 
    PROGhalf[:,:,:], bin_edges_pdf,bin_c_cond, d_bin_c_cond)

bin_edges_pdf_lam = np.linspace(-1e6,1e6,400)
[pdf_lam1_cond, bin_pdf_lam1_cond] = mystat.cond_pdf(lam1[:,:,:], 
    PROGhalf[:,:,:], bin_edges_pdf_lam,bin_c_cond,d_bin_c_cond)

bin_disp_sp = np.linspace(-9, 14, 20)
d_bin_disp_sp = 1/20

NC = len(bin_disp_sp)

lam1_cond_mean = np.zeros([NC])
lam2_cond_mean = np.zeros([NC])
lam3_cond_mean = np.zeros([NC])

for i in range(0, NC):
    print(f"iteration: {i}, bin displacement speed: {bin_disp_sp[i]}")

    condition = np.absolute(disp_PROG_cond_flat -
                            bin_disp_sp[i]) <  d_bin_disp_sp / 2.0

    ext = np.extract(condition, lam1_cond_flat)
    mean = np.mean(ext)
    lam1_cond_mean[i] = mean

    ext = np.extract(condition, lam2_cond_flat)
    mean = np.mean(ext)
    lam2_cond_mean[i] = mean

    ext = np.extract(condition, lam3_cond_flat)
    mean = np.mean(ext)
    lam3_cond_mean[i] = mean

# -----------------------------------------------------------------------------

# Contour plot of displacement speed
plt.figure(1)
plt.contourf(disp_sp_PROG[:,:,1])
plt.xlabel('y-coordinate')
plt.ylabel('x-coordinate') 
plt.colorbar(label=r'Displacement Speed, $\rmS_{d}$')
plt.style.use('seaborn')
plt.show()

#plt.figure(2)
#for j in range(0, len(pdf_disp_sp_cond[:,0])):
#    plt.plot(bin_pdf_disp_sp_cond, pdf_disp_sp_cond[j,:])
#
## Colormap
#cmap=plt.cm.get_cmap('Blues')
#cmap.set_under('white')
#
## Probability density function of displacement speed
#plt.figure(3)
#plt.plot(bin_pdf_disp_sp_cond,pdf_disp_sp_cond[0,:])
#plt.ylabel('Probability Density Function')
#plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
#plt.xlim(-15, 15)
#plt.margins(x=0)
#plt.margins(y=0)
#plt.show()
#
## Joint probability density function of compressive strain tensor
#plt.figure(4)
#
#plt.contourf(disp_jpdf_bin, lam_jpdf_bin,lam1_disp_sp_PROG_jpdf, cmap=cmap, 
#             vmin=0.075e-6, levels=10)
#
#plt.plot(bin_disp_sp, lam1_cond_mean[:], color='r',
#         label=r'Mean Compressive Strain Tensor, $\rm\gamma$')
#
#plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
#plt.ylabel(r'Compressive Strain Tensor, $\rm\gamma$')
#plt.colorbar(label='Joint Probability Density Function')
#plt.legend(loc ="upper left", prop={'size': 12})
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.margins(x=0)
#plt.margins(y=0)
#plt.subplots_adjust(left=0.2, bottom=0.1, right=0.95, top=0.95)
#plt.show()
# 
## Joint probability density function of intermediate strain tensor
#plt.figure(5)
#
#plt.contourf(disp_jpdf_bin, lam_jpdf_bin, lam2_disp_sp_PROG_jpdf, cmap=cmap, 
#             vmin=0.1e-6, levels=10)
#
#plt.plot(bin_disp_sp, lam2_cond_mean[:], color='r', 
#         label=r'Mean Intermediate Strain Tensor, $\rm\beta$')
#
#plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
#plt.ylabel(r'Intermediate Strain Tensor, $\rm\beta$')
#plt.colorbar(label='Joint Probability Density Function')
#plt.legend(loc="upper left", prop={'size': 12})
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.margins(x=0)
#plt.margins(y=0)
#plt.subplots_adjust(left=0.2, bottom=0.1, right=0.95, top=0.95)
#plt.show()
#
## Joint probability density function of extensive strain tensor
#plt.figure(6)
#
#plt.contourf(disp_jpdf_bin, lam_jpdf_bin,lam3_disp_sp_PROG_jpdf, cmap=cmap, 
#             vmin=0.075e-6, levels=10)
#
#plt.plot(bin_disp_sp,lam3_cond_mean[:], color='r',
#         label=r'Mean Extensive Strain Tensor $\rm\alpha$')
#
#plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
#plt.ylabel(r'Extensive Strain Tensor, $\rm\alpha$')
#plt.colorbar(label='Joint Probability Density Function')
#plt.legend(loc ="lower left", prop={'size': 12})
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.margins(x=0)
#plt.margins(y=0)
#plt.subplots_adjust(left=0.2, bottom=0.1, right=0.95, top=0.95)
#plt.show()

# Print finish
print("\nFinished!\n")
print("\n----\n")

