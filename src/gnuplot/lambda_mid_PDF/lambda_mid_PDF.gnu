set terminal epslatex size 12,3 standalone color colortext 10
set output 'lambda_mid_PDF.tex'

f1 = '../../../data/plots/R1K1_mid_pdf_lambda1.txt'
f2 = '../../../data/plots/R2K1_mid_pdf_lambda1.txt'
f3 = '../../../data/plots/R3K1_mid_pdf_lambda1.txt'
f4 = '../../../data/plots/R4K1_mid_pdf_lambda1.txt'

f5 = '../../../data/plots/R1K1_mid_pdf_lambda2.txt'
f6 = '../../../data/plots/R2K1_mid_pdf_lambda2.txt'
f7 = '../../../data/plots/R3K1_mid_pdf_lambda2.txt'
f8 = '../../../data/plots/R4K1_mid_pdf_lambda2.txt'

f9 = '../../../data/plots/R1K1_mid_pdf_lambda3.txt'
f10 = '../../../data/plots/R2K1_mid_pdf_lambda3.txt'
f11 = '../../../data/plots/R3K1_mid_pdf_lambda3.txt'
f12 = '../../../data/plots/R4K1_mid_pdf_lambda3.txt'

set multiplot layout 1,3

set ylabel '$PDF$'

set xrange[-5e5:5e5]
set yrange[*:*]

set xtics 2.5e5
set format x '%.1e'

set xlabel '$\gamma [1/s]$'

plot f1 using 1:2 every :::3::3 title 'R1K1' with lines lw 5, \
     f2 using 1:2 every :::3::3 title 'R2K1' with lines lw 5, \
     f3 using 1:2 every :::3::3 title 'R3K1' with lines lw 5, \
     f4 using 1:2 every :::3::3 title 'R4K1' with lines lw 5

set xlabel '$\beta [1/s]$'

plot f5 using 1:2 every :::3::3 title 'R1K1' with lines lw 5, \
     f6 using 1:2 every :::3::3 title 'R2K1' with lines lw 5, \
     f7 using 1:2 every :::3::3 title 'R3K1' with lines lw 5, \
     f8 using 1:2 every :::3::3 title 'R4K1' with lines lw 5

set xlabel '$\alpha [1/s]$'

plot f9 using 1:2 every :::3::3 title 'R1K1' with lines lw 5, \
     f10 using 1:2 every :::3::3 title 'R2K1' with lines lw 5, \
     f11 using 1:2 every :::3::3 title 'R3K1' with lines lw 5, \
     f12 using 1:2 every :::3::3 title 'R4K1' with lines lw 5
