import matplotlib.pyplot as plt


def plot_prog_var(c_half):
    """Contour plot of progress variable."""

    plt.figure(1)
    plt.contourf(c_half[:, :, 0], cmap='plasma')
    plt.xlabel('Y-Coordinate')
    plt.ylabel('X-Coordinate')
    plt.colorbar(label='Progress Variable, C (-)')
    plt.show()


def plot_disp_speed(s_d):
    """Contour plot of displacement speed."""

    plt.figure(2)
    plt.contourf(s_d[:, :, 0], cmap='Spectral')
    plt.xlabel('Y-Coordinate')
    plt.ylabel('X-Coordinate')
    plt.colorbar(label=r'Displacement Speed, $\rmS_{d}$')
    plt.show()


def plot_disp_speed_pdf(s_d_pdf, s_d_pdf_bin):
    """Probability density function of displacement speed."""

    plt.figure(3)
    plt.style.use('seaborn')
    for i in range(0, len(s_d_pdf[:, 0])):
        plt.plot(s_d_pdf_bin, s_d_pdf[i, :])
    plt.ylabel('Probability Density Function, PDF')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.xlim(-15, 15)
    plt.ylim(0.0, 0.1)
    plt.show()


def plot_strain_rate_pdf(lambda1_pdf, lambda1_pdf_bin, lambda2_pdf,
                         lambda2_pdf_bin, lambda3_pdf, lambda3_pdf_bin):
    """Probability density function of strain rate tensor."""

    plt.figure(4)
    plt.style.use('seaborn')
    for i in range(0, len(lambda1_pdf[:, 0])):
        plt.plot(lambda1_pdf_bin, lambda1_pdf[i, :], label=r'$\rm\alpha$')
    for i in range(0, len(lambda2_pdf[:, 0])):
        plt.plot(lambda2_pdf_bin, lambda2_pdf[i, :], label=r'$\rm\beta$')
    for i in range(0, len(lambda3_pdf[:, 0])):
        plt.plot(lambda3_pdf_bin, lambda3_pdf[i, :], label=r'$\rm\gamma$')
    plt.ylabel('Probability Density Function, PDF')
    plt.xlabel(r'Strain Rate Tensor')
    plt.xlim(-5e5, 5e5)
    plt.ylim(0, 3e-5)
    plt.show()


def plot_comp_strain_rate_jpdf(lambda1_jpdf, lambda1_jpdf_bin,
                               lambda1_mean, s_d_jpdf_bin,
                               s_d_mean_bin):
    """Joint probability density function of compressive strain rate tensor."""

    plt.figure(5)
    plt.contourf(s_d_jpdf_bin, lambda1_jpdf_bin, lambda1_jpdf,
                 cmap='inferno')
    plt.plot(s_d_mean_bin, lambda1_mean[:], color='w',
             label=r'Mean Compressive Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Compressive Strain Rate Tensor, $\rm\gamma$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='upper right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()


def plot_int_strain_rate_jpdf(lambda2_jpdf, lambda2_jpdf_bin,
                              lambda2_mean, s_d_jpdf_bin,
                              s_d_mean_bin):
    """Joint probability density function of intermediate strain rate
    tensor."""

    plt.figure(6)
    plt.contourf(s_d_jpdf_bin, lambda2_jpdf_bin, lambda2_jpdf,
                 cmap='inferno')
    plt.plot(s_d_mean_bin, lambda2_mean[:], color='w',
             label=r'Mean Intermediate Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Intermediate Strain Rate Tensor, $\rm\beta$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='upper right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()


def plot_ext_strain_rate_jpdf(lambda3_jpdf, lambda3_jpdf_bin,
                              lambda3_mean, s_d_jpdf_bin,
                              s_d_mean_bin):
    """Joint probability density function of extensive strain rate tensor."""

    plt.figure(7)
    plt.contourf(s_d_jpdf_bin, lambda3_jpdf_bin, lambda3_jpdf,
                 cmap='inferno')
    plt.plot(s_d_mean_bin, lambda3_mean[:], color='w',
             label=r'Mean Extensive Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Extensive Strain Rate Tensor, $\rm\alpha$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='lower right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()
