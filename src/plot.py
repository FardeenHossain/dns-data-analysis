import matplotlib.pyplot as plt


def plot_prog_var(c_half):
    """Contour plot of progress variable."""

    plt.figure(1)
    plt.contourf(c_half[:, :, 1], cmap='plasma')
    plt.xlabel('Y-Coordinate')
    plt.ylabel('X-Coordinate')
    plt.colorbar(label='Progress Variable, C (-)')
    plt.show()


def plot_disp_speed(s_d):
    """Contour plot of displacement speed."""

    plt.figure(2)
    plt.contourf(s_d[:, :, 1], cmap='Spectral')
    plt.xlabel('Y-Coordinate')
    plt.ylabel('X-Coordinate')
    plt.colorbar(label=r'Displacement Speed, $\rmS_{d}$')
    plt.show()


def plot_disp_speed_pdf(s_d_pdf, s_d_bin_pdf):
    """Probability density function of displacement speed."""

    plt.figure(3)
    plt.style.use('seaborn')
    for i in range(0, len(s_d_pdf[:, 0])):
        plt.plot(s_d_bin_pdf, s_d_pdf[i, :])
    plt.ylabel('Probability Density Function, PDF')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.xlim(-15, 15)
    plt.ylim(0.0, 0.1)
    plt.show()


def plot_comp_strain_tensor_jpdf(lambda1_bin_pdf, lambda1_pdf,
                                 lambda1_cond_mean, s_d_bin_pdf1,
                                 s_d_bin_pdf_cond):
    """Joint probability density function of compressive strain tensor."""

    plt.figure(5)
    plt.contourf(s_d_bin_pdf1, lambda1_bin_pdf, lambda1_pdf,
                 cmap='inferno')
    plt.plot(s_d_bin_pdf_cond, lambda1_cond_mean[:], color='w',
             label=r'Mean Compressive Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Compressive Strain Rate Tensor, $\rm\gamma$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='upper right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()


def plot_int_strain_tensor_jpdf(lambda2_bin_pdf, lambda2_pdf,
                                lambda2_cond_mean, s_d_bin_pdf2,
                                s_d_bin_pdf):
    """Joint probability density function of intermediate strain tensor."""

    plt.figure(6)
    plt.contourf(s_d_bin_pdf2, lambda2_bin_pdf, lambda2_pdf,
                 cmap='inferno')
    plt.plot(s_d_bin_pdf, lambda2_cond_mean[:], color='w',
             label=r'Mean Intermediate Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Intermediate Strain Rate Tensor, $\rm\beta$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='upper right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()


def plot_ext_strain_tensor_jpdf(lambda3_bin_pdf, lambda3_pdf,
                                lambda3_cond_mean, s_d_bin_pdf2,
                                s_d_bin_pdf):
    """Joint probability density function of extensive strain tensor."""

    plt.figure(7)
    plt.contourf(s_d_bin_pdf2, lambda3_bin_pdf, lambda3_pdf,
                 cmap='inferno')
    plt.plot(s_d_bin_pdf, lambda3_cond_mean[:], color='w',
             label=r'Mean Extensive Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Extensive Strain Rate Tensor, $\rm\alpha$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='lower right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()
