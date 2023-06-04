import matplotlib.pyplot as plt
import numpy as np

omega, ph_tot, ph_c1= np.loadtxt('c_chain.dos', unpack=True)

plt.figure()
plt.plot(omega, ph_tot, c='b', label='Phonon DOS')

plt.xlabel('Frequency (cm$^{-1}$)')
plt.ylabel('Phonon DOS (state/cm$^{-1}$/unit-cell)')
plt.title('Phonon DOS for linear carbon chain (1*1*1 unit cell with 1 atom)')
plt.legend(loc='upper right')

plt.xlim(0, 1800)
plt.ylim(0, 0.05)

plt.show()
