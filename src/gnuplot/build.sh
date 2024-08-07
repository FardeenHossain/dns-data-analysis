#!/bin/bash
rm figures/*

cd curvature_test
gnuplot curvature_test.gnu
pdflatex curvature_test.tex
mv curvature_test.pdf ../figures
cd ..

cd disp_speed_cond_mean
gnuplot disp_speed_cond_mean.gnu
pdflatex disp_speed_cond_mean.tex
mv disp_speed_cond_mean.pdf ../figures
cd ..

cd disp_speed_cond_mean_test
gnuplot disp_speed_cond_mean_test.gnu
pdflatex disp_speed_cond_mean_test.tex
mv disp_speed_cond_mean_test.pdf ../figures
cd ..

cd disp_speed_cond_mean_1D
gnuplot disp_speed_cond_mean_1D.gnu
pdflatex disp_speed_cond_mean_1D.tex
mv disp_speed_cond_mean_1D.pdf ../figures
cd ..

cd disp_speed_curvature_JPDF
gnuplot disp_speed_curvature_JPDF.gnu
pdflatex disp_speed_curvature_JPDF.tex
mv disp_speed_curvature_JPDF.pdf ../figures
cd ..

cd disp_speed_curvature_flames_JPDF
gnuplot disp_speed_curvature_flames_JPDF.gnu
pdflatex disp_speed_curvature_flames_JPDF.tex
mv disp_speed_curvature_flames_JPDF.pdf ../figures
cd ..

cd disp_speed_PDF
gnuplot disp_speed_PDF.gnu
pdflatex disp_speed_PDF.tex
mv disp_speed_PDF.pdf ../figures
cd ..

cd disp_speed_prog_var_JPDF
gnuplot disp_speed_prog_var_JPDF.gnu
pdflatex disp_speed_prog_var_JPDF.tex
mv disp_speed_prog_var_JPDF.pdf ../figures
cd ..

cd disp_speed_prog_var_PDF
gnuplot disp_speed_prog_var_PDF.gnu
pdflatex disp_speed_prog_var_PDF.tex
mv disp_speed_prog_var_PDF.pdf ../figures
cd ..

cd disp_speed_reactive_JPDF
gnuplot disp_speed_reactive_JPDF.gnu
pdflatex disp_speed_reactive_JPDF.tex
mv disp_speed_reactive_JPDF.pdf ../figures
cd ..

cd lambda_cond_mean
gnuplot lambda_cond_mean.gnu
pdflatex lambda_cond_mean.tex
mv lambda_cond_mean.pdf ../figures
cd ..

cd lambda_mid_PDF
gnuplot lambda_mid_PDF.gnu
pdflatex lambda_mid_PDF.tex
mv lambda_mid_PDF.pdf ../figures
cd ..

cd lambda_R3K1_PDF
gnuplot lambda_R3K1_PDF.gnu
pdflatex lambda_R3K1_PDF.tex
mv lambda_R3K1_PDF.pdf ../figures
cd ..

cd prod_rate_disp_speed_JPDF
gnuplot prod_rate_disp_speed_JPDF.gnu
pdflatex prod_rate_disp_speed_JPDF.tex
mv prod_rate_disp_speed_JPDF.pdf ../figures
cd ..

cd prod_rate_PDF
gnuplot prod_rate_PDF.gnu
pdflatex prod_rate_PDF.tex
mv prod_rate_PDF.pdf ../figures
cd ..

cd prod_rate_prog_var_JPDF
gnuplot prod_rate_prog_var_JPDF.gnu
pdflatex prod_rate_prog_var_JPDF.tex
mv prod_rate_prog_var_JPDF.pdf ../figures
cd ..

cd R1K1_lambda_JPDF
gnuplot R1K1_lambda_JPDF.gnu
pdflatex R1K1_lambda_JPDF.tex
mv R1K1_lambda_JPDF.pdf ../figures
cd ..

cd R2K1_lambda_JPDF
gnuplot R2K1_lambda_JPDF.gnu
pdflatex R2K1_lambda_JPDF.tex
mv R2K1_lambda_JPDF.pdf ../figures
cd ..

cd R3K1_lambda_JPDF
gnuplot R3K1_lambda_JPDF.gnu
pdflatex R3K1_lambda_JPDF.tex
mv R3K1_lambda_JPDF.pdf ../figures
cd ..

cd R4K1_lambda_JPDF
gnuplot R4K1_lambda_JPDF.gnu
pdflatex R4K1_lambda_JPDF.tex
mv R4K1_lambda_JPDF.pdf ../figures
cd ..
