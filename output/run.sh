#!/bin/bash

../build/info9

echo; echo NVE; echo; echo

../build/dynamic9 ../dhfr/dhfr2.xyz -k ../dhfr/dhfr2.key 1000 1 0.5 1
../dynamic_omm.py ../dhfr/dhfr2.py                       1000 1 0.1 1
