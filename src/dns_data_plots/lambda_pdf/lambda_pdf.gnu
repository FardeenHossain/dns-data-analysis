set terminal epslatex size 5,3.5 standalone color colortext 10
set output 'lambda_pdf.tex'

f1 = '../../../data/plots/R3K1_pdf_lambda_1.txt'
f2 = '../../../data/plots/R3K1_pdf_lambda_2.txt'
f3 = '../../../data/plots/R3K1_pdf_lambda_3.txt'

set xlabel '$\gamma, \beta, \alpha$'
set ylabel '$PDF$'

set xrange[-5e5:5e5]
set yrange[*:*]

plot f1 using 1:2 every :::0::0 title '$\gamma$' with lines, \
     f2 using 1:2 every :::0::0 title '$\beta$' with lines, \
     f3 using 1:2 every :::0::0 title '$\alpha$' with lines
