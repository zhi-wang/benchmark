from openmm import unit

parameters = 'amoeba2013.xml'
archive = 'dhfr2.arcpdb'
xyzfile = 'dhfr2.pdb'

nff1, nfft2, nfft3 = 64, 64, 64
ewaldalpha = 0.5446 # 7 Ang
elecutoff = 0.7*unit.nanometer
vdwcutoff = 1.2*unit.nanometer
vdwtaper = 0.9*vdwcutoff
polareps = 0.01
verbose = False
