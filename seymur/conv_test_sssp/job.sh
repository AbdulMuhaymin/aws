rm -f b2n2.ecut.out b2n2.etot_vs_ecut
touch b2n2.etot_vs_ecut

for ecut in {60..120..10}
do

cat > b2n2.ecut.in << EOF
&CONTROL
  calculation = 'scf'
  outdir = './outdir/'
  prefix = 'b2n2'
  pseudo_dir = '../'
/
&SYSTEM
  ecutwfc = $ecut
  ibrav = 8
  a = 4.57
  b = 2.50
  c = 10
  nat = 4
  ntyp = 2
/
&ELECTRONS
  conv_thr =   1d-08
/

ATOMIC_SPECIES
 B      10.811     B_pbe_v1.01.uspp.F.UPF
 N      14.0067    N.oncvpsp.upf

ATOMIC_POSITIONS angstrom
B   0.8500000000       1.8706148721       0.0000000000 
B   3.7300000000       1.8706148721       0.0000000000 
N   1.5700000000       0.6250000000       0.0000000000 
N   3.0100000000       0.6250000000       0.0000000000 
K_POINTS automatic
5 5 1 0 0 0
EOF

pw.x -in b2n2.ecut.in > b2n2.ecut.out

grep -e 'kinetic-energy' -e ! b2n2.ecut.out | \
	awk '/kinetic/{ecut=$(NF-1)}/!/{print ecut, 13605.662285137*$(NF-1)}' >> b2n2.etot_vs_ecut

done