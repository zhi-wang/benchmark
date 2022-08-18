#!/usr/bin/env python3


from openmm.app import *
from openmm import *
import importlib, os, sys


# xyz and key files
ifile = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location('key', ifile)
key = importlib.util.module_from_spec(spec)
sys.modules['key'] = key
spec.loader.exec_module(key)
xyzfile = os.path.join(os.path.dirname(ifile), key.xyzfile)


# nstep time-step save-frequency ensemble [T] [P]
nstep = int(sys.argv[2])
timestep = float(sys.argv[3])*unit.femtosecond
iwrite = int((float(sys.argv[4])*1000.0+1.0e-6)/float(sys.argv[3]))
ensemble = int(sys.argv[5]) # 1: NVE; 2: NVT; 4: NPT
print('#MDInput {}, {} step, {}, {} step_per_frame, {} ensemble'.format(xyzfile, nstep, timestep, iwrite, ensemble), end='')
kelvin = 1.0*unit.kelvin
if ensemble in [2, 4]:
    kelvin = float(sys.argv[6])*unit.kelvin
    print(', {}'.format(kelvin), end='')
tautemp = 0.2/unit.picosecond
atmsph = 1.0*unit.atmosphere
if ensemble == 4:
    atmsph = float(sys.argv[7])*unit.atmosphere
    print(', {}'.format(atmsph), end='')
volumetrial = 25
print('')


# defaults: verlet / andersen / monte carlo
integrator = VerletIntegrator(timestep)
thermostat = AndersenThermostat(kelvin, tautemp)
barostat = MonteCarloBarostat(atmsph, kelvin, volumetrial)


# getxyz mechanic mdinit
pdb = PDBFile(xyzfile)
forcefield = ForceField(key.parameters)
system = forcefield.createSystem(pdb.topology,
    nonbondedMethod=PME, ewaldErrorTolerance=key.ewaldalpha, nonbondedCutoff=key.elecutoff,
    vdwCutoff=key.vdwcutoff, mutualInducedTargetEpsilon=key.polareps)
if ensemble in [2, 4]:
    system.addForce(thermostat)
if ensemble == 4:
    system.addForce(barostat)
simulation = Simulation(pdb.topology, system, integrator)
simulation.context.setPositions(pdb.positions)
simulation.context.setVelocitiesToTemperature(kelvin)


# mdsave
srStep = True if key.verbose else False
srPotentialEnergy = True if key.verbose else False
srKineticEnergy = True if key.verbose else False
srTemperature = True if key.verbose else False
statereport = StateDataReporter(file=sys.stdout, totalSteps=nstep, separator='\t',
    reportInterval=iwrite, speed=True, remainingTime=True, step=srStep,
    potentialEnergy=srPotentialEnergy,
    kineticEnergy=srKineticEnergy,
    temperature=srTemperature)
pdbreport = PDBReporter(key.archive, iwrite)
simulation.reporters.append(pdbreport)
simulation.reporters.append(statereport)


# run
simulation.step(nstep)
