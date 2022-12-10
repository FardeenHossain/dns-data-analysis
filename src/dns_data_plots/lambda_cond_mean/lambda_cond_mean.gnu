set terminal epslatex size 15,3.5 standalone color colortext 10
set output 'lambda_cond_mean.tex'

f1 = '../../../data/plots/R1K1_mid_cond_mean_lambda1.txt'
f2 = '../../../data/plots/R2K1_mid_cond_mean_lambda1.txt'
f3 = '../../../data/plots/R3K1_mid_cond_mean_lambda1.txt'
f4 = '../../../data/plots/R4K1_mid_cond_mean_lambda1.txt'

set xlabel '$\gamma$'
set ylabel '$S_d$'

set xrange[-3e5:0]
set yrange[-14:14]

set format x '%.1e'
set xtics(-3e5, -2e5, -1e5, 0)

plot f1 using 2:1 every :::3::3 title 'R1K1' with lines, \
     f2 using 2:1 every :::3::3 title 'R2K1' with lines, \
     f3 using 2:1 every :::3::3 title 'R3K1' with lines, \
     f4 using 2:1 every :::3::3 title 'R4K1' with lines
