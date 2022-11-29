set terminal epslatex size 5,3.5 standalone color colortext 10
set output 'disp_speed_pdf.tex'

file = '../../../data/plots/R3K1_pdf_disp_speed.txt'

set xlabel '$Displacement Speed, S_d$'
set ylabel '$Probability Density Function, PDF$'

plot file using 1:2 every :::0::0 title 'C = 0.1' with lines
