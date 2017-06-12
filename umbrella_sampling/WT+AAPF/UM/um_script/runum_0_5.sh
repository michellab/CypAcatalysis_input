
for AT in   +0.5
do

cat > plumed.dat << EOF

omega: TORSION ATOMS=2500,2506,2508,2518
omega2: TORSION ATOMS=2500,2506,2508,2518
d1: DISTANCE ATOMS=826,2521      #distance A (ARG55:CZ---PRO4:O)
d2: DISTANCE ATOMS=954,2497      #distance B (GLN63:NE2---ALA2:O)
d3: DISTANCE ATOMS=1518,2507      #distance C (ASN102:N---ALA3:O)
d4: DISTANCE ATOMS=1531,2498      #distance D (ASN102:O---ALA3:N)




restraint-omega: RESTRAINT ARG=omega KAPPA=100 AT=$AT
PRINT STRIDE=10 ARG=omega,omega2,restraint-omega.bias FILE=COLVARK100$AT
PRINT STRIDE=10 ARG=omega,omega2,restraint-omega.bias,d1,d2,d3,d4 FILE=COLDISTK100$AT

EOF


#mdrun_mpi -plumed plumed.dat -nsteps 3500000 -x trajK800$AT.xtc -gpu_id 0
mdrun_mpi -ntomp 2 -plumed plumed.dat -nsteps 3500000 -x trajK100$AT.xtc -gpu_id 0 -pin off -pinoffset 2

done
