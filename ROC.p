set ylabel "TPR"
set xlabel "FPR"
set grid
set xrange [0:1]
set yrange [0:1.1]

f(x) = a*tanh(x/b)
fit f(x) "ripetitestresultavg" via a, b

set term pdf fsize 10
set output "grafico.pdf"

plot "ripetitestresult" using ($1/$2):($3/$4) title "ROC with 90% threshold", x title "", f(x) title ""
