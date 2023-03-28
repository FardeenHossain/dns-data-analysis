set terminal epslatex size 4,3 standalone color colortext 10
set output 'prod_rate_PDF.tex'

f1 = '../../../data/plots/R3K1_mid_pdf_prod_rate.txt'

set xlabel '$\dot{\omega_c} [kg/m^3s]$'
set ylabel '$PDF$'

set xrange[0:5e4]
set yrange[*:*]

plot f1 using 1:2 every :::3::3 title '' with lines lw 5
