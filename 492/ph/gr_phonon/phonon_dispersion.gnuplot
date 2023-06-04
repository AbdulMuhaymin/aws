set grid
set xlabel "q-points"
set ylabel "Frequency (1/cm)"
set title "Phonon dispersion of graphene"
plot "gr.freq.gp" u 1:2 w l lw 2 notitle,\
		 "gr.freq.gp" u 1:3 w l lw 2 notitle,\
		 "gr.freq.gp" u 1:4 w l lw 2 notitle,\
		 "gr.freq.gp" u 1:5 w l lw 2 notitle,\
		 "gr.freq.gp" u 1:6 w l lw 2 notitle,\
		 "gr.freq.gp" u 1:7 w l lw 2 notitle
pause -1