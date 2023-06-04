#! /bin/bash
# Phonon of Graphene

pw.x -i 1.scf.in > 1.scf.out
ph.x -i 2.ph.in > 2.ph.out
q2r.x -i 3.q2r.in > 3.q2r.out
matdyn.x -i 4.matdyn.in > 4.matdyn.out
