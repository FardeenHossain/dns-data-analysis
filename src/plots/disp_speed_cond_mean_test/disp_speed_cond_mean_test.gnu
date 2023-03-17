set terminal epslatex size 12,3 standalone color colortext 10
set output 'disp_speed_cond_mean_test.tex'

f1 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed_1.txt'
f2 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed_10.txt'
f3 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed.txt'

set multiplot layout 1,3

set xlabel '$C$'
set ylabel '$S_d$'

set key bottom left

set title '(a) 1 Data File'

plot f1 using 1:2 every :::0::0 with lines

set title '(b) 10 Data Files'

plot f2 using 1:2 every :::0::0 with lines

set title '(c) All Data Files'

plot f3 using 1:2 every :::0::0 with lines

