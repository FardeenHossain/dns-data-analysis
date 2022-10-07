# Quick Plot Script

import h5py
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import sys
import os
from operator import itemgetter
import myh5

from numpy import linalg as LA

f1 = h5py.File('data_disp_sp.hdf5', 'r')
disp_sp_PROG = f1['dataset_disp_sp_PROG']

plt.figure(1)
plt.contourf(disp_sp_PROG[:,:,1])
plt.title('Contour plot of Displacement Speed')
plt.xlabel('Y Coordinate')
plt.ylabel('X Coordinate') 
plt.colorbar(label = 'Displacement Speed')
plt.show()


#hpcwork/itv/Antonio/Fergus/ImportedCode/Displacement\ Speed/data_disp_sp.hdf5
