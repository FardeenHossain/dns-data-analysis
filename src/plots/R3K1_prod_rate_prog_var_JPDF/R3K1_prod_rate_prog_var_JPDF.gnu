set terminal epslatex size 4,3 standalone color colortext 10
set output 'R3K1_prod_rate_prog_var_JPDF.tex'

f1 = '../../../data/plots/R3K1_mid_jpdf_prod_rate_prog_var.txt'

set xlabel '$O_2$'
set ylabel '$C$'

set xrange[-1e4:0]
set yrange[0.1:0.9]

plot f1 using 1:2:3 every :::0::0 title '' with image
