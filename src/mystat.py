import h5py
import numpy as np
import math


def cond_pdf(q,c,bin_edges_pdf,bin_c_cond,d_bin_c_cond):

    bin_c_pdf = 0.5*(bin_edges_pdf[:-1]+bin_edges_pdf[1:])
  
    Nc = len(bin_c_cond)
    Nb = len(bin_c_pdf)

    pdf_cond = np.zeros([Nc,Nb])

    print(Nc)

    for j in range(0,Nc):
        print(j,bin_c_cond[j])
        condition = np.absolute(c-bin_c_cond[j])<d_bin_c_cond/2.0
        q_c = np.extract(condition,q)
        pdf , dum = np.histogram(q_c,bins=bin_edges_pdf, density=True)
        pdf_cond[j,:] = pdf

    return [pdf_cond,bin_c_pdf]


def cond_pdf2D(q1,q2,c,bin_edges_pdf,bin_c_cond,d_bin_c_cond):
    
    bin_c_pdf = 0.5*(bin_edges_pdf[:-1]+bin_edges_pdf[1:])
    
    Nc = len(bin_c_cond)
    Nb = len(bin_c_pdf)

    pdf2d_cond = np.zeros([Nc,Nb,Nb])
    
    print(Nc)

    for j in range(0,Nc):
        print(j,bin_c_cond[j])
        condition = np.absolute(c-bin_c_cond[j])<d_bin_c_cond/2.0
        q1_c = np.extract(condition,q1)
        q2_c = np.extract(condition,q2)
        pdf , x_edges, y_edges = np.histogram2d(q1_c,q2_c,bins=(bin_edges_pdf,bin_edges_pdf), density=True)
        pdf2d_cond[j,:,:] = pdf

    return [pdf2d_cond,bin_c_pdf]

