set ylabel "TPR"
set xlabel "FPR"
set grid
set xrange [0:1]
set yrange [0:1.1]

f(x) = a*tanh(x**2/b)
fit f(x) "ripetitestresultavg" via a, b

set term pdf fsize 10
set output "grafico.pdf"

set style line 1 lt 2

plot "ripetitestresultavg" with linespoints title "ROC with 90% threshold", x title "" 
