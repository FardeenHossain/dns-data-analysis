set terminal epslatex size 5,3.5 standalone color colortext 10
set output 'lambda_1_jpdf.tex'

f1 = '../../../data/plots/R3K1_jpdf_lambda_1.txt'

set xlabel '$S_d$'
set ylabel '$\alpha$'

set xrange[*:*]
set yrange[*:*]

plot f1 using 1:2:3 every :::0::0 title '$\alpha$' with image palette
