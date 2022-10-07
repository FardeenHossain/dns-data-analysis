import h5py
import numpy as np
import math

# [gUx,gUy,gUz,gVx,gVy,gVz,gWx,gWy,gWz] = ...vel_grad(U,V,W,dx)

def vel_grad(U,V,W,dx):
    
    # Compute gradient of U
    gC = np.gradient(U,dx)
    gUx = gC[0]
    gUy = gC[1]
    gUz = gC[2]

    # Compute gradient of V
    gC = np.gradient(V,dx)
    gVx = gC[0]
    gVy = gC[1]
    gVz = gC[2]

    # Compute gradient of W
    gC = np.gradient(W,dx)
    gWx = gC[0]
    gWy = gC[1]
    gWz = gC[2]
    
    return [gUx,gUy,gUz,gVx,gVy,gVz,gWx,gWy,gWz]
