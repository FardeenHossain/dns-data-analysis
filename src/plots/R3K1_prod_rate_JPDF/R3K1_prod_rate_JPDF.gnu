set terminal epslatex size 4,3 standalone color colortext 10
set output 'R3K1_prod_rate_JPDF.tex'

f1 = '../../../data/plots/R3K1_mid_jpdf_prod_rate.txt'

set ylabel '$S_d$'
set xlabel '$T$'

set xrange[-10:10]
set yrange[-50:50]

plot f1 using 1:2:3 every :::3::3 title '' with image
