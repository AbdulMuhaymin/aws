#!/usr/bin/env python
from Bands import *

datafile='si.bands.dat.gnu'
fermi = 6.3719
symmetryfile='3.si.bands_pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=fermi,\
color='black', linestyle='solid', name_k_points=['L','G','X','U','G'], title='Band structure of Si')


fig.savefig("test.png")
#plt.show()
