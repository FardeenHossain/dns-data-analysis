set terminal epslatex size 4,3 standalone color colortext 10
set output 'disp_speed_cond_mean_test.tex'

f1 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed_1.txt'
f2 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed_10.txt'
f3 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed.txt'

set xlabel '$C$'
set ylabel '$S_d$'

set key top left

plot f1 using 1:2 every :::0::0 title '1 data file' with lines, \
     f2 using 1:2 every :::0::0 title '10 data files' with lines, \
     f3 using 1:2 every :::0::0 title '17 data files' with lines

