import matplotlib.pyplot as plt
import numpy as np

omega, ph_tot, ph_c1, ph_c2 = np.loadtxt('gr.dos', unpack=True)

plt.figure()
plt.plot(omega, ph_tot, c='b', label='Total')
plt.plot(omega, ph_c1, c='r', ls='dashed', label='C atom')

plt.xlabel('Frequency (cm$^{-1}$)')
plt.ylabel('Phonon DOS (state/cm$^{-1}$/unit-cell)')
plt.legend(loc='upper left')

plt.xlim(0, 1700)
plt.ylim(0, 0.025)

plt.show()