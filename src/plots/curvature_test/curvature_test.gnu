set terminal epslatex size 4,3 standalone color colortext 10
set output 'curvature_test.tex'

f1 = '../../../data/plots/R3K1_mid_curvature_test.txt'

set xlabel '$r$'
set ylabel '$K$'

set key top right

plot f1 using 1:2 every :::0::0 title '$K_m$' with lines  lw 5, \
     f1 using 1:3 every :::0::0 title '$1/r$' with lines  lw 5
