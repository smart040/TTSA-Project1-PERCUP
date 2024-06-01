#!/bin/bash

for power in 2 3 
do
for base in {1..12} 
do
	 echo "python QPDS_12_noise2.py $power $base > out_${power}_${base}.txt"
done
done
