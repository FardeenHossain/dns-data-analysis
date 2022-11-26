#!/usr/bin/gnuplot -persist
#
# Qualitative Brewer palette 
# http://colorbrewer2.org/?type=qualitative&scheme=Set1&n=5
# Lines mains 
set style line 1 dt 1 lw 6 lc rgb "#e41a1c"   # red
set style line 2 dt 2 lw 6 lc rgb "#377eb8"   # blue
set style line 3 dt 3 lw 4 lc rgb "#4daf4a"   # green
set style line 4 dt 2 lw 4 lc rgb "#984ea3"   # purple
set style line 5 dt 1 lw 2 lc rgb "#ff7f00"   # orange
set style line 6 dt 1 lw 4 lc rgb "black"     # black 
set style line 7 dt 4 lw 4 lc rgb "#a65628"   # brown 
set style line 8 dt 4 lw 4 lc rgb "#f781bf"   # pink
set style line 9 dt 1 lw 2 lc rgb "#377eb8"   # blue

# Lines solid
set style line 11 lt 1 lw 2 lc rgb "#e41a1c"   # red
set style line 12 lt 1 lw 2 lc rgb "#377eb8"   # blue
set style line 13 lt 1 lw 2 lc rgb "#4daf4a"   # green
set style line 14 lt 1 lw 2 lc rgb "#984ea3"   # purple
set style line 15 lt 1 lw 2 lc rgb "#ff7f00"   # orange
set style line 16 lt 1 lw 2 lc rgb "black"     # black 
set style line 17 lt 1 lw 2 lc rgb "#a65628"   # brown 
set style line 18 lt 1 lw 2 lc rgb "#f781bf"   # pink

# Lines thin dashed 
set style line 21 lt 2 lw 1 lc rgb "#e41a1c"   # red
set style line 22 lt 2 lw 1 lc rgb "#377eb8"   # blue
set style line 23 lt 2 lw 1 lc rgb "#4daf4a"   # green
set style line 24 lt 2 lw 1 lc rgb "#984ea3"   # purple
set style line 25 lt 2 lw 1 lc rgb "#ff7f00"   # orange
set style line 26 lt 2 lw 1 lc rgb "black"     # black 
set style line 27 lt 2 lw 1 lc rgb "#a65628"   # brown 
set style line 28 lt 2 lw 1 lc rgb "#f781bf"   # pink

# Lines thin solid
set style line 31 lt 1 lw 1 lc rgb "#e41a1c"   # red
set style line 32 lt 1 lw 1 lc rgb "#377eb8"   # blue
set style line 33 lt 1 lw 1 lc rgb "#4daf4a"   # green
set style line 34 lt 1 lw 1 lc rgb "#984ea3"   # purple
set style line 35 lt 1 lw 1 lc rgb "#ff7f00"   # orange
set style line 36 lt 1 lw 1 lc rgb "black"     # black 
set style line 37 lt 1 lw 1 lc rgb "#a65628"   # brown 
set style line 38 lt 1 lw 1 lc rgb "#f781bf"   # pink


# Lines thick 
set style line 41 dt 1 lw 5 lc rgb "#e41a1c"   # red
set style line 42 dt 4 lw 5 lc rgb "#377eb8"   # blue
set style line 43 dt 1 lw 5 lc rgb "#4daf4a"   # green
set style line 44 dt 2 lw 5 lc rgb "#984ea3"   # purple
set style line 45 dt 1 lw 5 lc rgb "#ff7f00"   # orange
set style line 46 dt 3 lw 5 lc rgb "black"     # black 
set style line 47 dt 4 lw 5 lc rgb "#a65628"   # brown
set style line 48 dt 4 lw 4 lc rgb "#f781bf"   # pink
set style line 49 dt 2 lw 10 lc rgb "white"   # white

# Lines continuous color gradient
set style line 301 lc rgb '#E50800' lt 1 lw 1.5 # --- red
set style line 302 lc rgb '#D00911' lt 1 lw 1.5 #      .
set style line 303 lc rgb '#BB0A22' lt 1 lw 1.5 #      .
set style line 304 lc rgb '#A60B34' lt 1 lw 1.5 #      .
set style line 305 lc rgb '#910C45' lt 1 lw 1.5 #      .
set style line 306 lc rgb '#7C0D56' lt 1 lw 1.5 #      .
set style line 307 lc rgb '#680F68' lt 1 lw 1.5 #      .
set style line 308 lc rgb '#531079' lt 1 lw 1.5 #      .
set style line 309 lc rgb '#3E118A' lt 1 lw 1.5 #      .
set style line 310 lc rgb '#29129C' lt 1 lw 1.5 #      .
set style line 311 lc rgb '#1413AD' lt 1 lw 1.5 #      .
set style line 312 lc rgb '#0015BF' lt 1 lw 1.5 # --- blue

# Lines continuous color gradient
set style line 401 lc rgb '#0025ad' lt 1 lw 1.5 # --- blue
set style line 402 lc rgb '#0042ad' lt 1 lw 1.5 #      .
set style line 403 lc rgb '#0060ad' lt 1 lw 1.5 #      .
set style line 404 lc rgb '#007cad' lt 1 lw 1.5 #      .
set style line 405 lc rgb '#0099ad' lt 1 lw 1.5 #      .
set style line 406 lc rgb '#00ada4' lt 1 lw 1.5 #      .
set style line 407 lc rgb '#00ad88' lt 1 lw 1.5 #      .
set style line 408 lc rgb '#00ad6b' lt 1 lw 1.5 #      .
set style line 409 lc rgb '#00ad4e' lt 1 lw 1.5 #      .
set style line 410 lc rgb '#00ad31' lt 1 lw 1.5 #      .
set style line 411 lc rgb '#00ad14' lt 1 lw 1.5 #      .
set style line 412 lc rgb '#09ad00' lt 1 lw 1.5 # --- green

# Lines continuous 12 colors
set style line 501 lc rgb '#a6cee3' lt 1 lw 3 #1.5 # 
set style line 502 lc rgb '#1f78b4' lt 1 lw 3 #1.5 # 
set style line 503 lc rgb '#b2df8a' lt 1 lw 3 #1.5 # 
set style line 504 lc rgb '#33a02c' lt 1 lw 3 #1.5 # 
set style line 505 lc rgb '#fb9a99' lt 1 lw 3 #1.5 # 
set style line 506 lc rgb '#e31a1c' lt 1 lw 3 #1.5 # 
set style line 507 lc rgb '#fdbf6f' lt 1 lw 3 #1.5 # 
set style line 508 lc rgb '#ff7f00' lt 1 lw 3 #1.5 # 
set style line 509 lc rgb '#cab2d6' lt 1 lw 3 #1.5 # 
set style line 510 lc rgb '#6a3d9a' lt 1 lw 3 #1.5 # 
set style line 511 lc rgb 'black'   lt 1 lw 3 #1.5 # 
set style line 512 lc rgb '#b15928' lt 1 lw 3 #1.5 # 


# Symbols open
set style line 111 lt 1 lw 1 pt 65  ps 1.5 lc rgb "#e41a1c"      
set style line 112 lt 2 lw 1 pt 66  ps 1.5 lc rgb "#377eb8"      
set style line 113 lt 1 lw 1 pt 64  ps 1.5 lc rgb "#4daf4a"    
set style line 114 lt 2 lw 1 pt 3   ps 1.5 lc rgb "#984ea3" 
set style line 115 lt 1 lw 1 pt 13  ps 1.5 lc rgb "#ff7f00" 
set style line 116 lt 1 lw 1 pt 69  ps 1.5 lc rgb "black"   
set style line 117 lt 1 lw 1 pt 20  ps 1.5 lc rgb "#377eb8"
set style line 118 lt 2 lw 1 pt 125 ps 1.5 lc rgb "#e41a1c"
set style line 119 lt 1 lw 1 pt 112 ps 1.5 lc rgb "#4daf4a"

# Symbols solid
set style line 121 lt 1 lw 2 pt 7  ps 2 lc rgb "#e41a1c"    
set style line 122 lt 1 lw 2 pt 9  ps 2 lc rgb "#377eb8"    
set style line 123 lt 1 lw 2 pt 5  ps 2 lc rgb "#4daf4a"    
set style line 124 lt 1 lw 2 pt 11 ps 2 lc rgb "#984ea3"    

# Symbols open 
set style line 151 lt 1 lw 2 pt 6  ps 2 lc rgb "#e41a1c"    
set style line 152 lt 1 lw 2 pt 8  ps 2 lc rgb "#377eb8"    
set style line 153 lt 1 lw 2 pt 4  ps 2 lc rgb "#4daf4a"   
set style line 154 lt 1 lw 2 pt 12 ps 2 lc rgb "#984ea3"    

# Big Symbols solid 
set style line 161 lt 1 lw 2 pt 7   ps 3 lc rgb "#e41a1c"    
set style line 162 lt 1 lw 2 pt 9   ps 3 lc rgb "#377eb8"    
set style line 163 lt 1 lw 2 pt 5   ps 3 lc rgb "#4daf4a"    
set style line 164 lt 1 lw 2 pt 11  ps 3 lc rgb "#984ea3"    
set style line 165 lt 1 lw 2 pt 13  ps 3 lc rgb "#ff7f00" 

# Small Symbols solid
set style line 171 lt 1 lw 2 pt 7  ps 2.0 lc rgb "#e41a1c"    
set style line 172 lt 1 lw 2 pt 9  ps 2.0 lc rgb "#377eb8"    
set style line 173 lt 1 lw 2 pt 5  ps 2.0 lc rgb "#4daf4a"    
set style line 174 lt 1 lw 2 pt 13 ps 2.0 lc rgb "#984ea3"    

# Small Symbols open 
set style line 181 lt 1 lw 2 pt 6  ps 2.0 lc rgb "#e41a1c"    
set style line 182 lt 1 lw 2 pt 8  ps 2.0 lc rgb "#377eb8"    
set style line 183 lt 1 lw 2 pt 4  ps 2.0 lc rgb "#4daf4a"   
set style line 184 lt 1 lw 2 pt 12 ps 2.0 lc rgb "#984ea3"    


#-------------------------------------------------------------
#-------------------------------------------------------------

set style line 991 lt 1  lw 5 pt 65 ps 2.00 lc rgb '#e41a1c'
set style line 992 lt 1  lw 5 pt 69 ps 1.75 lc rgb '#377eb8'
set style line 993 lt 1  lw 5 pt 64 ps 2.00 lc rgb '#4daf4a'
set style line 994 lt 1  lw 5 pt 66 ps 2.00 lc rgb '#ff7f00'

set style line 981 lt 1  lw 5 pt 7  ps 2 lc rgb '#e41a1c'
set style line 982 lt 1  lw 5 pt 15 ps 2 lc rgb '#377eb8'
set style line 983 lt 1  lw 5 pt 5  ps 2 lc rgb '#4daf4a'
set style line 984 lt 1  lw 5 pt 9  ps 2 lc rgb '#ff7f00'

set style line 971 lt 1  lw 5 pt 7  ps 4 lc rgb '#e41a1c'
set style line 972 lt 1  lw 5 pt 15 ps 4 lc rgb '#377eb8'
set style line 973 lt 1  lw 5 pt 5  ps 4 lc rgb '#4daf4a'
set style line 974 lt 1  lw 5 pt 9  ps 4 lc rgb '#ff7f00'

set style line 961 lt 1  lw 5 pt 65 ps 2.00 lc rgb 'black'
set style line 962 lt 1  lw 5 pt 69 ps 1.75 lc rgb 'black'
set style line 963 lt 1  lw 5 pt 64 ps 2.00 lc rgb 'black'
set style line 964 lt 1  lw 5 pt 66 ps 2.00 lc rgb 'black'


