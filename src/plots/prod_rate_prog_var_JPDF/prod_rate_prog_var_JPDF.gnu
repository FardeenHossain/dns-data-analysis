set terminal epslatex size 4,3 standalone color colortext 10
set output 'prod_rate_prog_var_JPDF.tex'

f1 = '../../../data/plots/R3K1_mid_jpdf_prod_rate_prog_var.txt'

set xlabel '$C$'
set ylabel '$\dot{\omega_c}$'

set xrange[0.0:1.0]
set yrange[0:5e4]

set logscale cb

set format cb '%.1e'

set palette defined ( 0 'white', 1 'blue', 2 'red', 3 'yellow')

plot f1 using 2:1:3 every :::0::0 title '' with image
