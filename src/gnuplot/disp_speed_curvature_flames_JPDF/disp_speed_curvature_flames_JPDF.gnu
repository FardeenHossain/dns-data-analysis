set terminal epslatex size 8,6 standalone color colortext 10
set output 'disp_speed_curvature_flames_JPDF.tex'

f1 = '../../../data/plots/R1K1_mid_jpdf_disp_speed_curvature.txt'
f2 = '../../../data/plots/R2K1_mid_jpdf_disp_speed_curvature.txt'
f3 = '../../../data/plots/R3K1_mid_jpdf_disp_speed_curvature.txt'
f4 = '../../../data/plots/R4K1_mid_jpdf_disp_speed_curvature.txt'

set multiplot layout 2,2

set ylabel '$S_d [m/s]$'
set xlabel '$k_M [1/m]$'

set xrange[-2e4:2e4]
set yrange[-30:30]

set format x '%.1e'
set format cb '%.1e'

set xtics 1e4

set palette defined ( 0 'white', 1 'blue', 2 'black')

set title '(a) R1K1'
plot f1 using 1:2:3 every :::3::3 title '' with image

set title '(b) R2K1'
plot f2 using 1:2:3 every :::3::3 title '' with image

set title '(c) R3K1'
plot f3 using 1:2:3 every :::3::3 title '' with image

set title '(d) R4K1'
plot f4 using 1:2:3 every :::3::3 title '' with image
