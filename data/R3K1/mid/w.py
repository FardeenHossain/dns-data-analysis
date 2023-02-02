import h5py
import matplotlib.pyplot as plt

filename = 'data_1.800E-03_prate.h5'
with h5py.File(filename, 'r') as f:
    O2 = f['/data/O2'][:]
    O2_p = f['/data/source_O2'][:]

print(O2.shape)

plt.plot(O2[:,:,1],O2_p[:,:,1],'.')
plt.show()
