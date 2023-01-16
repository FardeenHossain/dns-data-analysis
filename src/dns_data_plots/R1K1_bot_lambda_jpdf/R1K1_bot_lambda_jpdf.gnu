set terminal epslatex size 15,3.5 standalone color colortext 10
set output 'R1K1_bot_lambda_jpdf.tex'

f1 = '../../../data/plots/R1K1_bot_jpdf_lambda1.txt'
f2 = '../../../data/plots/R1K1_bot_cond_mean_lambda1.txt'
f3 = '../../../data/plots/R1K1_bot_jpdf_lambda2.txt'
f4 = '../../../data/plots/R1K1_bot_cond_mean_lambda2.txt'
f5 = '../../../data/plots/R1K1_bot_jpdf_lambda3.txt'
f6 = '../../../data/plots/R1K1_bot_cond_mean_lambda3.txt'
set multiplot layout 1,3

set ylabel '$S_d$'

set xrange[-4e5:4e5]
set yrange[-14:14]

set format x '%.1e'
set xtics(-4e5, -2e5, 0e5, 2e5, 4e5)

set key font 'default, 10' textcolor rgb 'white'

set xlabel '$\gamma$'
plot f1 using 1:2:3 every :::3::3 title '' with image, \
     f2 using 2:1 every :::3::3 title 'mean $\gamma$' with lines lc rgb 'white'

set xlabel '$\beta$'
plot f3 using 1:2:3 every :::3::3 title '' with image, \
     f4 using 2:1 every :::3::3 title 'mean $\beta$' with lines lc rgb 'white'

set xlabel '$\alpha$'
plot f5 using 1:2:3 every :::3::3 title '' with image, \
     f6 using 2:1 every :::3::3 title 'mean $\alpha$' with lines lc rgb 'white'
