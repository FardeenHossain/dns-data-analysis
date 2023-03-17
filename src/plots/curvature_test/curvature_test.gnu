set terminal epslatex size 4,3 standalone color colortext 10
set output 'curvature_test.tex'

f1 = '../../../data/plots/R3K1_mid_curvature_test.txt'

set xlabel '$R$'
set ylabel '$K_m$'

set key top right

plot f1 using 1:2 every :::0::0 title 'Computed' with lines, \
     f1 using 1:3 every :::0::0 title 'Analytical' with lines
