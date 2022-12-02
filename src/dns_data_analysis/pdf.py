import numpy as np
import mystat


def calc_disp_speed_pdf(c_half, s_d):
    """Calculate displacement speed probability density function."""

    # Bin spacing
    bin_edges_pdf = np.linspace(-1e2, 1e2, 100)
    bin_c_cond = np.linspace(0.1, 0.9, 5)
    d_bin_c_cond = 0.01

    # Calculate displacement speed PDF
    s_d_pdf, s_d_bin_pdf = mystat.cond_pdf(s_d, c_half, bin_edges_pdf,
                                           bin_c_cond, d_bin_c_cond)

    print("Finished displacement speed PDF!")

    return [s_d_pdf, s_d_bin_pdf]


def calc_strain_rate_pdf(c_half, lambda1, lambda2, lambda3):
    """Calculate strain rate tensor eigenvalues probability density
    function."""

    # Bin spacing
    bin_edges_pdf = np.linspace(-1e6, 1e6, 100)
    bin_c_cond = np.linspace(0.1, 0.9, 5)
    d_bin_c_cond = 0.01

    # Calculate compressive strain rate tensor PDF
    lambda1_pdf, lambda1_pdf_bin = mystat.cond_pdf(lambda1, c_half,
                                                   bin_edges_pdf,
                                                   bin_c_cond,
                                                   d_bin_c_cond)

    # Calculate intermediate strain rate tensor PDF
    lambda2_pdf, lambda2_pdf_bin = mystat.cond_pdf(lambda2, c_half,
                                                   bin_edges_pdf,
                                                   bin_c_cond,
                                                   d_bin_c_cond)

    # Calculate extensive strain rate tensor PDF
    lambda3_pdf, lambda3_pdf_bin = mystat.cond_pdf(lambda3, c_half,
                                                   bin_edges_pdf,
                                                   bin_c_cond,
                                                   d_bin_c_cond)

    print("Finished strain rate tensor PDF!")

    return [lambda1_pdf, lambda1_pdf_bin, lambda2_pdf, lambda2_pdf_bin,
            lambda3_pdf, lambda3_pdf_bin]


def calc_strain_rate_jpdf(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate strain rate tensor eigenvalues joint probability density
    function."""

    # Bin spacing
    lambda_bin_edges_pdf = np.linspace(-1.5e5, 1.5e5, 100)
    s_d_bin_edges_pdf = np.linspace(-15, 15, 100)
    bin_c_cond = np.linspace(0.1, 0.9, 5)
    d_bin_c_cond = 0.2

    # Calculate compressive strain rate tensor PDF
    [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y] = mystat.cond_pdf2d(
        lambda1, s_d, c_half, lambda_bin_edges_pdf, s_d_bin_edges_pdf,
        bin_c_cond, d_bin_c_cond)

    # Calculate intermediate strain rate tensor PDF
    [lambda2_jpdf, lambda2_jpdf_bin_x, lambda2_jpdf_bin_y] = mystat.cond_pdf2d(
        lambda2, s_d, c_half, lambda_bin_edges_pdf, s_d_bin_edges_pdf,
        bin_c_cond, d_bin_c_cond)

    # Calculate extensive strain rate tensor PDF
    [lambda3_jpdf, lambda3_jpdf_bin_x, lambda3_jpdf_bin_y] = mystat.cond_pdf2d(
        lambda3, s_d, c_half, lambda_bin_edges_pdf, s_d_bin_edges_pdf,
        bin_c_cond, d_bin_c_cond)

    print("Finished strain rate tensor JPDF!")

    return [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y, lambda2_jpdf,
            lambda2_jpdf_bin_x, lambda2_jpdf_bin_y, lambda3_jpdf,
            lambda3_jpdf_bin_x, lambda3_jpdf_bin_y]


def calc_cond_mean(c_half, s_d, lambda1, lambda2, lambda3):
    """Calculate conditional mean of displacement speed and """

    bin_c_cond = np.linspace(0.1, 0.9, 5)
    d_bin_c_cond = 0.01
    nc = len(bin_c_cond)

    # Condition
    for j in range(0, nc):
        cond = np.absolute(c_half - bin_c_cond[j]) < d_bin_c_cond / 2.0

    # Extract condition
    s_d_cond = np.extract(cond, s_d)
    lambda1_cond = np.extract(cond, lambda1)
    lambda2_cond = np.extract(cond, lambda2)
    lambda3_cond = np.extract(cond, lambda3)

    # Flatten array
    s_d_cond_flat = np.ndarray.flatten(s_d_cond)
    lambda1_flat = np.ndarray.flatten(lambda1_cond)
    lambda2_flat = np.ndarray.flatten(lambda2_cond)
    lambda3_flat = np.ndarray.flatten(lambda3_cond)

    bin_s_d = np.linspace(-9, 14, 20)
    d_bin_s_d = 1 / 20
    nc = len(bin_s_d)

    # Initialise arrays with zeros
    lambda1_cond_mean = np.zeros([nc])
    lambda2_cond_mean = np.zeros([nc])
    lambda3_cond_mean = np.zeros([nc])

    for i in range(0, nc):
        cond = np.absolute(s_d_cond_flat - bin_s_d[i]) < d_bin_s_d / 2.0

        lambda1_extract = np.extract(cond, lambda1_flat)
        lambda1_cond_mean[i] = np.mean(lambda1_extract)

        lambda2_extract = np.extract(cond, lambda2_flat)
        lambda2_cond_mean[i] = np.mean(lambda2_extract)

        lambda3_extract = np.extract(cond, lambda3_flat)
        lambda3_cond_mean[i] = np.mean(lambda3_extract)

    return [bin_s_d, lambda1_cond_mean, lambda2_cond_mean, lambda3_cond_mean]
