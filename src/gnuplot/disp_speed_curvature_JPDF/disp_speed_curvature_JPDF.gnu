set terminal epslatex size 4,3 standalone color colortext 10
set output 'disp_speed_curvature_JPDF.tex'

f1 = '../../../data/plots/R3K1_mid_jpdf_disp_speed_curvature.txt'

set ylabel '$S_d [m/s]$'
set xlabel '$k_M [1/m]$'

set xrange[-2e4:2e4]
set yrange[-30:30]

set format x '%.1e'
set format cb '%.1e'

set xtics 1e4

set palette defined ( 0 'white', 1 'blue', 2 'black')
              
plot f1 using 1:2:3 every :::3::3 title '' with image
