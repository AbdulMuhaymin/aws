#!/usr/bin/env python
from Bands import *

datafile='b2n2.bands.pp.dat.gnu'
fermi = -0.5862
symmetryfile='4.b2n2.bands.pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=-0.5862,\
color='black', linestyle='solid', name_k_points=['G','X','S','Y','G','S'], title='Band structure of 1*1*1 carbon chain')


fig.savefig("test.png")
#plt.show()
