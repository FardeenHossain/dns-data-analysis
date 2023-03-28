set terminal epslatex size 4,3 standalone color colortext 10
set output 'disp_speed_prog_var_PDF.tex'

f1 = '../../../data/plots/R3K1_mid_pdf_disp_speed.txt'

set xlabel '$S_d [m/s]$'
set ylabel '$PDF$'

set xrange[-60:60]
set yrange[*:*]

plot f1 using 1:2 every :::0::0 title 'C = 0.10' with lines lw 5, \
     f1 using 1:2 every :::1::1 title 'C = 0.30' with lines lw 5, \
     f1 using 1:2 every :::2::2 title 'C = 0.50' with lines lw 5, \
     f1 using 1:2 every :::3::3 title 'C = 0.73' with lines lw 5, \
     f1 using 1:2 every :::4::4 title 'C = 0.90' with lines lw 5
