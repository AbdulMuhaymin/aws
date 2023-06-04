rm -f b2n2.ecut.out b2n2.etot_vs_ecut
touch b2n2.etot_vs_ecut

for dual in 4 6 8 12; do
for ecutwfc in {30..50..5}; do
let "ecutrho = ecutwfc * dual"

cat > b2n2.ecut.in << EOF
&CONTROL
  calculation = 'scf'
  outdir = './outdir/'
  prefix = 'b2n2'
  pseudo_dir = '../'
  disk_io='none'
/
&SYSTEM
  ecutwfc = $ecutwfc
  ecutrho = $ecutrho
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
 B      10.811     B.pbe-n-kjpaw_psl.1.0.0.UPF
 N      14.0067    N.pbe-n-kjpaw_psl.1.0.0.UPF

ATOMIC_POSITIONS angstrom
B   0.8500000000       1.8706148721       0.0000000000 
B   3.7300000000       1.8706148721       0.0000000000 
N   1.5700000000       0.6250000000       0.0000000000 
N   3.0100000000       0.6250000000       0.0000000000 
K_POINTS automatic
5 5 1 0 0 0
EOF

pw.x -in b2n2.ecut.in > b2n2.ecut.out

grep -e ! b2n2.ecut.out | awk -v a=$ecutwfc -v b=$ecutrho '{print a " " b " " $(NF-1)}' >> fe.etot_vs_ecut.$dual

done
done