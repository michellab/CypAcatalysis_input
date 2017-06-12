

for AT in   +1.0
do

cat > plumed.dat << EOF

omega: TORSION ATOMS=19,25,27,37
omega2: TORSION ATOMS=19,25,27,37




restraint-omega: RESTRAINT ARG=omega KAPPA=300 AT=$AT
PRINT STRIDE=10 ARG=omega,omega2,restraint-omega.bias FILE=COLVARK300$AT

EOF


mdrun_mpi -ntomp 8  -plumed plumed.dat -nsteps 3500000 -x trajK300$AT.xtc -gpu_id 1 -pinoffset 0 -pin on

done
