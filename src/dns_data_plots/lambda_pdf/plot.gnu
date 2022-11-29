set terminal epslatex size 5,3.5 standalone color colortext 10
set output 'lambda_pdf.tex'

f1 = '../../../data/plots/R3K1_pdf_lambda_1.txt'

set xlabel '$Strain Rate Tensor Eigenvalue$'
set ylabel '$Probability Density Function$'

plot f1 using 1:2 every :::0::0 title 'C = 0.1' with lines
