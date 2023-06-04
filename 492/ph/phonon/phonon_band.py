
import matplotlib.pyplot as plt
import numpy as np

# Number of phonon modes and q-points from c_chain.freq
nbnd = 3; nks = 41

# Open c_chain.freq.gp file
qs, *ph = np.loadtxt('c_chain.freq.gp', unpack=True)

# Read phonon at each phonon index
ph0 = []
for iq in range(nks):
    ph0.append([])
    for ib in range(nbnd):
        tmp = ph[ib][iq]
        ph0[iq].append(float(tmp))
    
# Set high-symmetry points from matdyn.in
G = qs[0]; Z = qs[40]

# Create figure object
plt.figure()

# Plot dotted lines at high-symmetry points
#plt.axvline(G, c='gray')
#plt.axvline(Z, c='gray')
# Plot the phonon dispersion
plt.plot(qs, ph0, c='b')

# Add the x and y-axis labels
plt.xlabel('High-symmetry points')
plt.ylabel('Frequency (cm$^{-1}$)')
plt.title('Phonon dispersion of linear carbon chain (1*1*1 unit cell with 1 atom)')

plt.xlim(G, Z)
#plt.ylim(-50, 1700)

# Add labels for high-symmetry points
plt.xticks([G, Z], ['$\\Gamma$', 'Z'])
# Hide x-axis minor ticks
plt.tick_params(axis='x', which='minor', bottom=False, top=False)

# Save the figure 
#plt.savefig('plot-phonon.pdf')
# Show the plot
plt.show()