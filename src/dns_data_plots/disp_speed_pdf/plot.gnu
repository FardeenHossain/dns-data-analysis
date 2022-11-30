set terminal epslatex size 5,3.5 standalone color colortext 10
set output 'disp_speed_pdf.tex'

f1 = '../../../data/plots/R3K1_pdf_disp_speed.txt'

set xlabel '$S_d$'
set ylabel '$PDF$'

plot f1 using 1:2 every :::0::0 title 'C = 0.1' with lines, \
     f1 using 1:2 every :::1::1 title 'C = 0.3' with lines, \
     f1 using 1:2 every :::2::2 title 'C = 0.5' with lines, \
     f1 using 1:2 every :::3::3 title 'C = 0.7' with lines, \
     f1 using 1:2 every :::4::4 title 'C = 0.9' with lines
