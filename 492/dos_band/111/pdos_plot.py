import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# load data
energy1, s_pdos = np.loadtxt('4_c.pdos.dat.pdos_atm#1(C)_wfc#1(s)', unpack=True, usecols =(0 ,1))
energy2, p_pdos = np.loadtxt('4_c.pdos.dat.pdos_atm#1(C)_wfc#2(p)', unpack=True, usecols =(0 ,1))
energy3, tot_pdos= np.loadtxt('4_c.pdos.dat.pdos_tot', unpack=True, usecols =(0 ,1))
#energy4, tot_dos= np.loadtxt('3_c.dos.dat', unpack=True, usecols =(0 ,1))

ef = -4.4314

# make plot
plt.figure(figsize = (20, 12))

plt.plot(energy1, s_pdos, linewidth=2, label='s-orbital')
plt.plot(energy2, p_pdos, linewidth=2, label='p-orbital')
plt.plot(energy3, tot_pdos, linewidth=2, label='Sum of PDOS')
#plt.plot(energy4, tot_dos, linewidth=2, label='DOS')

plt.title('Density of states for a 1*1*1 carbon chain', fontsize=25)
plt.xlabel('Energy (eV)', fontsize=15)
plt.ylabel('DOS', fontsize=15)
plt.axvline(x=ef, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
#plt.fill_between(energy4, 0, tot_dos, where=(energy4 < ef), facecolor='red', alpha=0.20)
plt.text(ef+0.1, 1.7, 'Fermi energy', fontsize=12, rotation=90)
plt.legend()
plt.show()
