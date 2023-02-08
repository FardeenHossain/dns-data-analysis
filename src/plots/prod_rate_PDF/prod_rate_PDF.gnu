set terminal epslatex size 4,3 standalone color colortext 10
set output 'prod_rate_PDF.tex'

f1 = '../../../data/plots/R3K1_mid_pdf_prod_rate.txt'

set xlabel '$O_2 source$'
set ylabel '$PDF$'

set xrange[-1e4:0]
set yrange[*:*]

plot f1 using 1:2 every :::3::3 title '' with lines
