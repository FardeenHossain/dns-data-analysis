set terminal epslatex size 15,3.5 standalone color colortext 10
set output 'R3K1_mid1_lambda_jpdf.tex'

f1 = '../../../data/plots/R3K1_mid_jpdf_lambda1.txt'
f2 = '../../../data/plots/R3K1_mid_cond_mean_lambda1.txt'
f3 = '../../../data/plots/R3K1_mid_jpdf_lambda2.txt'
f4 = '../../../data/plots/R3K1_mid_cond_mean_lambda2.txt'
f5 = '../../../data/plots/R3K1_mid_jpdf_lambda3.txt'
f6 = '../../../data/plots/R3K1_mid_cond_mean_lambda3.txt'
set multiplot layout 1,3

set ylabel '$S_d$'

set xrange[*:*]
set yrange[-15:15]

set xlabel '$\gamma$'
plot f1 using 1:2:3 every :::3::3 with image, \
plot f2 using 1:2 every :::3::3 '$mean \gamma$' with line

set xlabel '$\beta$'
plot f3 using 1:2:3 every :::3::3 with image, \
plot f4 using 1:2 every :::3::3 '$mean \beta$' with line

set xlabel '$\alpha$'
plot f5 using 1:2:3 every :::3::3 with image, \
plot f6 using 1:2 every :::3::3 '$mean \alpha$' with line
