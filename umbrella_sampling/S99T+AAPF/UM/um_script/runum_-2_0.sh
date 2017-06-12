
for AT in   -2.0
do

cat > plumed.dat << EOF

omega: TORSION ATOMS=2518,2524,2526,2536 
omega2: TORSION ATOMS=2518,2524,2526,2536
d1: DISTANCE ATOMS=826,2539      #distance A (ARG55:CZ---PRO4:O)
d2: DISTANCE ATOMS=954,2515      #distance B (GLN63:NE2---ALA2:O)
d3: DISTANCE ATOMS=1521,2525      #distance C (ASN102:N---ALA3:O)
d4: DISTANCE ATOMS=1534,2516      #distance D (ASN102:O---ALA3:N)




restraint-omega: RESTRAINT ARG=omega KAPPA=700 AT=$AT
PRINT STRIDE=10 ARG=omega,omega2,restraint-omega.bias FILE=COLVARK700$AT
PRINT STRIDE=10 ARG=omega,omega2,restraint-omega.bias,d1,d2,d3,d4 FILE=COLDISTK700$AT

EOF


#mdrun_mpi -plumed plumed.dat -nsteps 3500000 -x trajK800$AT.xtc -gpu_id 0
mdrun_mpi -ntomp 2 -plumed plumed.dat -nsteps 3500000 -x trajK700$AT.xtc -gpu_id 0 -pin off -pinoffset 2

done
