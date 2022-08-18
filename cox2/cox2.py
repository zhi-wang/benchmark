from openmm import unit

parameters = 'amoeba2018.xml'
archive = 'cox2.arcpdb'
xyzfile = 'cox2.pdb'

nfft1, nfft2, nfft3 = 128, 128, 128
ewaldalpha = 0.5446 # 7 Ang
elecutoff = 0.7*unit.nanometer
vdwcutoff = 1.2*unit.nanometer
vdwtaper = 0.9*vdwcutoff
polareps = 0.01
verbose = False
