

for AT in   +2.0
do

cat > plumed.dat << EOF

omega: TORSION ATOMS=19,25,27,37
omega2: TORSION ATOMS=19,25,27,37




restraint-omega: RESTRAINT ARG=omega KAPPA=600 AT=$AT
PRINT STRIDE=10 ARG=omega,omega2,restraint-omega.bias FILE=COLVARK600$AT

EOF


mdrun_mpi -ntomp 8 -plumed plumed.dat -nsteps 3500000 -x trajK600$AT.xtc -pin on -pinoffset 0

done
