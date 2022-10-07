import h5py
import numpy as np
import math
from numpy import linalg as LA

import mygrad

# [lam1,lam2,lam3,rr1,rr2,rr3] = myeig.vec_val(U,V,W,dx):

def vec_val(U,V,W,dx):
    
    [gUx,gUy,gUz,gVx,gVy,gVz,gWx,gWy,gWz] = mygrad.vel_grad(U,V,W,dx)
    
    Nx = len(U[:,1,1])
    Ny = len(V[1,:,1])
    Nz = len(W[1,1,:])
    
    lam1 = np.zeros([Nx,Ny,Nz])
    lam2 = np.zeros([Nx,Ny,Nz])
    lam3 = np.zeros([Nx,Ny,Nz])
    rr1 = np.zeros([Nx,Ny,Nz,3])
    rr2 = np.zeros([Nx,Ny,Nz,3])
    rr3 = np.zeros([Nx,Ny,Nz,3])
    BB = np.zeros([4,3])
    for i in range(0,Nx):
        print('Compute Eigen',i,Nx)
        for j in range(0,Ny):
            for k in range(0,Nz):
                # MM is the velocity gradient A
                MM = [ [gUx[i,j,k],gUy[i,j,k],gUz[i,j,k]] , [gVx[i,j,k],gVy[i,j,k],gVz[i,j,k]] , [gWx[i,j,k],gWy[i,j,k],gWz[i,j,k]] ]
                # MM2 is the strain tensor S=0.5(A+A_transpose)
                MM2 = 0.5*(MM + np.transpose(MM))
                lam, rr = LA.eig(MM2)
                
                BB[0,0] = lam[0]
                BB[0,1] = lam[1]
                BB[0,2] = lam[2]
                
                BB[1:,0] = rr[:,0]
                BB[1:,1] = rr[:,1]
                BB[1:,2] = rr[:,2]
                
                BB2 = np.transpose(BB)
                
                rowIndex=0
                BB_sort = BB2[BB2[:,0].argsort()]
                
                r1 = BB_sort[0,1:]
                r2 = BB_sort[1,1:]
                r3 = BB_sort[2,1:]
                
                rr1[i,j,k,:] = r1
                rr2[i,j,k,:] = r2
                rr3[i,j,k,:] = r3
                
                lam1[i,j,k] = BB_sort[0,0]
                lam2[i,j,k] = BB_sort[1,0]
                lam3[i,j,k] = BB_sort[2,0]
    return [lam1,lam2,lam3,rr1,rr2,rr3]
                