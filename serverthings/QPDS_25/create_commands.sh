#!/bin/bash

for power in 2 3 
do
for base in {1..25} 
do
	 echo "python QPDS_25.py $power $base > out_${power}_${base}.txt"
done
done
