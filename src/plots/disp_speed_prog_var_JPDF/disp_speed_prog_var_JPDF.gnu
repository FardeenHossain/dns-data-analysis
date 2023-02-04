set terminal epslatex size 4,3 standalone color colortext 10
set output 'disp_speed_prog_var_JPDF.tex'

f1 = '../../../data/plots/R3K1_mid_jpdf_disp_speed_prog_var.txt'

set xlabel '$C$'
set ylabel '$S_d$'

set xrange[0.0:1.0]
set yrange[-60:60]

plot f1 using 2:1:3 every :::0::0 title '' with image
