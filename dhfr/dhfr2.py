from openmm import unit

parameters = 'amoeba2013.xml'
archive = 'dhfr2.arcpdb'
xyzfile = 'dhfr2.pdb'

ewaldalpha = 0.0005
elecutoff = 0.7*unit.nanometer
vdwcutoff = 1.2*unit.nanometer
vdwtaper = 0.9*vdwcutoff
polareps = 0.01
verbose = False
