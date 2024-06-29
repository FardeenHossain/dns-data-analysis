set terminal epslatex size 12,9 standalone color colortext 10
set output 'R3K1_lambda_JPDF.tex'

f1 = '../../../data/plots/R3K1_bot_jpdf_lambda1.txt'
f2 = '../../../data/plots/R3K1_bot_cond_mean_lambda1.txt'
f3 = '../../../data/plots/R3K1_bot_jpdf_lambda2.txt'
f4 = '../../../data/plots/R3K1_bot_cond_mean_lambda2.txt'
f5 = '../../../data/plots/R3K1_bot_jpdf_lambda3.txt'
f6 = '../../../data/plots/R3K1_bot_cond_mean_lambda3.txt'

f7 = '../../../data/plots/R3K1_mid_jpdf_lambda1.txt'
f8 = '../../../data/plots/R3K1_mid_cond_mean_lambda1.txt'
f9 = '../../../data/plots/R3K1_mid_jpdf_lambda2.txt'
f10 = '../../../data/plots/R3K1_mid_cond_mean_lambda2.txt'
f11 = '../../../data/plots/R3K1_mid_jpdf_lambda3.txt'
f12 = '../../../data/plots/R3K1_mid_cond_mean_lambda3.txt'

f13 = '../../../data/plots/R3K1_top_jpdf_lambda1.txt'
f14 = '../../../data/plots/R3K1_top_cond_mean_lambda1.txt'
f15 = '../../../data/plots/R3K1_top_jpdf_lambda2.txt'
f16 = '../../../data/plots/R3K1_top_cond_mean_lambda2.txt'
f17 = '../../../data/plots/R3K1_top_jpdf_lambda3.txt'
f18 = '../../../data/plots/R3K1_top_cond_mean_lambda3.txt'

set multiplot layout 3,3

set ylabel '$S_d [m/s]$'

set xrange[-2e5:2e5]
set yrange[-60:60]

set format x '%.1e'
set format cb '%.1e'

set xtics 1e5

set palette defined ( 0 'white', 1 'blue', 2 'black')
                    
set title ' '
set key top right
set xlabel '$\gamma [1/s]$'

plot f1 using 1:2:3 every :::3::3 title '' with image, \
     f2 using 2:1 every :::3::3 title 'Mean $\gamma$' with lines lw 5 linecolor rgb 'red'

set title '(a) R3K1 Bottom'
set key top left
set xlabel '$\beta [1/s]$'

plot f3 using 1:2:3 every :::3::3 title '' with image, \
     f4 using 2:1 every :::3::3 title 'Mean $\beta$' with lines lw 5 linecolor rgb 'red'

set title ' '
set key top left
set xlabel '$\alpha [1/s]$'

plot f5 using 1:2:3 every :::3::3 title '' with image, \
     f6 using 2:1 every :::3::3 title 'Mean $\alpha$' with lines lw 5 linecolor rgb 'red'


set title ' '
set key top right
set xlabel '$\gamma [1/s]$'

plot f7 using 1:2:3 every :::3::3 title '' with image, \
     f8 using 2:1 every :::3::3 title 'Mean $\gamma$' with lines lw 5 linecolor rgb 'red'

set title '(b) R3K1 Middle'
set key top left
set xlabel '$\beta [1/s]$'

plot f9 using 1:2:3 every :::3::3 title '' with image, \
     f10 using 2:1 every :::3::3 title 'Mean $\beta$' with lines lw 5 linecolor rgb 'red'

set title ' '
set key top left
set xlabel '$\alpha [1/s]$'

plot f11 using 1:2:3 every :::3::3 title '' with image, \
     f12 using 2:1 every :::3::3 title 'Mean $\alpha$' with lines lw 5 linecolor rgb 'red'

set title ' '
set key top right
set xlabel '$\gamma [1/s]$'

plot f13 using 1:2:3 every :::3::3 title '' with image, \
     f14 using 2:1 every :::3::3 title 'Mean $\gamma$' with lines lw 5 linecolor rgb 'red'

set title '(c) R3K1 Top'
set key top left
set xlabel '$\beta [1/s]$'

plot f15 using 1:2:3 every :::3::3 title '' with image, \
     f16 using 2:1 every :::3::3 title 'Mean $\beta$' with lines lw 5 linecolor rgb 'red'

set title ' '
set key top left
set xlabel '$\alpha [1/s]$'

plot f17 using 1:2:3 every :::3::3 title '' with image, \
     f18 using 2:1 every :::3::3 title 'Mean $\alpha$' with lines lw 5 linecolor rgb 'red'