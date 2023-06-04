import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# load data
energy, dos, idos = np.loadtxt('3_c.dos.dat', unpack=True)

ef = -4.431

# make plot
plt.figure(figsize = (20, 12))
plt.plot(energy, dos, linewidth=2, color='red')
plt.title('DOS for a 1*1*1 carbon chain (with SOC)', fontsize=25)
plt.xlabel('Energy (eV)', fontsize=15)
plt.ylabel('DOS (states/eV)', fontsize=15)
plt.axvline(x=ef, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.fill_between(energy, 0, dos, where=(energy < ef), facecolor='red', alpha=0.20)
plt.text(ef+0.1, 1.7, 'Fermi energy', fontsize=12, rotation=90)
plt.xticks(np.arange(-20, 21, step=5))
plt.savefig("dos.svg")

################### For PDOS (gnuplot) ##############
# set terminal qt font "Arial,15"
# set xlabel "Energy (ev)"
# set ylabel "DOS (states/ev)"
# set title "Projected DOS of 1D carbon chain (1*1*1 Cell)"
# set arrow 1 from -4.4313,0 to -4.4313,6.5 nohead ls 0 dt 2 lw 2
# plot "4_c.pdos.dat.pdos_atm#1(C)_wfc#1(s)" u 1:2 w l lw 4 title "s-orbital", "4_c.pdos.dat.pdos_atm#1(C)_wfc#2(p)" u 1:2 w l lw 4 title "p-orbital"
