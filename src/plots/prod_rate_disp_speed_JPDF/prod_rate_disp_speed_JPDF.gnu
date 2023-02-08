set terminal epslatex size 4,3 standalone color colortext 10
set output 'prod_rate_disp_speed_JPDF.tex'

f1 = '../../../data/plots/R3K1_mid_jpdf_prod_rate_cond.txt'

set ylabel '$S_d$'
set xlabel '$\omega_c$'

set xrange[0:5e4]
set yrange[-60:60]

set format cb '%.1e'

# set palette defined ( 0.07 'white', 0.08 'blue', 0.15 'red')

plot f1 using 1:2:3 every :::3::3 title '' with image
