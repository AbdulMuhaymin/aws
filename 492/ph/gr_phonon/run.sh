#! /bin/bash
# Phonon of Graphene

pw.x < 1.scf.in > 1.scf.out
ph.x < 2.ph.in > 2.ph.out
q2r.x < 3.q2r.in > 3.q2r.out
matdyn.x < 4.matdyn.in > 4.matdyn.out
