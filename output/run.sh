#!/bin/bash

INFO9=../../build/info9
DYN9=../../build/dynamic9
OPMM=../dynamic_omm.py

date; hostname; echo; echo

$INFO9

echo; echo NVE; echo; echo

echo DHFR; echo
cp ../dhfr/dhfr2.[xk]* .
$DYN9 dhfr2.xyz        1000 1 0.5 1
$OPMM ../dhfr/dhfr2.py 1000 1 0.5 1
echo; echo
