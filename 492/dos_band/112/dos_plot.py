import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# load data
energy, dos, idos = np.loadtxt('3_c.dos.dat', unpack=True)

ef = -4.4244

# make plot
plt.figure(figsize = (20, 12))
plt.plot(energy, dos, linewidth=2, color='red')
plt.title('Density of states for a 1*1*2 carbon chain', fontsize=20)
plt.xlabel('Energy (eV)', fontsize=15)
plt.ylabel('DOS (states/eV)', fontsize=15)
plt.axvline(x=ef, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.fill_between(energy, 0, dos, where=(energy < ef), facecolor='red', alpha=0.20)
plt.text(ef+0.1, 1.7, 'Fermi energy', fontsize=12, rotation=90)
plt.xticks(np.arange(-20, 9, step=5))
plt.show()

################### For PDOS (gnuplot) ##############
# sumpdos.x *\(C\)*\(p\) > atom_C_p.dat
# set terminal qt font "Arial,15"
# set xlabel "Energy (ev)"
# set ylabel "DOS (states/ev)"
# set title "Projected DOS of 1D carbon chain (1*1*1 Cell)"
# set arrow 1 from -4.4244,0 to -4.4244,6.5 nohead ls 0 dt 2 lw 2
# plot "atom_C_s.dat" u 1:2 w l lw 4 title "s-orbital", "atom_C_p.dat" u 1:2 w l lw 4 title "p-orbital"
