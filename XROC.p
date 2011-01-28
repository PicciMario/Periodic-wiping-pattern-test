set ylabel "TPR"
set xlabel "FPR"
set grid
set xrange [0:1]
set yrange [0:1.1]

set term pdf fsize 10
set output "grafico.pdf"

set style line 2 lt 1 pt 7 ps 2 lw 3

plot "ripetitestresult_8000000" using ($1/$2):($3/$4) title "tests with n=8'000'000", x title "", "ripetitestresultavg_8000000" title "" linestyle 2
