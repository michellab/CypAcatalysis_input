gmx=/home/pattama/local/gromacs/bin

$gmx'/pdb2gmx' -f 3K0NA.pdb -o 3K0NA_processed.gro -water tip3p -ignh -ff amber99sb_modified 

$gmx'/editconf' -f 3K0NA_processed.gro -o 3K0N_newbox.gro -c -d 1.0 -bt dodecahedron

$gmx/gmx solvate -cp 3K0N_newbox.gro -cs spc216.gro -o 3K0NA_solv.gro -p topol.top

$gmx'/grompp' -f ions.mdp -c 3K0NA_solv.gro -p topol.top -o ions.tpr

echo SOL | $gmx'/genion' -s ions.tpr -o 3K0NA_solv_ions.gro -p topol.top -pname NA -nname CL -neutral

$gmx'/grompp' -f minim.mdp -c 3K0NA_solv_ions.gro -p topol.top -o em.tpr

$gmx'/mdrun' -v -deffnm em


$gmx'/grompp' -f nvt.mdp -c em.gro -p topol.top -o nvt.tpr

$gmx'/mdrun' -v -deffnm nvt  


$gmx'/grompp' -f npt.mdp -c nvt.gro -p topol.top -o npt.tpr
$gmx'/mdrun' -v -deffnm npt  
