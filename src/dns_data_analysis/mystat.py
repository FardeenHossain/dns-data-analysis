import numpy as np


def cond_pdf(q, c, bin_edges_pdf, bin_c_cond, d_bin_c_cond):
    bin_c_pdf = 0.5 * (bin_edges_pdf[:-1] + bin_edges_pdf[1:])

    nc = len(bin_c_cond)
    nb = len(bin_c_pdf)

    pdf_cond = np.zeros([nc, nb])

    for j in range(0, nc):
        cond = np.absolute(c - bin_c_cond[j]) < d_bin_c_cond / 2.0

        q_cond = np.extract(cond, q)

        pdf, dum = np.histogram(q_cond, bins=bin_edges_pdf, density=True)
        pdf_cond[j, :] = pdf

    return [pdf_cond, bin_c_pdf]


def cond_pdf2d(q1, q2, c, bin_edges_pdf1, bin_edges_pdf2, bin_c_cond,
               d_bin_c_cond):
    bin_c_pdf1 = 0.5 * (bin_edges_pdf1[:-1] + bin_edges_pdf1[1:])
    bin_c_pdf2 = 0.5 * (bin_edges_pdf2[:-1] + bin_edges_pdf2[1:])

    nc = len(bin_c_cond)
    nb1 = len(bin_c_pdf1)
    nb2 = len(bin_c_pdf2)

    pdf2d_cond = np.zeros([nc, nb1, nb2])

    for j in range(0, nc):
        cond = np.absolute(c - bin_c_cond[j]) < d_bin_c_cond / 2.0

        q1_cond = np.extract(cond, q1)
        q2_cond = np.extract(cond, q2)

        q1_cond_flat = np.ndarray.flatten(q1_cond)
        q2_cond_flat = np.ndarray.flatten(q2_cond)

        pdf, x_edges, y_edges = np.histogram2d(q1_cond_flat, q2_cond_flat,
                                               bins=(bin_edges_pdf1,
                                                     bin_edges_pdf2),
                                               density=True)

        pdf2d_cond[j, :, :] = pdf

    return [pdf2d_cond, bin_c_pdf1, bin_edges_pdf2]
