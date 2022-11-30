set terminal epslatex size 5,3.5 standalone color colortext 10
set output 'R3K1_mid1_lambda1_jpdf.tex'

f1 = '../../../data/plots/R3K1_jpdf_lambda_1.txt'

set xlabel '$\gamma$'
set ylabel '$S_d$'

set xrange[*:*]
set yrange[-15:15]

plot f1 using 1:2:3 every :::0::0 title '$\alpha$' with image
