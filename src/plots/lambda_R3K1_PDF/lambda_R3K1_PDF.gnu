set terminal epslatex size 12,3 standalone color colortext 10
set output 'lambda_R3K1_PDF.tex'

f1 = '../../../data/plots/R3K1_bot_pdf_lambda1.txt'
f2 = '../../../data/plots/R3K1_bot_pdf_lambda2.txt'
f3 = '../../../data/plots/R3K1_bot_pdf_lambda3.txt'

f4 = '../../../data/plots/R3K1_mid_pdf_lambda1.txt'
f5 = '../../../data/plots/R3K1_mid_pdf_lambda2.txt'
f6 = '../../../data/plots/R3K1_mid_pdf_lambda3.txt'

f7 = '../../../data/plots/R3K1_top_pdf_lambda1.txt'
f8 = '../../../data/plots/R3K1_top_pdf_lambda2.txt'
f9 = '../../../data/plots/R3K1_top_pdf_lambda3.txt'

set multiplot layout 1,3

set xlabel '$\gamma, \beta, \alpha$'
set ylabel '$PDF$'

set xrange[-5e5:5e5]
set yrange[*:*]

set xtics 2.5e5
set format x '%.1e'

set title '(a) Bottom'

plot f1 using 1:2 every :::3::3 title '$\gamma$' with lines lw 5, \
     f2 using 1:2 every :::3::3 title '$\beta$' with lines lw 5, \
     f3 using 1:2 every :::3::3 title '$\alpha$' with lines lw 5

set title '(b) Middle'

plot f4 using 1:2 every :::3::3 title '$\gamma$' with lines lw 5, \
     f5 using 1:2 every :::3::3 title '$\beta$' with lines lw 5, \
     f6 using 1:2 every :::3::3 title '$\alpha$' with lines lw 5

set title '(c) Top'

plot f7 using 1:2 every :::3::3 title '$\gamma$' with lines lw 5, \
     f8 using 1:2 every :::3::3 title '$\beta$' with lines lw 5, \
     f9 using 1:2 every :::3::3 title '$\alpha$' with lines lw 5
