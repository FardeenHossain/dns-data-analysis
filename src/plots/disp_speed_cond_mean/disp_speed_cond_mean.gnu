# set terminal epslatex size 12,3 standalone color colortext 10
set terminal epslatex size 4,3 standalone color colortext 10
set output 'disp_speed_cond_mean.tex'

f1 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed.txt'

#f1 = '../../../data/plots/R1K1_bot_cond_mean_lambda1.txt'
#f2 = '../../../data/plots/R2K1_bot_cond_mean_lambda1.txt'
#f3 = '../../../data/plots/R3K1_bot_cond_mean_lambda1.txt'
#f4 = '../../../data/plots/R4K1_bot_cond_mean_lambda1.txt'

#f5 = '../../../data/plots/R1K1_mid_cond_mean_lambda1.txt'
#f6 = '../../../data/plots/R2K1_mid_cond_mean_lambda1.txt'
#f7 = '../../../data/plots/R3K1_mid_cond_mean_lambda1.txt'
#f8 = '../../../data/plots/R4K1_mid_cond_mean_lambda1.txt'

#f9 = '../../../data/plots/R1K1_top_cond_mean_lambda1.txt'
#f10 = '../../../data/plots/R2K1_top_cond_mean_lambda1.txt'
#f11 = '../../../data/plots/R3K1_top_cond_mean_lambda1.txt'
#f12 = '../../../data/plots/R4K1_top_cond_mean_lambda1.txt'

#set multiplot layout 1,3

set xlabel '$C$'
set ylabel '$\S_d'

set xrange[-60:60]
#set yrange[-4e5:0]

#set ytics 1e5
#set format y '%.1e'

#set key bottom right

#set title '(a) Bottom'

plot f1 using 1:2 every :::3::3 title 'R3K1' with lines, \

#plot f1 using 1:2 every :::3::3 title 'R1K1' with lines, \
#     f2 using 1:2 every :::3::3 title 'R2K1' with lines, \
#     f3 using 1:2 every :::3::3 title 'R3K1' with lines, \
#     f4 using 1:2 every :::3::3 title 'R4K1' with lines

#set title '(b) Middle'

#plot f5 using 1:2 every :::3::3 title 'R1K1' with lines, \
#     f6 using 1:2 every :::3::3 title 'R2K1' with lines, \
#     f7 using 1:2 every :::3::3 title 'R3K1' with lines, \
#     f8 using 1:2 every :::3::3 title 'R4K1' with lines

#set title '(c) Top'

#plot f9 using 1:2 every :::3::3 title 'R1K1' with lines, \
#     f10 using 1:2 every :::3::3 title 'R2K1' with lines, \
#     f11 using 1:2 every :::3::3 title 'R3K1' with lines, \
#     f12 using 1:2 every :::3::3 title 'R4K1' with lines
