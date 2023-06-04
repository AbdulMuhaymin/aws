rm -f 1c.clat.out 1c.etot_vs_clat
touch 1c.etot_vs_clat

for clat in $(seq 1.2 0.05 1.70)
do

cat > 1c.clat.in << EOF
&control
 calculation='scf'
 prefix='1c_clat'
 pseudo_dir='../'
 outdir='./outdir/'
/
&system    
 ibrav 	= 6
 a     	= 10
 b     	= 10
 c     	= $clat
 nat   	= 1
 ntyp  	= 1
 ecutwfc = 45
 occupations = 'smearing'
 smearing = 'mf'
 degauss = 0.01
/
&electrons
/
ATOMIC_SPECIES
 C      12.01100     C.rel-pbe-n-kjpaw_psl.1.0.0.UPF
ATOMIC_POSITIONS (angstrom)
 C 0.00 0.00 0.00 
K_POINTS automatic
 1 1 41 0 0 0
EOF

pw.x -in 1c.clat.in > 1c.clat.out

grep -e 'a(3)' -e ! 1c.clat.out | \
	awk '/               /{clat=$(NF-1)}/!/{print 10*clat, 13605.662285137*$(NF-1)}' >> 1c.etot_vs_clat

done
