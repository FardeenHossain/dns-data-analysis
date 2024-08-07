import my_stat
import numpy as np
from config import flame


def calc_disp_speed_pdf(c_half, s_d):
    # Bin spacing
    bin_edges_pdf = np.linspace(-1e2, 1e2, 200)
    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    # Calculate PDF
    s_d_pdf, s_d_bin_pdf = my_stat.cond_pdf(
        s_d, c_half, bin_edges_pdf, bin_c_cond, d_bin_c_cond
    )

    return [s_d_pdf, s_d_bin_pdf]


def calc_strain_rate_pdf(c_half, lambda1, lambda2, lambda3):
    # Bin spacing
    bin_edges_pdf = np.linspace(-1e6, 1e6, 200)
    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    # Calculate compressive strain rate PDF
    lambda1_pdf, lambda1_pdf_bin = my_stat.cond_pdf(
        lambda1, c_half, bin_edges_pdf, bin_c_cond, d_bin_c_cond
    )

    # Calculate intermediate strain rate PDF
    lambda2_pdf, lambda2_pdf_bin = my_stat.cond_pdf(
        lambda2, c_half, bin_edges_pdf, bin_c_cond, d_bin_c_cond
    )

    # Calculate extensive strain rate PDF
    lambda3_pdf, lambda3_pdf_bin = my_stat.cond_pdf(
        lambda3, c_half, bin_edges_pdf, bin_c_cond, d_bin_c_cond
    )

    return [
        lambda1_pdf,
        lambda1_pdf_bin,
        lambda2_pdf,
        lambda2_pdf_bin,
        lambda3_pdf,
        lambda3_pdf_bin,
    ]


def calc_disp_speed_prog_var_jpdf(c_half, s_d):
    # Bin spacing
    bin_c_half = np.linspace(0.0, 1.0, 100)
    bin_s_d = np.linspace(-1e2, 1e2, 100)

    # Calculate JPDF
    [s_d_c_half_jpdf, s_d_c_half_jpdf_bin_x, s_d_c_half_jpdf_bin_y] = my_stat.pdf2d(
        s_d, c_half, bin_s_d, bin_c_half
    )

    return [s_d_c_half_jpdf, s_d_c_half_jpdf_bin_x, s_d_c_half_jpdf_bin_y]


def calc_disp_speed_curvature_jpdf(c_half, s_d, k):
    # Bin spacing
    k_bin_edges_pdf = np.linspace(-5e4, 5e4, 200)
    s_d_bin_edges_pdf = np.linspace(-1e2, 1e2, 200)

    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    # Calculate JPDF
    [s_d_k_jpdf, s_d_k_jpdf_bin_x, s_d_k_jpdf_bin_y] = my_stat.cond_pdf2d(
        k, s_d, c_half, k_bin_edges_pdf, s_d_bin_edges_pdf, bin_c_cond, d_bin_c_cond
    )

    print("Finished displacement speed curvature JPDF!")

    return [s_d_k_jpdf, s_d_k_jpdf_bin_x, s_d_k_jpdf_bin_y]


def calc_strain_rate_jpdf(c_half, s_d, lambda1, lambda2, lambda3):
    # Bin spacing
    if flame == "R1K1":
        lambda_bin_edges_pdf = np.linspace(-4e5, 4e5, 200)
    if flame == "R2K1":
        lambda_bin_edges_pdf = np.linspace(-3e5, 3e5, 200)
    if flame == "R3K1":
        lambda_bin_edges_pdf = np.linspace(-2e5, 2e5, 200)
    if flame == "R4K1":
        lambda_bin_edges_pdf = np.linspace(-2e5, 2e5, 200)

    s_d_bin_edges_pdf = np.linspace(-1e2, 1e2, 200)

    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    # Calculate compressive strain rate JPDF
    [lambda1_jpdf, lambda1_jpdf_bin_x, lambda1_jpdf_bin_y] = my_stat.cond_pdf2d(
        lambda1,
        s_d,
        c_half,
        lambda_bin_edges_pdf,
        s_d_bin_edges_pdf,
        bin_c_cond,
        d_bin_c_cond,
    )

    # Calculate intermediate strain rate JPDF
    [lambda2_jpdf, lambda2_jpdf_bin_x, lambda2_jpdf_bin_y] = my_stat.cond_pdf2d(
        lambda2,
        s_d,
        c_half,
        lambda_bin_edges_pdf,
        s_d_bin_edges_pdf,
        bin_c_cond,
        d_bin_c_cond,
    )

    # Calculate extensive strain rate JPDF
    [lambda3_jpdf, lambda3_jpdf_bin_x, lambda3_jpdf_bin_y] = my_stat.cond_pdf2d(
        lambda3,
        s_d,
        c_half,
        lambda_bin_edges_pdf,
        s_d_bin_edges_pdf,
        bin_c_cond,
        d_bin_c_cond,
    )

    return [
        lambda1_jpdf,
        lambda1_jpdf_bin_x,
        lambda1_jpdf_bin_y,
        lambda2_jpdf,
        lambda2_jpdf_bin_x,
        lambda2_jpdf_bin_y,
        lambda3_jpdf,
        lambda3_jpdf_bin_x,
        lambda3_jpdf_bin_y,
    ]


def calc_disp_speed_cond_mean(c_half, s_d):
    # Bin spacing
    bin_c_cond = np.linspace(0.0, 1.0, 100)
    d_bin_c_cond = 0.1

    # Calculate conditional mean
    [bin_c_cond, s_d_cond_mean] = my_stat.cond_mean(
        s_d, c_half, bin_c_cond, d_bin_c_cond
    )

    return [bin_c_cond, s_d_cond_mean]


def calc_lambda_c_cond_mean(c_half, s_d, lambda1, lambda2, lambda3):
    # Bin spacing
    bin_c_cond = [0.1, 0.3, 0.5, 0.73, 0.9]
    d_bin_c_cond = 0.1

    bin_s_d = np.linspace(-15, 15, 100)
    d_bin_s_d = 0.1

    # Calculate conditional mean
    [bin_s_d, lambda1_cond_mean] = my_stat.cond_mean_c(
        lambda1, s_d, c_half, bin_s_d, bin_c_cond, d_bin_s_d, d_bin_c_cond
    )

    [bin_s_d, lambda2_cond_mean] = my_stat.cond_mean_c(
        lambda2, s_d, c_half, bin_s_d, bin_c_cond, d_bin_s_d, d_bin_c_cond
    )

    [bin_s_d, lambda3_cond_mean] = my_stat.cond_mean_c(
        lambda3, s_d, c_half, bin_s_d, bin_c_cond, d_bin_s_d, d_bin_c_cond
    )

    return [bin_s_d, lambda1_cond_mean, lambda2_cond_mean, lambda3_cond_mean]
