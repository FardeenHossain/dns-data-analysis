set terminal epslatex size 4,3 standalone color colortext 10
set output 'disp_speed_cond_mean_1D.tex'

f1 = '../../../data/plots/R1K1_mid_cond_mean_disp_speed.txt'
f2 = '../../../data/plots/R2K1_mid_cond_mean_disp_speed.txt'
f3 = '../../../data/plots/R3K1_mid_cond_mean_disp_speed.txt'
f4 = '../../../data/plots/R4K1_mid_cond_mean_disp_speed.txt'
f5 = '/hpcwork/itv/Antonio/premixed_jet_flames/1D/flame-massfractions-rates.dat'

set xlabel '$C$'
set ylabel '$S_d$'

set key top left

plot f1 using 1:2 every :::0::0 title 'R1K1' with lines, \
     f2 using 1:2 every :::0::0 title 'R2K1' with lines, \
     f3 using 1:2 every :::0::0 title 'R3K1' with lines, \
     f4 using 1:2 every :::0::0 title 'R4K1' with lines, \
     f5 using 1:(1/$3*1.704496e+00) title '1D Flamelet' with lines
