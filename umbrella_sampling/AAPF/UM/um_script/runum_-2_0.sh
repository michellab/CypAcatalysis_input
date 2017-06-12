

for AT in   -2.0
do

cat > plumed.dat << EOF

omega: TORSION ATOMS=19,25,27,37
omega2: TORSION ATOMS=19,25,27,37




restraint-omega: RESTRAINT ARG=omega KAPPA=800 AT=$AT
PRINT STRIDE=10 ARG=omega,omega2,restraint-omega.bias FILE=COLVARK800$AT

EOF


mdrun_mpi -ntomp 8 -plumed plumed.dat -nsteps 3500000 -x trajK800$AT.xtc -pin on -pinoffset 0 -gpu_id 1

done
