set xlabel "Lattice parameter (Bohr)"
set ylabel "Total Magnetization (Bohr)"
set title "Total Energy vs. Lattice Parameter for Bulk Fe"
set terminal qt
set font "Arial,50"
plot "Fe.mag_vs_alat.degauss0.005.nK8" w lp title "nk=8, degauss=0.005",\
	"Fe.mag_vs_alat.degauss0.005.nK10" w lp title "nK=10, degauss=0.005",\
	"Fe.mag_vs_alat.degauss0.005.nK12" w lp title "nK=12, degauss=0.005",\
	"Fe.mag_vs_alat.degauss0.01.nK8" w lp title "nk=8, degauss=0.01",\
	"Fe.mag_vs_alat.degauss0.01.nK10" w lp title "nK=10, degauss=0.01",\
	"Fe.mag_vs_alat.degauss0.01.nK12" w lp title "nK=12, degauss=0.01",\
	"Fe.mag_vs_alat.degauss0.1.nK8" w lp title "nk=8, degauss=0.1",\
	"Fe.mag_vs_alat.degauss0.1.nK10" w lp title "nK=10, degauss=0.1",\
	"Fe.mag_vs_alat.degauss0.1.nK12" w lp title "nK=12, degauss=0.1"
pause -1