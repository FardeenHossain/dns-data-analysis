set terminal epslatex size 5,3.5 standalone color colortext 10
set output 'R3K1_mid1_lambda_jpdf.tex'

f1 = '../../../data/plots/R3K1_jpdf_lambda_1.txt'
f2 = '../../../data/plots/R3K1_jpdf_lambda_2.txt'
f3 = '../../../data/plots/R3K1_jpdf_lambda_3.txt'

set multiplot layout 1,3

set xlabel '$\gamma$'
set ylabel '$S_d$'

set xrange[*:*]
set yrange[-14.5:14.5]

plot f1 using 1:2:3 every :::3::3 title '$\gamma$' with image
plot f2 using 1:2:3 every :::3::3 title '$\beta$' with image
plot f3 using 1:2:3 every :::3::3 title '$\alpha$' with image
