gmx=/home/pattama/local/gromacs/bin

$gmx'/pdb2gmx' -f 3K0O_AAPF.pdb -o 3K0O_processed.gro -water tip3p -ignh -ff amber99sb_modified 

$gmx'/editconf' -f 3K0O_processed.gro -o 3K0O_newbox.gro -c -d 1.0 -bt dodecahedron

$gmx/gmx solvate -cp 3K0O_newbox.gro -cs spc216.gro -o 3K0O_solv.gro -p topol.top

$gmx'/grompp' -f ions.mdp -c 3K0O_solv.gro -p topol.top -o ions.tpr

echo SOL | $gmx'/genion' -s ions.tpr -o 3K0O_solv_ions.gro -p topol.top -pname NA -nname CL -neutral

$gmx'/grompp' -f minim.mdp -c 3K0O_solv_ions.gro -p topol.top -o em.tpr

$gmx'/mdrun' -v -deffnm em


$gmx'/grompp' -f nvt.mdp -c em.gro -p topol.top -o nvt.tpr

$gmx'/mdrun' -v -deffnm nvt  -ntomp 1 -gpu_id 0 -pin off -pinoffset 1


$gmx'/grompp' -f npt.mdp -c nvt.gro -p topol.top -o npt.tpr
$gmx'/mdrun' -v -deffnm npt -ntomp 1 -gpu_id 0 -pin off -pinoffset 1
