set grid
set xlabel "q-points"
set ylabel "Frequency (1/cm)"
set title "Phonon dispersion of linear carbon chain"
plot "c_chain.freq.gp" u 1:1 w l lw 2 notitle,\
		 "c_chain.freq.gp" u 1:2 w l lw 2 notitle,\
		 "c_chain.freq.gp" u 1:3 w l lw 2 notitle
pause -1
