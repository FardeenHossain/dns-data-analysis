import matplotlib.pyplot as plt

# Colormap
cmap = plt.cm.get_cmap('Blues')
cmap.set_under('white')


def plot_disp_speed(disp_speed):
    """Contour plot of displacement speed."""

    plt.figure(1)
    plt.contourf(disp_speed[:, :, 1])
    plt.xlabel('y-coordinate')
    plt.ylabel('x-coordinate')
    plt.colorbar(label=r'Displacement Speed, $\rmS_{d}$')
    plt.style.use('seaborn')
    plt.show()


def plot_figure_2(pdf_disp_speed_cond, bin_pdf_disp_speed_cond):
    """Unknown plot."""

    plt.figure(2)
    for j in range(0, len(pdf_disp_speed_cond[:, 0])):
        plt.plot(bin_pdf_disp_speed_cond, pdf_disp_speed_cond[j, :])
    plt.show()


def plot_disp_speed_pdf(pdf_disp_speed_cond, bin_pdf_disp_speed_cond):
    """Probability density function of displacement speed."""

    plt.figure(3)
    plt.plot(bin_pdf_disp_speed_cond, pdf_disp_speed_cond[0, :])
    plt.ylabel('Probability Density Function')
    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.xlim(-15, 15)
    plt.margins(x=0)
    plt.margins(y=0)
    plt.show()


def plot_comp_strain_tensor_jpdf(lambda1_jpdf_bin, lambda1_disp_speed_c_jpdf,
                                 lambda1_cond_mean, disp1_jpdf_bin,
                                 bin_disp_speed):
    """Joint probability density function of compressive strain tensor."""

    plt.figure(4)

    plt.contourf(disp1_jpdf_bin, lambda1_jpdf_bin, lambda1_disp_speed_c_jpdf,
                 cmap=cmap,
                 vmin=0.075e-6, levels=10)

    plt.plot(bin_disp_speed, lambda1_cond_mean[:], color='r',
             label=r'Mean Compressive Strain Tensor, $\rm\gamma$')

    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Compressive Strain Tensor, $\rm\gamma$')
    plt.colorbar(label='Joint Probability Density Function')
    plt.legend(loc="upper left", prop={'size': 12})
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.margins(x=0)
    plt.margins(y=0)
    plt.subplots_adjust(left=0.2, bottom=0.1, right=0.95, top=0.95)
    plt.show()


def plot_int_strain_tensor_jpdf(lambda2_jpdf_bin, lambda2_disp_speed_c_jpdf,
                                lambda2_cond_mean, disp2_jpdf_bin,
                                bin_disp_speed):
    """Joint probability density function of intermediate strain tensor."""
    plt.figure(5)

    plt.contourf(disp2_jpdf_bin, lambda2_jpdf_bin, lambda2_disp_speed_c_jpdf,
                 cmap=cmap,
                 vmin=0.1e-6, levels=10)

    plt.plot(bin_disp_speed, lambda2_cond_mean[:], color='r',
             label=r'Mean Intermediate Strain Tensor, $\rm\beta$')

    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Intermediate Strain Tensor, $\rm\beta$')
    plt.colorbar(label='Joint Probability Density Function')
    plt.legend(loc="upper left", prop={'size': 12})
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.margins(x=0)
    plt.margins(y=0)
    plt.subplots_adjust(left=0.2, bottom=0.1, right=0.95, top=0.95)
    plt.show()


def plot_ext_strain_tensor_jpdf(lambda3_jpdf_bin, lambda3_disp_speed_c_jpdf,
                                lambda3_cond_mean, disp3_jpdf_bin,
                                bin_disp_speed):
    """Joint probability density function of extensive strain tensor."""

    plt.figure(6)

    plt.contourf(disp3_jpdf_bin, lambda3_jpdf_bin, lambda3_disp_speed_c_jpdf,
                 cmap=cmap,
                 vmin=0.075e-6, levels=10)

    plt.plot(bin_disp_speed, lambda3_cond_mean[:], color='r',
             label=r'Mean Extensive Strain Tensor $\rm\alpha$')

    plt.xlabel(r'Displacement Speed, $\rmS_{d}$')
    plt.ylabel(r'Extensive Strain Tensor, $\rm\alpha$')
    plt.colorbar(label='Joint Probability Density Function')
    plt.legend(loc="lower left", prop={'size': 12})
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.margins(x=0)
    plt.margins(y=0)
    plt.subplots_adjust(left=0.2, bottom=0.1, right=0.95, top=0.95)
    plt.show()
