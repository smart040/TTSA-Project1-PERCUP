#!/bin/bash

for power in 2 
do
for base in {1..12} 
do
	 echo "python QPDS_12.py $power $base > out_${power}_${base}.txt"
done
done
