import matplotlib.pyplot as plt


def plot_prog_var(prog_var):
    """Contour plot of progress variable."""

    plt.figure(1)
    plt.contourf(prog_var[:, :, 1], cmap='plasma')
    plt.xlabel('Y-Coordinate')
    plt.ylabel('X-Coordinate')
    plt.colorbar(label='Progress Variable, C (-)')
    plt.show()


def plot_disp_speed(disp_speed):
    """Contour plot of displacement speed."""

    plt.figure(2)
    plt.contourf(disp_speed[:, :, 1], cmap='Spectral')
    plt.xlabel('Y-Coordinate')
    plt.ylabel('X-Coordinate')
    plt.colorbar(label=r'Displacement Speed, $\rmS_{d}$')
    plt.show()


def plot_disp_speed_pdf(pdf_disp_speed_cond, bin_pdf_disp_speed_cond):
    """Probability density function of displacement speed."""

    plt.figure(3)
    plt.style.use('seaborn')
    for i in range(0, len(pdf_disp_speed_cond[:, 0])):
        plt.plot(bin_pdf_disp_speed_cond, pdf_disp_speed_cond[i, :])
    plt.ylabel('Probability Density Function, PDF')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.xlim(-15, 15)
    plt.ylim(0.0, 0.1)
    plt.show()


def plot_comp_strain_tensor_jpdf(lambda1_jpdf_bin, lambda1_disp_speed_c_jpdf,
                                 lambda1_cond_mean, disp1_jpdf_bin,
                                 bin_disp_speed):
    """Joint probability density function of compressive strain tensor."""

    plt.figure(5)
    plt.contourf(disp1_jpdf_bin, lambda1_jpdf_bin, lambda1_disp_speed_c_jpdf,
                 cmap='inferno')
    plt.plot(bin_disp_speed, lambda1_cond_mean[:], color='w',
             label=r'Mean Compressive Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Compressive Strain Rate Tensor, $\rm\gamma$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='upper right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()


def plot_int_strain_tensor_jpdf(lambda2_jpdf_bin, lambda2_disp_speed_c_jpdf,
                                lambda2_cond_mean, disp2_jpdf_bin,
                                bin_disp_speed):
    """Joint probability density function of intermediate strain tensor."""

    plt.figure(6)
    plt.contourf(disp2_jpdf_bin, lambda2_jpdf_bin, lambda2_disp_speed_c_jpdf,
                 cmap='inferno')
    plt.plot(bin_disp_speed, lambda2_cond_mean[:], color='w',
             label=r'Mean Intermediate Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Intermediate Strain Rate Tensor, $\rm\beta$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='upper right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()


def plot_ext_strain_tensor_jpdf(lambda3_jpdf_bin, lambda3_disp_speed_c_jpdf,
                                lambda3_cond_mean, disp3_jpdf_bin,
                                bin_disp_speed):
    """Joint probability density function of extensive strain tensor."""

    plt.figure(7)
    plt.contourf(disp3_jpdf_bin, lambda3_jpdf_bin, lambda3_disp_speed_c_jpdf,
                 cmap='inferno')
    plt.plot(bin_disp_speed, lambda3_cond_mean[:], color='w',
             label=r'Mean Extensive Strain Rate Tensor')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Extensive Strain Rate Tensor, $\rm\alpha$')
    plt.colorbar(label='Joint Probability Density Function, JPDF')
    plt.legend(loc='lower right', labelcolor='white')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlim(-15, 15)
    plt.ylim(-1.5e5, 1.5e5)
    plt.show()


def plot_all(prog_var, disp_speed, pdf_disp_speed_cond,
             bin_pdf_disp_speed_cond, bin_disp_speed, lambda1_jpdf_bin,
             lambda1_disp_speed_c_jpdf, lambda1_cond_mean, disp1_jpdf_bin,
             lambda2_jpdf_bin, lambda2_disp_speed_c_jpdf, lambda2_cond_mean,
             disp2_jpdf_bin, lambda3_jpdf_bin, lambda3_disp_speed_c_jpdf,
             lambda3_cond_mean, disp3_jpdf_bin):
    """Function to plot all graphs."""

    # Plot progress variable
    plot_prog_var(prog_var)

    # Plot displacement speed
    plot_disp_speed(disp_speed)

    # Plot displacement speed probability density function
    plot_disp_speed_pdf(pdf_disp_speed_cond, bin_pdf_disp_speed_cond)

    # Plot compressive strain rate tensor joint probability density function
    plot_comp_strain_tensor_jpdf(lambda1_jpdf_bin, lambda1_disp_speed_c_jpdf,
                                 lambda1_cond_mean, disp1_jpdf_bin,
                                 bin_disp_speed)

    # Plot intermediate strain rate tensor joint probability density function
    plot_int_strain_tensor_jpdf(lambda2_jpdf_bin, lambda2_disp_speed_c_jpdf,
                                lambda2_cond_mean, disp2_jpdf_bin,
                                bin_disp_speed)

    # Plot extensive strain rate tensor joint probability density function
    plot_ext_strain_tensor_jpdf(lambda3_jpdf_bin, lambda3_disp_speed_c_jpdf,
                                lambda3_cond_mean, disp3_jpdf_bin,
                                bin_disp_speed)
