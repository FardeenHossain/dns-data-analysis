#!/usr/bin/gnuplot -persist
set terminal epslatex size 7,4.5 dashed standalone color colortext 20

load '../palette.gnu'
load '../defs.gnu'

#
f1= '../../data/moments_x_sigmanorm1_61.dat'



set key samplen 1.5



set autoscale  y

set ytics nomirror
set ytics

set tics in

set xlabel  '$a$'
set ylabel  '$\Omega~[kg/s]$'

#set ytics("0.0" 0, "2.0" .002, "4.0" .004, "6.0" .006, "8.0" .008 , "10.0" .01 )

set xrange[*:*]
set yrange[*:*]


set key right top

#set key inside right top Left reverse
#set key at 9.7,.009 Left reverse

set output 'example.tex'


set lmargin at screen 0.25
set rmargin at screen 0.93
set bmargin at screen 0.18
set tmargin at screen 0.95

p f1 u 1:2 ev :::0::0 t 'data' w lp ls 991\




