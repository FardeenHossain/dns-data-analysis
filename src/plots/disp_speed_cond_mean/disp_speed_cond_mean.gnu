set terminal epslatex size 12,3 standalone color colortext 10
set output 'disp_speed_cond_mean.tex'

f1 = '../../../data/plots/R1K1_bot_cond_mean_disp_speed.txt'
f2 = '../../../data/plots/R2K1_bot_cond_mean_disp_speed.txt'
f3 = '../../../data/plots/R3K1_bot_cond_mean_disp_speed.txt'
f4 = '../../../data/plots/R4K1_bot_cond_mean_disp_speed.txt'

f5 = '../../../data/plots/R1K1_mid_cond_mean_disp_speed.txt'
f6 = '../../../data/plots/R2K1_mid_cond_mean_disp_speed.txt'
f7 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed.txt'
f8 = '../../../data/plots/R4K1_mid_cond_mean_disp_speed.txt'

f9 = '../../../data/plots/R1K1_top_cond_mean_disp_speed.txt'
f10 = '../../../data/plots/R2K1_top_cond_mean_disp_speed.txt'
f11 = '../../../data/plots/R3K1_top_cond_mean_disp_speed.txt'
f12 = '../../../data/plots/R4K1_top_cond_mean_disp_speed.txt'

set multiplot layout 1,3

set xlabel '$C$'
set ylabel '$S_d$'

set key top left

set title '(a) Bottom'

plot f1 using 1:2 every :::0::0 title 'R1K1' with lines, \
     f2 using 1:2 every :::0::0 title 'R2K1' with lines, \
     f3 using 1:2 every :::0::0 title 'R3K1' with lines, \
     f4 using 1:2 every :::0::0 title 'R4K1' with lines

set title '(b) Middle'

plot f5 using 1:2 every :::0::0 title 'R1K1' with lines, \
     f6 using 1:2 every :::0::0 title 'R2K1' with lines, \
     f7 using 1:2 every :::0::0 title 'R3K1' with lines, \
     f8 using 1:2 every :::0::0 title 'R4K1' with lines

set title '(c) Top'

plot f9 using 1:2 every :::0::0 title 'R1K1' with lines, \
     f10 using 1:2 every :::0::0 title 'R2K1' with lines, \
     f11 using 1:2 every :::0::0 title 'R3K1' with lines, \
     f12 using 1:2 every :::0::0 title 'R4K1' with lines
